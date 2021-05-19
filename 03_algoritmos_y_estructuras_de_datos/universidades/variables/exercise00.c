#include <stdio.h>

int main() {
    double total, seasons, number_chap, duration_chap;

    printf("**********Think in a serie**************\n");

    printf("Now, how much seasons have?: \n");
    scanf("%lf", &seasons);

    printf("How much chapter have?: \n");
    scanf("%lf", &number_chap);

    printf("How much minuts chapters have?: \n");
    scanf("%lf", &duration_chap);

    total = seasons * number_chap * duration_chap / 60;
    printf("You has been %lf hours look the serie\n", total);

    return 0;
}