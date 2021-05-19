#include <stdio.h>

int main() {
    double euros, dollars;

    printf("Enter the dollar amount: ");
    scanf("%lf", &dollars);

    euros = dollars * 0.92;
    printf("%lf dollars are %lf euros.\n", dollars, euros);

    return 0;
}