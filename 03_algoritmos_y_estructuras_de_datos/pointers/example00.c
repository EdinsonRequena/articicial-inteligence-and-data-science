#include<stdio.h>
int main()

{
	int b = 5;
	int *b_pointer = NULL;

	b_pointer = &b;

	printf("The b value is: %d. \n The *b_pointer values is: %d. \n", b, *b_pointer);
	printf("the b's memory direction is: %p \n", &b);
	printf("the b_pointer's memory direction is: %p \n", b_pointer);

	return 0;
}
