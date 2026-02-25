#include<stdio.h>
#include"funciones.h"

int main(){
    int opc;
    printf("\n\n\t***** Práctica 2 *****\n");

    automata automatas[4];
    if(crearAutomatas(automatas) != 0){
        printf("Error al crear los autómatas, saliendo\n");
        return 1;
    }

    do{
        printf("\n Elija la expresión regular a revisar \n\n");
        printf("1.- (a*)b(a*)\n");
        printf("2.- (a*)bb(a*)\n");
        printf("3.- a*b*\n");
        printf("4.- (a*)b(a*)b(a*)\n");
        printf("5.- Salir\n\n");

        scanf("%d", &opc);
        getchar();

        if(opc>=1 && opc<=4){
            menuExpresiones(opc, automatas);
        }else if(opc != 5){
            printf("Opción inválida, intente de nuevo\n");
        }
    }while(opc != 5);

    for(int i=0; i<4; i++){
        liberarAutomata(automatas[i]);
    }


    return 0;
}