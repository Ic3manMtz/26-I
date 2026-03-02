/*
    ANALIZADOR LÉXICO PARA UAMILang
    --------------------------------
    Este programa reconoce:

    - Palabras reservadas
    - Identificadores
    - Números enteros
    - Operadores aritméticos
    - Operadores relacionales
    - Símbolos especiales

    El análisis se realiza carácter por carácter,
    simulando el comportamiento básico de un AFD.
*/

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100 // Tamaño máximo del lexema

// ==============================
// TABLA DE PALABRAS RESERVADAS
// ==============================

const char *reservadas[] = {"entero", "imprimir", "si",         "entonces",
                            "finSi",  "mientras", "finMientras"};

// --------------------------------------
// Función que verifica si un lexema
// pertenece al conjunto de reservadas
// --------------------------------------

int esReservada(char *lexema, int numReservadas) {
  int i;

  for (i = 0; i < numReservadas; i++) {
    if (strcmp(lexema, reservadas[i]) == 0)
      return 1; // Sí es palabra reservada
  }

  return 0; // No es palabra reservada
}

// ==============================
// FUNCIÓN PRINCIPAL DE ANÁLISIS
// ==============================

void analizar(FILE *archivo) {

  char c;           // Carácter actual
  char lexema[MAX]; // Buffer para almacenar el token
  int i;            // Índice del lexema

  // Leer carácter por carácter hasta EOF
  while ((c = fgetc(archivo)) != EOF) {

    // Ignorar espacios, tabulaciones y saltos de línea
    if (isspace(c))
      continue;

    // ==============================
    // SWITCH PRINCIPAL
    // ==============================

    switch (c) {

    // --------------------------------
    // OPERADORES ARITMÉTICOS
    // --------------------------------
    case '+':
      printf("OP_ARITMETICO: %c\n", c);
      break;

    // --------------------------------
    // SÍMBOLOS ESPECIALES
    // --------------------------------
    case ';':
      printf("SIMBOLO: %c\n", c);
      break;

    // --------------------------------
    // OPERADORES RELACIONALES
    // Puede ser:
    // >  <  =  !
    // o combinaciones:
    // >=  <=  ==  !=
    // --------------------------------
    case '!':
      char siguiente = fgetc(archivo);

      // Si el siguiente carácter es '='
      // entonces es un operador relacional doble
      if (siguiente == '=') {
        printf("OP_RELACIONAL: %c=\n", c);
      } else {
        // Si no es '=', regresamos el carácter
        // porque pertenece al siguiente token
        ungetc(siguiente, archivo);
        printf("OP_RELACIONAL: %c\n", c);
      }

      break;

    // --------------------------------
    // CASO GENERAL
    // Aquí analizamos identificadores
    // y números o errores lexicos
    // --------------------------------
    default:
      // ----------------------------
      // IDENTIFICADORES O RESERVADAS
      // Regla: letra (letra|digito)*
      // ----------------------------
      if (isalpha(c)) {

        i = 0;

        // Guardamos el primer carácter
        lexema[i] = c;
        i = i + 1;

        // Mientras sean letras o dígitos
        while (isalnum(c = fgetc(archivo))) {
          // Evitamos desbordamiento
          if (i < MAX - 1) {
            lexema[i] = c;
            i = i + 1;
          }
        }

        // Cerramos la cadena
        lexema[i] = '\0';

        // Regresamos el carácter que rompió el ciclo
        ungetc(c, archivo);

        // Verificamos si es reservada
        if (esReservada(lexema, 7))
          printf("PALABRA_RESERVADA: %s\n", lexema);
        else
          printf("IDENTIFICADOR: %s\n", lexema);
      }

      // ----------------------------
      // NÚMEROS ENTEROS
      // Regla: digito+
      // ----------------------------
      else if (isdigit(c)) {

      }

      // ----------------------------
      // ERROR LÉXICO
      // ----------------------------
      else {
        printf("ERROR_LEXICO: %c\n", c);
      }
    }
  }
}

// ==============================
// FUNCIÓN MAIN
// ==============================

int main() {

  // Abrimos archivo de entrada
  FILE *archivo = fopen("entrada.txt", "r");

  if (archivo == NULL) {
    printf("No se pudo abrir el archivo.\n");
    return 1;
  }

  // Ejecutamos el análisis léxico
  analizar(archivo);

  // Cerramos archivo
  fclose(archivo);

  return 0;
}