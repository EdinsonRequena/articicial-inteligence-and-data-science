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

    printf("Tamaño variable sexo: %d\n", sizeof(sexo));
    printf("Tamaño variable CP: %d\n", sizeof(cp));
    printf("Tamaño variable HP: %d\n", sizeof(hp));
    printf("Tamaño variable peso: %d\n", sizeof(peso));
    printf("Tamaño variable altura: %d\n", sizeof(altura));
    printf("Tamaño variable caramelos: %d\n", sizeof(caramelos));

    return 0;
}