#include <stdio.h>

int main() {
    double tiempo1, tiempo2, tiempo3, tiempo4, tiempo5;
    double precio1, precio2, precio3, precio4, precio5;
    double total;

    printf("Piensa en los últimos cinco juegos que has jugado.\n"); 
    printf("¿Cuántas horas le has echado al primero de ellos? "); 
    scanf("%lf", &tiempo1); 
    printf("¿Y cuánto te costó? "); 
    scanf("%lf", &precio1); 
    printf("¿Cuántas horas le has echado al segundo? "); 
    scanf("%lf", &tiempo2); 
    printf("¿Y cuánto te costó? "); 
    scanf("%lf", &precio2); 
    printf("¿Cuántas horas le has echado al tercero? "); 
    scanf("%lf", &tiempo3); 
    printf("¿Y cuánto te costó? "); 
    scanf("%lf", &precio3); 
    printf("¿Cuántas horas le has echado al cuarto? "); 
    scanf("%lf", &tiempo4); 
    printf("¿Y cuánto te costó? "); 
    scanf("%lf", &precio4); 
    printf("¿Cuántas horas le has echado al quinto? "); 
    scanf("%lf", &tiempo5); 
    printf("¿Y cuánto te costó? "); 
    scanf("%lf", &precio5); 
    
    total = (precio1/tiempo1 + precio2/tiempo2 + precio3/tiempo3 + precio4/tiempo4 + precio5/tiempo5) / 5; 
    printf("¡Los últimos 5 juegos te han salido a %lf euros la hora!\n", total); 
    
    return 0; 
}