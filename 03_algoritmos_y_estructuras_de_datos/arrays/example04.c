/*

Matriz o tablas bidemensionales

*/

#include <stdio.h>

#define DIM 2

int main() {
    int num[DIM][DIM] = {{1, 3}, {5, 3}};
    int deter;

    deter = (num[0][0] * num[1][1]) - (num[1][0] * num[0][1]);

    printf("El determinante es %d: ", deter);

    return 0;
}