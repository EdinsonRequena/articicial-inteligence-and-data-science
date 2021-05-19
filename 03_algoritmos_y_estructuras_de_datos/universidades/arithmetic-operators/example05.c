#include <stdio.h>

int main() {
    int a=5, b=2;
    double x;
   
    x = (double)a / b;
    printf("%lf\n", x); //Muestra 2.500000
    x = a / b;
    printf("%lf\n", x); //Muestra 2.000000
   
    return 0;
}