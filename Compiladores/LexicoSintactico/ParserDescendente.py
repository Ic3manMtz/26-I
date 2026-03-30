# ParserDescendente.py

from Alex import AnalizadorLexico
import TipoToken
from SubtipoToken import *


class Parser:

    # =========================
    # CONSTRUCTOR
    # =========================
    def __init__(self, archivo):
        self.lexer = AnalizadorLexico(archivo)
        self.lexer.crearLista()
        self.token_actual = self.lexer.obtenerToken()

    # =========================
    # ERROR
    # =========================
    def error(self, msg="Error sintáctico"):
        raise Exception(
            f"{msg} en línea {self.token_actual.getnumLinea()} -> {self.token_actual.getlexema()}"
        )

    # =========================
    # MATCH
    # =========================
    def match(self, tipo, subtipo=None, lexema=None):

        if (self.token_actual.getTipo() == tipo and
           (subtipo is None or self.token_actual.getSubType() == subtipo) and
           (lexema is None or self.token_actual.getLexema() == lexema)):

            self.token_actual = self.lexer.obtenerToken()
        else:
            esperado = tipo if subtipo is None else subtipo
            self.error(f"Se esperaba '{esperado}'")
    # =========================
    # PROGRAMA
    # =========================
    def programa(self):
        self.lista_sentencias()

        # VALIDACIÓN FINAL (IMPORTANTE)
        if self.token_actual is not None:
            self.error("Se esperaba fin de archivo")

    # =========================
    # LISTA_SENTENCIAS
    # =========================
    def lista_sentencias(self):

        while self.token_actual is not None and not (
            self.token_actual.getTipo() == TipoToken.PALABRA_RESERVADA and
            self.token_actual.getSubType() in [FIN_SI, FIN_MIENTRAS, FIN_PARA, HASTA]
        ):
            self.sentencia()

    # =========================
    # SENTENCIA
    # =========================
    def sentencia(self):

        #  Guardamos token anterior para detectar loops
        token_anterior = self.token_actual

        if self.token_actual.getSubType() in [ENTERO_PR, REAL_PR]:
            self.declaracion()
        elif self.token_actual.getTipo() == TipoToken.IDENTIFICADOR:
            self.asignacion()
        elif self.token_actual.getSubType() == LEER:
            self.lectura()
        elif self.token_actual.getSubType() == IMPRIMIR:
            self.escritura()
        elif self.token_actual.getSubType() == SI:
            self.condicional()
        elif self.token_actual.getSubType() == PARA:
            self.para()
        elif self.token_actual.getSubType() == MIENTRAS:
            self.mientras()
        else:
            self.error("Sentencia no válida")

        #  PROTECCIÓN CONTRA LOOP INFINITO
        if self.token_actual == token_anterior:
            raise Exception("Loop infinito: no se consumió token")

    # =========================
    # DECLARACION
    # =========================
    def declaracion(self):
        # Consume el tipo (entero o real)
        self.match(TipoToken.PALABRA_RESERVADA)

        # Consume el identificador
        self.match(TipoToken.IDENTIFICADOR)

        # Consume el punto y coma
        self.match(TipoToken.SIMBOLO, PUNTO_COMA)
       

    # =========================
    # ASIGNACION
    # =========================
    def asignacion(self):
        # Consume el identidicador
        self.match(TipoToken.IDENTIFICADOR)

        # Consume el =
        self.match(TipoToken.OPERADOR_RELACIONAL, IGUAL)

        # Procesa la expresión del lado derecho
        self.expresion()

        self.match(TipoToken.SIMBOLO, PUNTO_COMA)
       

    # =========================
    # LECTURA
    # =========================
    def lectura(self):
        # Cosume "leer"
        self.match(TipoToken.PALABRA_RESERVADA, LEER)

        # Consume el identificador donde se guarda el valor
        self.match(TipoToken.IDENTIFICADOR)

        self.match(TipoToken.SIMBOLO, PUNTO_COMA)
       

    # =========================
    # ESCRITURA
    # =========================
    def escritura(self):
        # Consume "imprimir"
        self.match(TipoToken.PALABRA_RESERVADA, IMPRIMIR)

        # Procesa lo que se imprimirá
        self.expresion()

        self.match(TipoToken.SIMBOLO, PUNTO_COMA)
       
    # =========================
    # CONDICION
    # =========================
    def condicion(self):
        # Lado izquierdo de la comparación
        self.expresion()

        # Operador relacional
        self.match(TipoToken.OPERADOR_RELACIONAL)

        # Lado derecho de la comparación
        self.expresion()
       

    # =========================
    # CONDICIONAL
    # =========================
    def condicional(self):
        # Consume "si"
        self.match(TipoToken.PALABRA_RESERVADA, SI)

        # Procesa la condición
        self.condicion()

        # Consume "entonces"
        self.match(TipoToken.PALABRA_RESERVADA, ENTONCES)

        # Procesa el cuerpo del si
        self.lista_sentencias()

        # Consume "finSi"
        self.match(TipoToken.PALABRA_RESERVADA, FIN_SI)
        

    # =========================
    # MIENTRAS
    # =========================
    def mientras(self):
        # Consume "mientras"
        self.match(TipoToken.PALABRA_RESERVADA, MIENTRAS)

        # Procesa la codición
        self.condicion()

        # Consume "hacer"
        self.match(TipoToken.PALABRA_RESERVADA, HACER)
        
        # Procesa el cuerpo del ciclo
        self.lista_sentencias()

        # Consume "finMientras"
        self.match(TipoToken.PALABRA_RESERVADA, FIN_MIENTRAS)


    # =========================
    # PARA
    # =========================
    def para(self):
        # Consume "para"
        self.match(TipoToken.PALABRA_RESERVADA, PARA)

        # Consume el identificador 
        self.match(TipoToken.IDENTIFICADOR)

        # Consume "="
        self.match(TipoToken.OPERADOR_RELACIONAL, IGUAL)

        # Expresion de inicio
        self.expresion()

        # Consume "hasta"
        self.match(TipoToken.PALABRA_RESERVADA, HASTA)

        # Expresion de fin
        self.expresion()

        # Consume "entonces"
        self.match(TipoToken.PALABRA_RESERVADA, ENTONCES)

        # Cuerpo del ciclo
        self.lista_sentencias()

        # Consume "finPara"
        self.match(TipoToken.PALABRA_RESERVADA, FIN_PARA)
        
    # =========================
    # EXPRESION
    # =========================
    def expresion(self):
        self.termino()

        # Mientras haya + o - seguimos procesando
        while(self.token_actual is not None and 
              self.token_actual.getTipo() == TipoToken.OPERADOR_ARITMETICO and
              self.token_actual.getSubType() in [OPERADOR_SUMA, OPERADOR_RESTA]):
            
            self.match(TipoToken.OPERADOR_ARITMETICO)
            self.termino()
        

    # =========================
    # TERMINO
    # =========================
    def termino(self):
        self.factor()
        # Mientras haya * o / seguimos procesando factores
        while (self.token_actual is not None and
            self.token_actual.getTipo() == TipoToken.OPERADOR_ARITMETICO and
            self.token_actual.getSubType() in [OPERADOR_MULTIPLICACION, OPERADOR_DIVISIOM]):
            self.match(TipoToken.OPERADOR_ARITMETICO)
            self.factor()
            
    # =========================
    # FACTOR
    # =========================
    # Regla: IDENTIFICADOR | NUMERO ENTERO | NUMERO REAL | (EXPRESION)
    def factor(self):
        if self.token_actual.getTipo() == TipoToken.IDENTIFICADOR:
            self.match(TipoToken.IDENTIFICADOR)

        elif self.token_actual.getTipo() == TipoToken.NUMERO and \
            self.token_actual.getSubType() == ENTERO:
            self.match(TipoToken.NUMERO)

        elif self.token_actual.getTipo() == TipoToken.NUMERO and \
            self.token_actual.getSubType() == REAL:
            self.match(TipoToken.NUMERO)

        elif (self.token_actual.getTipo() == TipoToken.SIMBOLO and
            self.token_actual.getSubType() == PAREN_IZQ):
            self.match(TipoToken.SIMBOLO, PAREN_IZQ)
            self.expresion()
            self.match(TipoToken.SIMBOLO, PAREN_DER)

        else:
            self.error("Factor inválido")


# =========================
# MAIN
# =========================
import sys

if __name__ == "__main__":
    try:
        #  Validar que el usuario pase el nombre del archivo
        if len(sys.argv) < 2:
            print("Uso: python ParserDescendente.py <archivo>")
            sys.exit(1)

        #  Nombre del archivo desde consola
        archivo = sys.argv[1]

        # Crear parser con el archivo indicado
        parser = Parser(archivo)
        parser.programa()

        print("Programa válido")

    except Exception as e:
        print("ERROR:", e)