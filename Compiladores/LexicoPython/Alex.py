import re
import TipoToken
import SubtipoToken
import Token

EXPRESIONES_REGULARES = [
    
    # #\*       - Se usa \ para poder escapar y que * sea literal
    # [\s\S]*?  - Cualquier caracter incluyendo saltos de línea \s(espacio,tab y salto de línea)
    #             \S es todo lo demás. *? cero o más, pero lo mínimo posible
    # \*#       - Cierre literal *#
    ("COMENTARIO_BLOQUE", r'#\*[\s\S]*?\*#'),

    # ##        - Inicio literal
    # [^\n]*    - Cualquier caracter excepto saltos de línea. ^ es una negación
    ("COMENTARIO_LINEA", r'##[^\n]*'),

    # [^"\n]    - Cualquier caracter excepto " y salto de línea
    ("CADENA", r'"[^"\n]*"'),
    ("CADENA_ERROR", r'"[^"\n]*'),

    # \d        - Cualquier dígito del 0 al 9
    # \.        - Punto literal
    # +         - Uno o más
    ("NUMERO_REAL", r'\d+\.\d+'),
    ("NUMERO_ENTERO", r'\d+'),

    # [a-zA-Z_] - El primer caracter debe ser letra o guión bajo
    # [a-zA-Z0-9_]* - Los siguientes pueden ser letra, dígito o guión bajo, cero o más veces
    ("IDENTIFICADOR", r'[a-zA-Z_][a-zA-Z0-9_]*'),

    # Uso del or | para probar cada uno
    ("OP_RELACIONAL", r'>=|<=|==|!=|>|<|=|!'),

    # Clase de caracteres, toma exactamente uno de los que están dentro
    ("OP_ARITMETICO", r'[+\-*/%]'),

    # Clase de símbolos, toma exactamente uno de los que están dentro
    ("SIMBOLO", r'[;()\[\]{}:,]'),

    ("NEWLINE", r'\n'),
    # Espacio o tab, uno o más
    ("ESPACIO", r'[ \t]+'),

    # Cualquier otro carácter
    ("ERROR_LEXICO", r'.'),
]

# Toma cada tupla de patrones y la convierte en un regex gigante
PATRON_MAESTRO = re.compile(
    '|'.join(f'(?P<{nombre}>{regex})' for nombre, regex in EXPRESIONES_REGULARES)
)

