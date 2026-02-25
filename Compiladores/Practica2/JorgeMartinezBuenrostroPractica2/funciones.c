#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include"funciones.h"

cadena crearCadena(){
    cadena a;

    a = (cadena)malloc(sizeof(Cadena));
    if(a == NULL){
        return NULL;
    }

    a->wn = (char*)malloc(sizeof(char));
    if(a->wn == NULL){
        free(a);
        return NULL;
    }

    a->wn[0] = '\0';
    a->longitud = 0;

    return a;
}

void pedirCadena(cadena a){
    scanf("%[^\n]s",a->wn);
    getchar();
    
    int longitud = 0;
    while(a->wn[longitud] != '\0'){
        longitud++;
    }

    a->longitud = longitud;
}

void liberarCadena(cadena a){
    if(a != NULL){
        free(a->wn);
        free(a);
    }
}

automata crearAutomata(int num_estados, int num_simbolos, int estado_inicial,
                        int* estados_finales, int num_finales, int** transiciones){

    if(num_estados<=0 || num_simbolos<=0 || estado_inicial<0 || num_finales<0 || transiciones==NULL){
        return NULL;
    }

    automata a = (automata)malloc(sizeof(Automata));
    if(a == NULL){
        return NULL;
    }

    a->num_estados = num_estados;
    a->num_simbolos = num_simbolos;
    a->estado_inicial = estado_inicial;
    a->num_finales = num_finales;

    a->estados_finales = (int*)malloc(num_finales * sizeof(int));
    if(a->estados_finales==NULL && num_finales>0){
        free(a);
        return NULL;
    }
    for(int i=0; i<num_finales; i++){
        a->estados_finales[i]=estados_finales[i];
    }

    a->transiciones = (int**)malloc(num_estados * sizeof(int*));
    if(a->transiciones == NULL){
        free(a->estados_finales);
        free(a);
        return NULL;
    }

    for(int i = 0; i < num_estados; i++) {
        a->transiciones[i] = (int*)malloc(num_simbolos * sizeof(int));
        if(a->transiciones[i] == NULL){
            for(int j=0; j<i; j++){
                free(a->transiciones[j]);
            }
            free(a->transiciones);
            free(a->estados_finales);
            free(a);
            return NULL;
        }

        for(int j=0; j<num_simbolos; j++){
            a->transiciones[i][j] = transiciones[i][j];
        }
    }

    return a;
}

int procesarCadena(automata a, cadena c){
    if(a==NULL || c==NULL){
        return 0;
    }

    int estado_actual = a->estado_inicial;

    printf("\n **** Transiciones del autómata ****\n\n");
    for(int i=0; i<c->longitud; i++){
        char ch = c->wn[i];
        int simbolo = ch - 'a';
        if(simbolo<0 || simbolo >= a->num_simbolos){
            printf("Símbolo inválido [%c]", simbolo+'a');
            return 0;
        }

        int estado_anterior = estado_actual;
        estado_actual = a->transiciones[estado_actual][simbolo];

        printf("Delta(q%d, %c)=q%d\n", estado_anterior, simbolo+'a', estado_actual);
        if(estado_actual == -1){
            return 0;
        }
    }

    printf("\n\n Estado final q%d", estado_actual);

    for(int i=0; i<a->num_finales; i++){
        if(a->estados_finales[i] == estado_actual){
            return 1;
        }
    }

    return 0;
}

void liberarAutomata(automata a) {
    if (a == NULL) return;
    for (int i = 0; i < a->num_estados; i++) {
        free(a->transiciones[i]);
    }
    free(a->transiciones);
    free(a->estados_finales);
    free(a);
}

int crearAutomatas(automata automatas[4]) {
    // Autómata 1: a*ba*
    int num_estados1 = 3;
    int num_simbolos = 2;  // a, b
    int inicial1 = 0;
    int finales1[] = {1};
    int num_finales1 = 1;
    int transiciones1[3][2] = {
        {0, 1},  // q0: a->q0, b->q1
        {1, 2},  // q1: a->q1, b->q2 
        {2, 2}   // q2: a->q2, b->q2
    };
    int* transiciones_ptr1[3] = {transiciones1[0], transiciones1[1], transiciones1[2]};

    // Autómata 2: a*bba*
    int num_estados2 = 4;
    int inicial2 = 0;
    int finales2[] = {2};
    int num_finales2 = 1;
    int transiciones2[4][2] = {
        {0, 1},  // q0: a->q0, b->q1
        {3, 2},  // q1: a->q3, b->q2
        {2, 3},  // q2: a->q2, b->q3
        {3, 3}   // q3: a->q3, b->q3
    };
    int* transiciones_ptr2[4] = {transiciones2[0], transiciones2[1], transiciones2[2], transiciones2[3]};

    // Autómata 3: a*b*
    int num_estados3 = 3;
    int inicial3 = 0;
    int finales3[] = {0, 1};  // q0 y q1 son finales
    int num_finales3 = 2;
    int transiciones3[3][2] = {
        {0, 1},  // q0: a->q0, b->q1
        {2, 1},  // q1: a->q2, b->q1
        {2, 2}   // q2: a->q2, b->q2
    };
    int* transiciones_ptr3[3] = {transiciones3[0], transiciones3[1], transiciones3[2]};

    // Autómata 4: a*ba*ba*
    int num_estados4 = 4;
    int inicial4 = 0;
    int finales4[] = {2};
    int num_finales4 = 1;
    int transiciones4[4][2] = {
        {0, 1},  // q0: a->q0, b->q1
        {1, 2},  // q1: a->q1, b->q2
        {2, 3},  // q2: a->q2, b->q3
        {3, 3}   // q3: a->q3, b->q3
    };
    int* transiciones_ptr4[4] = {transiciones4[0], transiciones4[1], transiciones4[2], transiciones4[3]};

    automatas[0] = crearAutomata(num_estados1, num_simbolos, inicial1,
                                 finales1, num_finales1, transiciones_ptr1);
    if (automatas[0] == NULL) return -1;

    automatas[1] = crearAutomata(num_estados2, num_simbolos, inicial2,
                                 finales2, num_finales2, transiciones_ptr2);
    if (automatas[1] == NULL) {
        liberarAutomata(automatas[0]);
        return -1;
    }

    automatas[2] = crearAutomata(num_estados3, num_simbolos, inicial3,
                                 finales3, num_finales3, transiciones_ptr3);
    if (automatas[2] == NULL) {
        liberarAutomata(automatas[0]);
        liberarAutomata(automatas[1]);
        return -1;
    }

    automatas[3] = crearAutomata(num_estados4, num_simbolos, inicial4,
                                 finales4, num_finales4, transiciones_ptr4);
    if (automatas[3] == NULL) {
        liberarAutomata(automatas[0]);
        liberarAutomata(automatas[1]);
        liberarAutomata(automatas[2]);
        return -1;
    }

    return 0;
}

void menuExpresiones(int opc, automata automatas[4]){
   if (opc<1 || opc>4) return;

    cadena cad = crearCadena();
    if (cad == NULL) {
        printf("Error al crear la cadena.\n");
        return;
    }

    printf("Ingrese la cadena a evaluar (solo a y b, para cadena vacía solo presiona ENTER): ");
    pedirCadena(cad);

    if (procesarCadena(automatas[opc - 1], cad)) {
        printf("\tCADENA ACEPTADA\n\n");
    } else {
        printf("\tCADENA RECHAZADA\n\n");
    }

    liberarCadena(cad);
}
