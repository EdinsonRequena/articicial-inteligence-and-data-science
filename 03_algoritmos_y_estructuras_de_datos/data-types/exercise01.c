#include <stdio.h>

int main() {
    char sexo;
    int cp, hp, caramelos;
    double peso, altura;

    printf("Introduce el sexo (M/F): ");
    scanf("%c", &sexo);

    printf("Introduce los puntos de combate: ");
    scanf("%d", &cp);

    printf("Introduce los puntos de salud: ");
    scanf("%d", &hp);

    printf("Introduce el peso: ");
    scanf("%lf", &peso);

    printf("Introduce la altura: ");
    scanf("%lf", &altura);
    
    printf("Introduce el número de caramelos: ");
    scanf("%d", &caramelos);

    printf("Sexo: %c\n", sexo);
    printf("CP: %d\n", cp);
    printf("HP: %d\n", hp);
    printf("Peso: %.1lf\n", peso);
    printf("Altura: %.2lf\n", altura);
    printf("Caramelos: %d\n", caramelos);

    return 0;
}