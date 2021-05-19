#include <stdio.h>

int main() {
    char h = 'h', e = 'e', l = 'l', l2 = 'l', o = 'o';
    char we1, we2, we3, we4, we5;

    we1 = h + 3;
    we2 = e + 3;
    we3 = l + 3;
    we4 = l + 3;
    we5 = o + 3;
    
    printf("The original word is: %c%c%c%c%c\n", h, e , l, l2, o);
    printf("The cipher word is: %c%c%c%c%c\n", we1, we2 , we3, we4, we5);

    return 0;
}