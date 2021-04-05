/*

Funcion gets()
Cuando queramos almacenar más de una palabra, utilizaremos la función gets()de la siguiente forma

*/

#include <stdio.h>

#define LON 16

int main() {
    char nombre[LON];

    printf("Introduce tu nombre: ");
    gets(nombre);

    printf("Hola, %s.", nombre);

    return 0;
}