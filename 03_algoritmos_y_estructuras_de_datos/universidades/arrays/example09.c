/*

Conociendo la funcion strlen que nos permite saber la longitud de una cadena de caracteres (string)
Esto nos ayudara mas adelante con los arrays

*/

#include <stdio.h>
#include <string.h>

#define DIM 20

int main() {
    char nombre1[DIM] = "Ana";
    char nombre2[DIM] = "Anacleto";
    char nombre3[DIM] = "Anastasia";
  
    printf("La longitud de nombre1 es %d\n", strlen(nombre1));
    printf("La longitud de nombre2 es %d\n", strlen(nombre2));
    printf("La longitud de nombre3 es %d\n", strlen(nombre3));
  
    return 0;
}