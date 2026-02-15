#include<stdio.h>
#include<conio.h>
main()
{
    float radio, area;
    area = 0;
    radio = 0;
    printf("Area de un ciruculo");
    // entrada de datos
    printf("\nIntroduce el radio =>");
    scanf("%f", &radio);
    /* proceso para calcular el Area total*/
    area = 3.1416 * pow(radio, 2);
    // salida
    printf("\n\nArea = %5.2f", area);
    getch();
}