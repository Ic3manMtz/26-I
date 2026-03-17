/*
    ANALIZADOR LÉXICO PARA UAMILang
    --------------------------------
    Este programa reconoce:

    - Palabras reservadas
    - Identificadores
    - Números enteros y reales
    - Operadores aritméticos: +, -, *, /, %
    - Operadores relacionales: >, <, =, >=, <=, ==, !=
    - Símbolos especiales: ; ( ) { } [ ] : ,
    - Cadenas entre comillas dobles
    - Comentarios de línea (##) y de bloque (#* ... *#)  (se muestran como tokens)

    El análisis se realiza carácter por carácter,
    simulando el comportamiento básico de un AFD.
*/

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100 // Tamaño máximo del lexema (para identificadores, números, etc.)
#define MAX_COMENTARIO 1000 // Tamaño máximo para comentarios

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
// FUNCIONES AUXILIARES PARA CADENAS Y COMENTARIOS
// ==============================

// Procesa una cadena entre comillas dobles
void procesarCadena(FILE *archivo) {
    char lexema[MAX];
    int i = 0;
    char c;
    while ((c = fgetc(archivo)) != EOF && c != '"') {
        if (i < MAX - 1)
            lexema[i++] = c;
    }
    lexema[i] = '\0';
    if (c == EOF) {
        printf("ERROR_LEXICO: cadena no cerrada\n");
    } else {
        printf("CADENA: \"%s\"\n", lexema);
    }
}

// Procesa un comentario de línea (## ... hasta newline) y lo muestra
void procesarComentarioLinea(FILE *archivo) {
    char lexema[MAX_COMENTARIO];
    int i = 0;
    char c;
    while ((c = fgetc(archivo)) != EOF && c != '\n') {
        if (i < MAX_COMENTARIO - 1)
            lexema[i++] = c;
    }
    lexema[i] = '\0';
    // Mostramos el comentario completo (incluyendo ##)
    printf("COMENTARIO_LINEA: ##%s\n", lexema);
    // El newline se ignora (no se genera token)
}

// Procesa un comentario de bloque (#* ... *#) y lo muestra
void procesarComentarioBloque(FILE *archivo) {
    char lexema[MAX_COMENTARIO];
    int i = 0;
    char c, prev = 0;
    int cerrado = 0;

    while ((c = fgetc(archivo)) != EOF) {
        if (prev == '*' && c == '#') {
            cerrado = 1;
            break; // Encontramos el cierre
        }
        if (i < MAX_COMENTARIO - 1)
            lexema[i++] = c;
        prev = c;
    }
    lexema[i] = '\0';

    if (cerrado) {
        printf("COMENTARIO_BLOQUE: #*%s*#\n", lexema);
    } else {
        printf("ERROR_LEXICO: comentario de bloque no cerrado: #*%s\n", lexema);
    }
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
    case '-':
    case '*':
    case '/':
    case '%':
      printf("OP_ARITMETICO: %c\n", c);
      break;

    // --------------------------------
    // SÍMBOLOS ESPECIALES
    // --------------------------------
    case ';':
    case '(':
    case ')':
    case '{':
    case '}':
    case '[':
    case ']':
    case ':':
    case ',':
      printf("SIMBOLO: %c\n", c);
      break;

    // --------------------------------
    // OPERADORES RELACIONALES
    // Puede ser:
    // >  <  =  !
    // o combinaciones:
    // >=  <=  ==  !=
    // --------------------------------
    case '>':
    case '<':
    case '=': {
      char siguiente = fgetc(archivo);
      if (siguiente == '=') {
        printf("OP_RELACIONAL: %c=\n", c);
      } else {
        ungetc(siguiente, archivo);
        printf("OP_RELACIONAL: %c\n", c);
      }
      break;
    }

    case '!': {
      char siguiente = fgetc(archivo);
      if (siguiente == '=') {
        printf("OP_RELACIONAL: !=\n");
      } else {
        ungetc(siguiente, archivo);
        printf("OP_RELACIONAL: !\n");
      }
      break;
    }

    // --------------------------------
    // CADENAS
    // --------------------------------
    case '"':
      procesarCadena(archivo);
      break;

    // --------------------------------
    // COMENTARIOS
    // --------------------------------
    case '#': {
      char siguiente = fgetc(archivo);
      if (siguiente == '#') {
        procesarComentarioLinea(archivo);
      } else if (siguiente == '*') {
        procesarComentarioBloque(archivo);
      } else {
        // '#' solitario no es válido
        ungetc(siguiente, archivo);
        printf("ERROR_LEXICO: %c\n", c);
      }
      break;
    }

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
      // NÚMEROS ENTEROS Y REALES
      // Regla: dígito+ ( '.' dígito+ )?
      // ----------------------------
      else if (isdigit(c)) {
        i = 0;

        // Acumular parte entera
        while (isdigit(c)) {
          if (i < MAX - 1)
            lexema[i++] = c;
          c = fgetc(archivo);
        }

        // Verificar si hay parte decimal
        if (c == '.') {
          int sig = fgetc(archivo);
          if (isdigit(sig)) {
            // Es número real
            if (i < MAX - 1)
              lexema[i++] = '.';
            c = sig;
            while (isdigit(c)) {
              if (i < MAX - 1)
                lexema[i++] = c;
              c = fgetc(archivo);
            }
            lexema[i] = '\0';
            ungetc(c, archivo);
            printf("NUMERO_REAL: %s\n", lexema);
          } else {
            // No es real: el punto pertenece al siguiente token
            ungetc(sig, archivo);
            ungetc(c, archivo);
            lexema[i] = '\0';
            printf("NUMERO_ENTERO: %s\n", lexema);
          }
        } else {
          // Número entero
          lexema[i] = '\0';
          ungetc(c, archivo);
          printf("NUMERO_ENTERO: %s\n", lexema);
        }
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