#include <stdio.h>

int main() {
    char mander = '4';
    char meleon = 53;
    char izard = mander + 2; 
  
    printf("%c %c %c\n", mander, meleon, izard);
    printf("%d %d %d\n", mander, meleon, izard);
    printf("%c %d %c\n", mander, meleon, izard);
  
    return 0;
}