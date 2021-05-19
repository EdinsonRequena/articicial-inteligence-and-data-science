#include <stdio.h>

int main() {
    double dollars, euros;

    dollars = 100;
    euros = dollars * 0.92;

    printf("%lf dollars are %lf euros.\n", dollars, euros);

    return 0;
}