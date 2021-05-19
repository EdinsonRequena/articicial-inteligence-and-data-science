/*

Escriba un programa que calcule la media de puntos obtenidos en las últimas 5 partidas de tu videojuego favorito 
con 3 de tus jugadores favoritos. Usando matrices

------------------------------------- Problema resuelto por pasos ---------------------------------------------------

1) Declarar e inicializar una matriz de 3 filas y 5 elementos
	a) como hacerlo en codigo?
		*) float matriz[3][5]

2) cada fila representara a cada uno de los 3 jugadores donde cada elemento respresentara a los puntajes obtenidos 
en las ultimas 5 partidas

3) sacar el promedio de los elementos de la matriz
	a) como sacar un promedio?
		*) sumar todos los valores
		*) dividir la suma de los valores entre el numero de valores
		*) ejem: 
			n + n + n = n3
				n3 / 3 = promedio de n3

	b) Como pasar la ecuacion en codigo
		*) float mat[2][3] .....
		*) op1 = (mat[0][0] + mat[0][1] + mat[0][2]) / 3
		*) op2 = (mat[1][0] + mat[1][1] + mat[1][2]) / 3

4) Imprima el resultado de las ecuaciones por pantalla!

*/

#include <stdio.h>

int main() {
    float matriz[3][5];

    matriz[0][0] = 200.0;
    matriz[0][1] = 67.05;
    matriz[0][2] = 145.60;
    matriz[0][3] = 100.45;
    matriz[0][4] = 88.50;

    matriz[1][0] = 300.0;
    matriz[1][1] = 799.05;
    matriz[1][2] = 10.60;
    matriz[1][3] = 5.45;
    matriz[1][4] = 8.50;

    matriz[2][0] = 55.0;
    matriz[2][1] = 345.05;
    matriz[2][2] = 148.60;
    matriz[2][3] = 110.45;
    matriz[2][4] = 88.50;

    float op1 = (matriz[0][0] + matriz[0][1] + matriz[0][2] + matriz[0][3] + matriz[0][4]) / 5;
    float op2 = (matriz[1][0] + matriz[1][1] + matriz[1][2] + matriz[1][3] + matriz[1][4]) / 5;
    float op3 = (matriz[2][0] + matriz[2][1] + matriz[2][2] + matriz[2][3] + matriz[2][4]) / 5;

    printf("Your average wiht player1 is: %f\n", op1);
    printf("Your average wiht player2 is: %f\n", op2);
    printf("Your average wiht player3 is: %f\n", op3);

    return 0;
}