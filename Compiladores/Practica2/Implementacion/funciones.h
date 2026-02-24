#include<stdio.h>

typedef struct Cadena{
    char * wn;
    int longitud;
}Cadena;

typedef struct Automata{
    int num_estados;
    int num_simbolos;
    int estado_inicial;
    int * estados_finales;
    int num_finales;
    int** transiciones;
}Automata;

typedef Cadena * cadena;
typedef Automata * automata;

cadena crearCadena();
void pedirCadena(cadena);
void liberarCadena(cadena);


/*
num_estados: número de estados
num_simbolos: número de símbolos del alfabeto
estado_inicial: estado inicial
estados_finales: arreglo con los estados finales
transiciones: matriz de transiciones
*/
automata crearAutomata(int num_estados, int num_simbolos, int estado_inicial,
                        int* estados_finales, int num_finales, int** transiciones);
int procesarCadena(automata, cadena);
void liberarAutomata(automata);
int crearAutomatas(automata automatas[4]);

void menuExpresiones(int, automata automatas[4]);
