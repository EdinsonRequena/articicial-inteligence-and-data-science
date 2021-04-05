/*

Escriba un programa que calcule la media de puntos obtenidos en las últimas 5 partidas de tu videojuego favorito 
con 3 de tus jugadores favoritos. Usando vectores

-------------------------------------Problema resuelto por pasos------------------------------------------------

1) declarar 3 constantes con el nombre de los jugadores y un         
valor de 5

2) inicializar 3 vectores que contengan 5 elementos cada uno

3) los 5 elementos seran la experiencia obtenido en las ulitimas
5 partidas

4) sacar el promedio de todas esas partidas

	a) Como sacar un promedio?
		*) sumar todos los valores
		*) dividir la suma de esos valores entre la cantidad
		   de valores
		*) es decir, si son 5 valores se suman esos 5 valores
		   y se divide entre el numero de esos valores (es decir 5)

6) formula para sacar el promedio en el codigo
	a) declarar 3 variables que almacenen el resultado de las
	   ecuaciones
	b) como hacer que las variables anteriores almacenen el resultado?
		*) sumar todos los indices del vector
		*) dividir esa suma entre el numero de indices (en este caso
		    en especifico sera 5)
		*) recordar la jerarquia de operaciones
		*) ejemplo: op = (vec[0] + vec[1]) / 2

7) imprimir el valor de todas las variables que almacenen el resultado de la ecuacion por pantalla!

---------------------------------------------------------------------------------------------------

*/

#include <stdio.h>

#define PLAYER1 5
#define PLAYER2 5
#define PLAYER3 5

int main() {
    float vector1[PLAYER1] = {123.77, 88.9, 110.05, 70, 45.01};
    float operacion1 = (vector1[0] + vector1[1] + vector1[2] + vector1[3] + vector1[4]) / 5;

    float vector2[PLAYER2] = {88.77, 95.9, 265.05, 100, 200.01};
    float operacion2 = (vector2[0] + vector2[1] + vector2[2] + vector2[3] + vector2[4]) / 5;

    float vector3[PLAYER3] = {200.77, 255.9, 10.05, 8, 300.01};
    float operacion3 = (vector3[0] + vector3[1] + vector3[2] + vector3[3] + vector3[4]) / 5;

    printf("Your average wiht player1 is: %f\n", operacion1);
    printf("Your average wiht player2 is: %f\n", operacion2);
    printf("Your average wiht player3 is: %f\n", operacion3);

    return 0;
}
