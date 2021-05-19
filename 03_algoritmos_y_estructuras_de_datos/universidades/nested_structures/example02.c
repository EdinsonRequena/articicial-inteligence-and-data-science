#include <stdio.h>

#define MAX_STR 128
#define DIM_NOVELAS 4
#define DIM_AUTORES 3

typedef struct {
    char nombre[MAX_STR];
    char primer_apellido[MAX_STR];
    char segundo_apellido[MAX_STR];
} Escritor;

typedef struct {
    Escritor autores[DIM_AUTORES];
    char titulo[MAX_STR];
    int anyo;
} Libro;

int main () {
    Libro novelas[DIM_NOVELAS];

    /* Primer libro */
    printf("Introduce el nombre del primer autor del primer libro: ");
    fgets(novelas[0].autores[0].nombre, MAX_STR, stdin);
    printf("Introduce el nombre del segundo autor del primer libro: ");
    fgets(novelas[0].autores[1].nombre, MAX_STR, stdin);
    printf("Introduce el título del primer libro: ");
    fgets(novelas[0].titulo, MAX_STR, stdin);

    /* Segundo libro */
    printf("Introduce el nombre del autor del segundo libro: ");
    fgets(novelas[1].autores[0].nombre, MAX_STR, stdin);
    printf("Introduce el título del segundo libro: ");
    fgets(novelas[1].titulo, MAX_STR, stdin);

    printf("%s fue escrito por %s y %s.\n", novelas[0].titulo, novelas[0].autores[0].nombre, novelas[0].autores[1].nombre);
    printf("%s fue escrito por %s.\n", novelas[1].titulo, novelas[1].autores[0].nombre);
   
    return 0;
}