class AnalizadorLexico:

    numLinea = 1          # Número de línea actual del programa
    L = []                # Lista donde se almacenarán los tokens encontrados
    codigo = ""           # Cadena donde se guarda todo el código fuente

    # DICCIONARIO DE SUBTIPOS
    # Sirven para mapear el lexema capturado a su constante SubtipoToken
    SUBTIPOS_ARITMETICO = {
        "+": SubtipoToken.OPERADOR_SUMA,
        "-": SubtipoToken.OPERADOR_RESTA,
        "*": SubtipoToken.OPERADOR_MULTIPLICACION,
        "/": SubtipoToken.OPERADOR_DIVISIOM,
        "%": SubtipoToken.OPERADOR_MODULO,
    }

    SUBTIPOS_RELACIONAL = {
        ">": SubtipoToken.MAYOR,
        "<": SubtipoToken.MENOR,
        "=": SubtipoToken.IGUAL,
        ">=": SubtipoToken.MAYOR_IGUAL,
        "<=": SubtipoToken.MENOR_IGUAL,
        "==": SubtipoToken.IGUAL_IGUAL,
        "!=": SubtipoToken.DIFERENTE,
        "!": SubtipoToken.NOT,
    }

    SUBTIPOS_ESPECIAL = {
        ";": SubtipoToken.PUNTO_COMA,
        "(": SubtipoToken.PAREN_IZQ,
        ")": SubtipoToken.PAREN_DER,
        "{": SubtipoToken.LLAVE_IZQ,
        "}": SubtipoToken.LLAVE_DER,
        "[": SubtipoToken.CORCHETE_IZQ,
        "]": SubtipoToken.CORCHETE_DER,
        ":": SubtipoToken.DOS_PUNTOS,
        ",": SubtipoToken.COMA,
    }

    # Constructor: lee el archivo y guarda todo su contenido en self.codigo
    def __init__(self, programa):

        archivo = open(programa, 'r')
        lineas = archivo.readlines()

        for linea in lineas:
            self.codigo = self.codigo + linea
        
        archivo.close()


    # Devuelve el siguiente token de la lista
    def obtenerToken(self):

        if len(self.L) > 0:
            return self.L.pop(0)

        return None


    # Permite regresar un token a la lista (útil para el parser)
    def regresarToken(self, t):

        self.L.insert(0, t)


    # Verifica si un lexema es una palabra reservada
    def esPalabraReservada(self, lexeme):

        palabras = {
            "if": SubtipoToken.IF,
            "else": SubtipoToken.ELSE,
            "while": SubtipoToken.WHILE,
            "int": SubtipoToken.INT,
            "float": SubtipoToken.FLOAT,
            "return": SubtipoToken.RETURN,

            "entero": SubtipoToken.ENTERO_PR,
            "imprimir": SubtipoToken.IMPRIMIR,
            "si": SubtipoToken.SI,
            "entonces": SubtipoToken.ENTONCES,
            "finSi": SubtipoToken.FIN_SI,
            "mientras": SubtipoToken.MIENTRAS,
            "finMientras": SubtipoToken.FIN_MIENTRAS,
        }

        if lexeme in palabras:
            return palabras[lexeme]

        return None


    # Método que analiza el código y genera la lista de tokens
    def crearLista(self):
        index = 0

        while index < len(self.codigo):

            match = PATRON_MAESTRO.match(self.codigo, index)

            if match:

                grupo = match.lastgroup # Nombre del patrón que casó
                lexema = match.group()  # Texto capturado 

                # Espacios y saltos de línea
                if grupo == "ESPACIO":
                    index = match.end()
                    continue
                
                if grupo == "NEWLINE":
                    self.numLinea += 1
                    index = match.end()
                    continue

                # Comentarios
                if grupo == "COMENTARIO_LINEA":
                    t = Token.Token(TipoToken.COMENTARIO_LINEA, None, lexema, self.numLinea)
                    self.L.append(t)
                elif grupo == "COMENTARIO_BLOQUE":
                    # Contamos los saltos de línea dentro del bloque
                    self.numLinea += lexema.count('\n')
                    t = Token.Token(TipoToken.COMENTARIO_BLOQUE, None, lexema, self.numLinea)
                    self.L.append(t)

                # Cadenas
                elif grupo == "CADENA":
                    t = Token.Token(TipoToken.CADENA, None, lexema, self.numLinea)
                    self.L.append(t)
                elif grupo == "CADENA_ERROR":
                    print(f"ERROR_LEXICO en línea {self.numLinea}: cadena no cerrada: {lexema}")

                # Numeros
                elif grupo == "NUMERO_REAL":
                    t = Token.Token(TipoToken.NUMERO, SubtipoToken.REAL, lexema, self.numLinea)
                    self.L.append(t)
                
                elif grupo == "NUMERO_ENTERO":
                    t = Token.Token(TipoToken.NUMERO, SubtipoToken.ENTERO, lexema, self.numLinea)
                    self.L.append(t)

                # Identifiadores y palabras reservadas
                elif grupo == "IDENTIFICADOR":
                    subtipo = self.esPalabraReservada(lexema)
                    if subtipo is not None:
                        t = Token.Token(TipoToken.PALABRA_RESERVADA, subtipo, lexema, self.numLinea)
                    else:
                        t = Token.Token(TipoToken.IDENTIFICADOR, None, lexema, self.numLinea)

                    self.L.append(t)

                # Operadores relacionales
                elif grupo == "OP_RELACIONAL":
                    subtipo = self.SUBTIPOS_RELACIONAL.get(lexema, None)
                    t = Token.Token(TipoToken.OPERADOR_RELACIONAL, subtipo, lexema, self.numLinea)
                    self.L.append(t)

                # Operadores aritmeticos
                elif grupo == "OP_ARITMETICO":
                    subtipo = self.SUBTIPOS_ARITMETICO.get(lexema, None)
                    t = Token.Token(TipoToken.OPERADOR_ARITMETICO, subtipo, lexema, self.numLinea)
                    self.L.append(t)

                # Simbolos especiales
                elif grupo == "SIMBOLO":
                    subtipo = self.SUBTIPOS_ESPECIAL.get(lexema, None)
                    t = Token.Token(TipoToken.SIMBOLO, subtipo, lexema, self.numLinea)
                    self.L.append(t)

                # Error lexico
                elif grupo == "ERROR_LEXICO":
                    print(f"ERROR_LEXICO en línea {self.numLinea}: Simbolo no reconocido: {lexema}")


                index = match.end()