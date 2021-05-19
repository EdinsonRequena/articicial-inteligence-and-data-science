/*

Matriz o tablas bidemensionales

*/

#include <stdio.h>

int main() {
    int num[2][2] = {{3, 9}, {12, 1}};
    int deter;

    deter = (num[0][0] * num[1][1]) - (num[1][0] * num[0][1]);

    printf("El determinante es %d: ", deter);

    return 0;
}