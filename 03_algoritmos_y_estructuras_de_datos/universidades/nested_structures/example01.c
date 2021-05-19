/*

Structures Tables!

*/

#include <stdio.h>

#define MAX_STR 128
#define DIM_NOVELAS 4

typedef struct {
    char nombre[MAX_STR];
    char primer_apellido[MAX_STR];
    char segundo_apellido[MAX_STR];
} Escritor;

typedef struct {
    Escritor autor;
    char titulo[MAX_STR];
    int fecha;
} Libro;

int main () {
    Libro novelas[DIM_NOVELAS];

    /* Primer libro */
    printf("Introduce el nombre del autor del primer libro: ");
    fgets(novelas[0].autor.nombre, MAX_STR, stdin);
    printf("Introduce el título del primer libro: ");
    fgets(novelas[0].titulo, MAX_STR, stdin);

    /* Segundo libro */
    printf("Introduce el nombre del autor del segundo libro: ");
    fgets(novelas[1].autor.nombre, MAX_STR, stdin);
    printf("Introduce el título del segundo libro: ");
    fgets(novelas[1].titulo, MAX_STR, stdin);

    /* Tercer libro */
    printf("Introduce el nombre del autor del segundo libro: ");
    fgets(novelas[2].autor.nombre, MAX_STR, stdin);
    printf("Introduce el título del segundo libro: ");
    fgets(novelas[2].titulo, MAX_STR, stdin);

    /* Cuarto libro */
    printf("Introduce el nombre del autor del segundo libro: ");
    fgets(novelas[3].autor.nombre, MAX_STR, stdin);
    printf("Introduce el título del segundo libro: ");
    fgets(novelas[3].titulo, MAX_STR, stdin);

    printf("%s fue escrito por %s.\n", novelas[0].titulo, novelas[0].autor.nombre);
    printf("%s fue escrito por %s.\n", novelas[1].titulo, novelas[1].autor.nombre);
    printf("%s fue escrito por %s.\n", novelas[2].titulo, novelas[2].autor.nombre);
    printf("%s fue escrito por %s.\n", novelas[3].titulo, novelas[3].autor.nombre);

    return 0;
}
