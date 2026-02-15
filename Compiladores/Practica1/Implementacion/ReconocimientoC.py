import re

file = open("CalculoArea.c", mode='r')
archivo = file.read()

# Definición de patrones para cada categoría léxica
# (?<=Y)X Coincide X solo si es precedido con Y
# X(?=Y) Coincide X solo si Y está despúes

patrones = [
    ("IDENTIFICADOR", r'(?<=[ \t])[A-Za-z_][A-Za-z0-9_]*(?=[ ,;])'),
    ("NUMERO_ENTERO", r"(?<=[ \t(])\d+(?=[ ,;)])"),
    ("NUMERO_REAL",   r"[0-9]+\.[0-9]+"),
    ("CADENA",        r'"[^"]*"'),
    ("COMENTARIO_LINEA",  r"//[^\n]*"),
    ("COMENTARIO_MULTI",  r"/\*.*?\*/"),
    ("OPERADOR_ARITMETICO", r"[+\-*/%=]"),
    ("OPERADOR_RELACIONAL", r"<=|>=|>|<"),
    ("OPERADOR_LOGICO",     r"&&|\|\|"),
]

# Recorrer cada patrón
for nombre, patron in patrones:
    print(f"\n--- {nombre} ---")
    print(f"Patrón: {patron}")

    coincidencias = re.findall(patron, archivo)
    if coincidencias:
        print(f"Todas las coincidencias: {coincidencias}")
    else:
        print("Todas las coincidencias: No encontrado")