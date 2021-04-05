/*

Arrays y funcion scanf.

A diferencia de otras tablas, sí es posible leer e imprimir las cadenas de caracteres de una vez.
Para ello, es necesario utilizar el especificador %s.
La función printf() muestra todos los caracteres de la variable hasta el carácter nulo.
En el ejemplo, la variable nombre está formada por cuatro caracteres y un quinto con el código ASCII 0,
que es la marca de final de cadena.

Al usar scanf(), esta lectura de caracteres tiene un límite, y es que se almacena todo
hasta encontrar un espacio en blanco (‘ ’) o salto de línea (‘\n’).

*/

#include <stdio.h>

#define TAM 8

int main() {
    char nombre[TAM];

    printf("Escribe tu nombre: ");
    scanf('%s', nombre); // cuando leemos cadenas de caracteres con scanf() no hay que utilizar el símbolo ampersand (&) delante de la variable.

    printf("Hola, %s.", nombre);


    return 0;
}