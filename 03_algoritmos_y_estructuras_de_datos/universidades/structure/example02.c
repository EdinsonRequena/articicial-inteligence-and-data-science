#include <stdio.h>
#include <string.h>

#define MAX_STR 128

int main() {
    struct {
        char autor[MAX_STR];
        char titulo[MAX_STR];
        int anyo;
    } novela = {"", "El héroe discreto", 2013};
   
    printf("Introduzca el autor de %s, publicado en %d: ", novela.titulo, novela.anyo);
    fgets(novela.autor, MAX_STR, stdin);
   
    printf("%s fue escrito por %s en %d.\n", novela.titulo, novela.autor, novela.anyo);
    
    return 0;
}