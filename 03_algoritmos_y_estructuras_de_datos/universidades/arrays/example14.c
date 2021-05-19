/*

La funcion strcmp() permite comparar dos cadenas de caracteres que se le indican como argumentos, 
especificando si la primera es menor, mayor o igual que la segunda 
a través de un número negativo, positivo o 0, respectivamente.

*/

#include <stdio.h>
#include <string.h>

#define DIM 8

int main() {
    char nombre1[DIM] = "Ana";
    char nombre2[DIM] = "Anabel";

    printf("Ana vs. Anabel: %d\n", strcmp(nombre1, nombre2));
    printf("Ana vs. Ana: %d\n", strcmp(nombre1, nombre1));
    printf("Anabel vs. Ana: %d\n", strcmp(nombre2, nombre1));

    return 0;
}