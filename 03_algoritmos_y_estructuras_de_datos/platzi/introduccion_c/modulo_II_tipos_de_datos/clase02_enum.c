#include <stdio.h>

enum weekDays {Sunday, Monday, Tuesday, Wendsday, Thursday, Friday, Saturday};

int main() {

    enum weekDays today;
    today = Sunday;

    printf("Day %d", today+1);

    return 0;
}