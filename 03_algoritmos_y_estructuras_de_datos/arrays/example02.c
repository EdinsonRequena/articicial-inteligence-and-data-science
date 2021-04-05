#include <stdio.h>

#define TABLE 3

int main() {
    int datos_a[TABLE] = {8,7,9};   // 3 elementos
    int datos_b[] = {8,7,9};      // 3 elementos
    int datos_c[TABLE+2] = {8,7,9}; // 5 elementos
    int datos_d[TABLE+22] = {0};    // 25 elementos

    return 0;
}