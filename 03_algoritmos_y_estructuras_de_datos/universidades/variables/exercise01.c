#include <stdio.h>

int main() {
    double temporadas, capitulos, duracion, intro, total;

    printf("Piensa en una serie que hayas visto...\n"); 
    printf("¿Cuántas temporadas tiene? "); 
    scanf("%lf", &temporadas); 
    printf("¿Cuántos capítulos de media cada temporada? "); 
    scanf("%lf", &capitulos); 
    printf("¿Cuántos minutos duran aproximadamente los capítulos? "); 
    scanf("%lf", &duracion); 
    printf("¿Y su intro? "); 
    scanf("%lf", &intro); 
    
    total = temporadas*capitulos*(duracion - intro) / 60; 
    printf("¡En total has invertido unas %.2lf horas en ver la serie!\n", total); 
    
    return 0; 
}
