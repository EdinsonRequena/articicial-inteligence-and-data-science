#include <stdio.h>

#define MULT(A, B) A*B

int main() {
    printf("MULT(5,5): %d\n", MULT(5,5));
    printf("MULT(2+3,3+2): %d\n", MULT(2+3,3+2));
    return 0;
}