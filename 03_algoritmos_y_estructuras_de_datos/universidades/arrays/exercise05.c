/*

Crear un programa que permita a un usuario jugar a hundir la flota de manera simple, el usuario tendra 2 oportunidades. Use matrices.

------------------------------Resuelto por pasos--------------------------------

1) Crear un vector de 2 filas y 3 columnas

2) Inicializar el vector con 2 'O' y el resto de posiciones las colocamos a 'X'
	a) ejemplo de la matriz:
		*)|_X_|_O_|
                  |_O_|_X_|
                  |_X_|_X_|

	b) Como llevarlo a codigo
		*) char mat[3][2]

		*) mat[0][0] = "X"
		*) mat[0][1] = "O"
		
		*) mat[1][0] = "O"
		*) mat[1][1] = "X"

		*) mat[2][0] = "X"
		*) mat[2][1] = "X"

3) Declarar 2 variables que almacenen la fila y la columna ingresada por el usuario (las variables deberian ser inicializadas al principio de la funcion)
	a) llevarlo a codigo
		*) int fila, columna
		*) printf("fila: ")
		*) scanf("%d", &fila)
		*) repetir con columna

	b) Al usuario le pedimos que introduzca un número de fila y columna, 		pero nosotros tenemos que traducirlo al lenguaje de tablas; es decir, 		restarle 1 a las filas y columnas, pues a la primera se accede con [0].
		*) mat[-1][-1]

4) Mostrar el resultado por pantalla!

*/

#include <stdio.h>

int main() {
    int fila, colum;
    char matriz[3][2] = {{'X', 'O'}, {'O', 'X'}, {'X', 'X'}};

    printf("Elige una fila: ");
    scanf("%d", &fila);

    printf("Elige una columna: ");
    scanf("%d", &colum);

    printf("En la fila %d, columna %d, encontramos: %c\n", fila, colum, matriz[fila-1][colum-1]);

    printf("Elige una fila: ");
    scanf("%d", &fila);

    printf("Elige una columna: ");
    scanf("%d", &colum);

    printf("En la fila %d, columna %d, encontramos: %c\n", fila, colum, matriz[fila-1][colum-1]);

    return 0;
}