/*

We are going to make a program that allows us to encrypt 
the characters that the user enters, one by one.

*/

#include <stdio.h>

int main() {
    char c1, c2, c3, c4, c5;

    printf("Type a character: ");
    scanf("%c", &c1);

    printf("Type a second character: ");
    scanf("\n%c", &c2);

    printf("Type a third character: ");
    scanf("\n%c", &c3);

    printf("Type another character: ");
    scanf("\n%c", &c4);

    printf("Type the last character: ");
    scanf("\n%c", &c5);

    printf("The original word is: %c%c%c%c%c\n", c1, c2, c3, c4, c5);
    printf("The cipher word is: %c%c%c%c%c\n", c1+3, c2+3, c3+3, c4+3, c5+3);

    return 0;
}
