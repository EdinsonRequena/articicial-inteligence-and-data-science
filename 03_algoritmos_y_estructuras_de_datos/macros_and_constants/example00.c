#include <stdio.h>

#define PIES_POR_CM 0.03

int main() {
    int ancho, largo;
    double ancho_p, largo_p;

    printf ("Introduce el ancho: ");
    scanf ("%d", &ancho);
    ancho_p = ancho * PIES_POR_CM;
   
    printf ("Introduce el largo: ");
    scanf ("%d", &largo);
    largo_p = largo * PIES_POR_CM;

    printf ("%d x %d cm son %.2lf x %.2lf pies.\n", ancho, largo, ancho_p, largo_p);

    return 0;
}