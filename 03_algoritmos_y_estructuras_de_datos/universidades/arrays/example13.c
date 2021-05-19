/*

Funcion gets() y getchar()
Cuando queramos usar la funcion scanf() y gets() sin que genere conflictos debemos usar la funcion getchar() de la siguiente forma.

*/

#include <stdio.h>

#define TAM 16

int main() {
    char nombre[TAM], ciudad[TAM];

    printf("Introduce tu nombre: ");
    scanf("%s", nombre);
    getchar();

    printf("Introduce tu ciudad de residencia: ");
    gets(ciudad);

    printf("Hola, %s. Vives en %s.\n", nombre, ciudad);

    return 0;
}