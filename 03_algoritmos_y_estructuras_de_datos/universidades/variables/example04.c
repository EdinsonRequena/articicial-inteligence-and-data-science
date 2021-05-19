#include <stdio.h>

int main() {
    double euros = 0.92, dollars;

    printf("Enter the dollar amount: ");
    scanf("%lf", &dollars);

    euros = dollars * euros;
    printf("%lf dollars are %lf euros.\n", dollars, euros);

    return 0;
}