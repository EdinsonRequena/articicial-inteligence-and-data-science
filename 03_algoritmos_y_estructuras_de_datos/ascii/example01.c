#include <stdio.h>

int main() {
    char c1, c2;

    printf("Type a letter: ");
    scanf("%c", &c1);
    printf("Type a letter: ");
    scanf("\n%c", &c2);

    printf("You has been type the letters %d y %d\n", c1, c2);
    return 0;
}