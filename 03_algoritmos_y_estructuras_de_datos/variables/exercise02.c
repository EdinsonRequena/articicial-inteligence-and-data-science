#include <stdio.h>

int main() {
    double total, game1, time1, game2, time2, game3, time3, game4, time4, game5, time5;

    printf("**********Think in te last five game that you buy**********\n");

    printf("Now, how many hour did you play the first game?: \n");
    scanf("%lf", &game1);
    printf("How many dollars did you spend in the first game?: \n");
    scanf("%lf", &time1);

    printf("how many hour did you play the second game?: \n");
    scanf("%lf", &game2);
    printf("How many dollars did you spend in the second game?: \n");
    scanf("%lf", &time2);

    printf("how many hour did you play the third game?: \n");
    scanf("%lf", &game3);
    printf("How many dollars did you spend in the third game?: \n");
    scanf("%lf", &time3);

    printf("how many hour did you play the fourth game?: \n");
    scanf("%lf", &game4);
    printf("How many dollars did you spend in the fourth game?: \n");
    scanf("%lf", &time4);

    printf("how many hour did you play the fifth game?: \n");
    scanf("%lf", &game5);
    printf("How many dollars did you spend in the fifth game?: \n");
    scanf("%lf", &time5);

    total = (game1/time1 + game2/time2 + game3/time3 + game4/time4 + game5/time5) / 5;
    printf("The last five game cost you %lf$ the hour\n", total);
    return 0;
}