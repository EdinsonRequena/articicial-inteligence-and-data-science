/*

Sin ejecutar el programa, di cuales son las salidas que tiene.

*/

#include <stdio.h>

#define DIM 8

int main() {
    char nombre[DIM] = "Ana Gil";

    printf("Hola, %s.\n", nombre);
   
    nombre[3] = 'n';
    nombre[5] = 0;
   
    printf("Hola, %s.", nombre);

    return 0;
}