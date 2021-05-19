#include <stdio.h>

int main() {
    char sex;
    int age;
    float weight;
    double height;
    int children;

    printf("---------- Welcome there! -------- \n");

    printf("What is your sex?: ");
    scanf("%c", &sex);

    printf("What is your age?: ");
    scanf("%d", &age);

    printf("What is your weight?: ");
    scanf("%f", &weight);

    printf("What is your height?: ");
    scanf("%lf", &height);

    printf("How many children do you have?: ");
    scanf("%d", &children);

    return 0;
}