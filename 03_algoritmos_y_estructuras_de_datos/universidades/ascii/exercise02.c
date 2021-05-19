/*

We are going to make a program that allows us to encrypt 
the characters that the user enters, one by one.

*/

#include <stdio.h>

int main() {
    char h, o, m, e, r;
    char l1, l2, l3, l4, l5;

    printf("----------welcome, there!---------\n");

    printf("Type a letter: ");
    scanf("%c", &h);

    printf("Type a letter: ");
    scanf("\n%c", &o);

    printf("Type a letter: ");
    scanf("\n%c", &m);

    printf("Type a letter: ");
    scanf("\n%c", &e);

    printf("Type a letter: ");
    scanf("\n%c", &r);

    l1 = h + 3;
    l2 = o + 3;
    l3 = m + 3;
    l4 = e + 3;
    l5 = r + 3;

    printf("The original word is: %c%c%c%c%c\n", h, o , m, e, r);
    printf("The cipher word is: %c%c%c%c%c\n", l1, l2 , l3, l4, l5);

    return 0;
}