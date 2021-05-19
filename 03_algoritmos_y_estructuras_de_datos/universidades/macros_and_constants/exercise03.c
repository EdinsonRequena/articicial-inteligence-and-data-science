/*

Write a program that calculates the user's weight on other planets.

For example:

Enter your weight: 71.5
Your weight on Jupiter is: 179.114796 kg.
Your weight on the moon is: 11.83 kg.
Your weight on Mars is: 27.85 kg.
Your weight on Jupiter is: 188.76 kg.
Your weight on Saturn: is 92.95 kg.
Your weight in Neptune is: 57.20 kg.
Your weight in Mercury is: 100.10 kg.

*/

#include <stdio.h>

int main() {
    double peso_final, peso_tierra;
    const double JUPITER = 24.55, VENUS = 8.87, URANO = 8.887, MARTE = 3.71, TIERRA = 9.8, SATURNO = 10.44, NEPTUNO = 11.15, MERCURIO = 3.7;

    printf("--------Know your weight in another planets-------\n");

    printf("What's your weight on earth?: \n");
    scanf("%lf", &peso_tierra);

    peso_final = (peso_tierra * JUPITER) / TIERRA;
    printf("Your weight in jupiter is:%lf\n", peso_final);

    peso_final = (peso_tierra * VENUS) / TIERRA;
    printf("Your weight in venus is:%lf\n", peso_final);

    peso_final = (peso_tierra * URANO) / TIERRA;
    printf("Your weight in urano is:%lf\n", peso_final);

    peso_final = (peso_tierra * MARTE) / TIERRA;
    printf("Your weight in mars is:%lf\n", peso_final);

    peso_final = (peso_tierra * MERCURIO) / TIERRA;
    printf("Your weight in mercury is:%lf\n", peso_final);

    peso_final = (peso_tierra * SATURNO) / TIERRA;
    printf("Your weight in saturn is:%lf\n", peso_final);

    peso_final = (peso_tierra * NEPTUNO) / TIERRA;
    printf("Your weight in neptune is:%lf\n", peso_final);

    return 0;
}