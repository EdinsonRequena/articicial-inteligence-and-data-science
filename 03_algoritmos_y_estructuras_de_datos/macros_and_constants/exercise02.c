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

#define JUPITER 24.55
#define VENUS 8.87
#define URANO 8.887
#define MARTE 3.71
#define TIERRA 9.8
#define SATURNO 10.44
#define NEPTUNO 11.15
#define MERCURIO 3.7

int main() {
    double peso;

    printf("Introduce tu peso: ");
    scanf("%lf", &peso);
   
	printf("Tu peso en la Tierra es %.2lf kg.\n", peso);
	printf("Tu peso en la venus es %.2lf kg.\n", peso*VENUS);
	printf("Tu peso en Marte es %.2lf kg.\n", peso*MARTE);
	printf("Tu peso en Júpiter es %.2lf kg.\n", peso*JUPITER);
	printf("Tu peso en el saturno es %.2lf kg.\n", peso*SATURNO);
	printf("Tu peso en neptuno es %.2lf kg.\n", peso*NEPTUNO);
	printf("Tu peso en mercurio es %.2lf kg.\n", peso*MERCURIO);
    
    return 0;
}