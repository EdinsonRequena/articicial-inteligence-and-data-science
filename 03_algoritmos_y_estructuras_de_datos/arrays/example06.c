/*

Matriz o tablas bidemensionales

*/

#include <stdio.h>

int main() {
    int num[2][4] = {{3, 9}, {12, 1, 5}}; // Esta es una matriz de 2 filas y 4 columnas
                                          // primera fila = {3, 9, 0, 0}, segunda fila = {12, 1, 5, 0}
    int deter;

    deter = (num[0][0] * num[1][1] * num[1][2] * num[0][3]) - (num[1][0] * num[0][1] * num[0][2] * num[1][3]);

    printf("El determinante es %d: ", deter);

    return 0;
}
