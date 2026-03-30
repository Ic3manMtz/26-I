#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programa principal que ejecuta el analizador léxico.

Este programa:
1. Crea un objeto del analizador léxico.
2. Lee el archivo de entrada (programa.txt).
3. Genera la lista de tokens del programa.
4. Imprime cada token encontrado.
"""

# Importa la clase AnalizadorLexico
import AnalizadorLexico


# Crear una instancia del analizador léxico
# Se le pasa como argumento el archivo que contiene el programa fuente
l = AnalizadorLexico.AnalizadorLexico("programa.txt")


# Genera la lista de tokens a partir del código fuente
l.crearLista()


# Obtener el primer token
t = l.obtenerToken()


# Mientras existan tokens en la lista
while t != None:

    # Imprimir el token encontrado
    print("Token: ", t)

    # Obtener el siguiente token
    t = l.obtenerToken()
