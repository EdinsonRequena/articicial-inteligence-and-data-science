/*

Cadena de caracteres en arrays

Siempre y cuando no alcancemos el máximo de caracteres en la información de la variable, 
los elementos vacíos se completan automáticamente con el carácter nulo (código ASCII: 0 o '\0'), 
por lo que no es necesario especificarlos. Por lo tanto, la inicialización anterior refleja

*/

#include <stdio.h>

#define TAM 8

int main() {
    char nombre[TAM] = {'A', 'n', 'a'}; // Elemento a elemento
    char nombre1[TAM] = "Eddy"; // Conjunto

//  todos los del array que no se especifican automaticamente con el codigo ASCII 0 (NULL)

    printf("Hola, %s.\n", nombre);
    printf("Hola, %s.", nombre1);

    return 0;
}