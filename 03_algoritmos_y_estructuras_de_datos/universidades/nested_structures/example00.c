/*

nested structures

*/

#include <stdio.h>

#define MAX_STR 128

typedef struct {
    char nombre[MAX_STR];
    char primer_apellido[MAX_STR];
    char segundo_apellido[MAX_STR];
} Escritor;

typedef struct {
    Escritor autor;
    char titulo[MAX_STR];
    int anyo;
} Libro;

int main() {
    Libro novela;

    printf("Introduce el nombre del autor: ");
    fgets(novela.autor.nombre, MAX_STR, stdin);
    printf("Introduce el primer apellido del autor: ");
    fgets(novela.autor.primer_apellido, MAX_STR, stdin);
    printf("Introduce el segundo apellido del autor: ");
    fgets(novela.autor.segundo_apellido, MAX_STR, stdin);
  
    printf("Introduce el título del libro: ");
    fgets(novela.titulo, MAX_STR, stdin);
    printf("Introduce el año de publicación del libro: ");
    scanf("%d", &novela.anyo, MAX_STR, stdin);

    printf("%s fue escrito en %d por %s %s %s.\n", novela.titulo, novela.anyo, novela.autor.nombre, novela.autor.primer_apellido, novela.autor.segundo_apellido);
  
    return 0;
}