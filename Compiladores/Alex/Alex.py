#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analizador léxico simple que reconoce operadores relacionales,
números enteros positivos e identificadores.
"""

import re
import TipoToken
import SubTipoToken
import Token


class AnalizadorLexico:

    numLinea = 1          # Número de línea actual del programa
    L = []                # Lista donde se almacenarán los tokens encontrados
    codigo = ""           # Cadena donde se guarda todo el código fuente

    # Constructor: lee el archivo y guarda todo su contenido en self.codigo
    def __init__(self, programa):

        archivo = open(programa, 'r')
        lineas = archivo.readlines()

        for linea in lineas:
            self.codigo = self.codigo + linea


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
            "if": SubTipoToken.IF,
            "else": SubTipoToken.ELSE,
            "while": SubTipoToken.WHILE,
            "int": SubTipoToken.INT,
            "float": SubTipoToken.FLOAT,
            "return": SubTipoToken.RETURN
        }

        if lexeme in palabras:
            return palabras[lexeme]

        return None


    # Método que analiza el código y genera la lista de tokens
    def crearLista(self):

        patron = re.compile(r'(>=|<=|>|<|\d+|[a-zA-Z_][a-zA-Z0-9_]*)')

        index = 0

        while index < len(self.codigo):

            match = patron.match(self.codigo, index)

            if match:

                lexema = match.group()

                # Numero
                if lexema.isdigit():
                    t = Token.Token(TipoToken.NUMERO, None, lexema, self.numLinea)

                # Identificador o palabra reservada
                elif lexema[0].isalpha() or lexema[0] == "_":

                    subtipo = self.esPalabraReservada(lexema)

                    if subtipo != None:
                        t = Token.Token(TipoToken.PALABRA_RESERVADA, subtipo, lexema, self.numLinea)
                    else:
                        t = Token.Token(TipoToken.IDENTIFICADOR, None, lexema, self.numLinea)

                # Operadores relacionales
                else:
                    t = Token.Token(TipoToken.OPERADOR_RELACIONAL, None, lexema, self.numLinea)

                self.L.append(t)

                index = match.end()

            else:

                print("Error léxico en línea", self.numLinea, "símbolo:", self.codigo[index])

                index = index + 1
