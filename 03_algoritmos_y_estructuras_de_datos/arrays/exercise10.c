/*

Escribir un programa que pida una palabra y después un número inferior al tamaño de dicha palabra. El programa introducirá el valor ASCII 0 en la posición indicada por el usuario y mostrará la cadena resultante, el programa tambien imprimira la longitud de la palabra completa y luego de la palabra recortada.

----------------------------resuelto por pasos----------------------------------

1) Definir una constante con la longitud del string (opcional)

2) Declarar una variable que alamacene enteros en la cual le pasaremos por valor la longitud que indicara el usuario

3) Crear un vector de tipo char especificando su longitud
	a) ejemplo de codigo:
		*) char vector[10]

4) pedir al usuario que escriba una palabra, almacenarlo en el vector anteriormente creado e imprimir la longitud de la misma.
	a) ejemplo de codigo:
		*) char vector[10]
		*) printf("Escriba: ")
		*) scanf('%s', vector) NO utilizar el símbolo ampersand(&)
		*) printf("Longitud: %d", strlen(vector))

5) Pedir al usuario la longitud en la que quiera recortar la palabra anteriormente ingresada e ingresar ese valor en la variable int anteriormente creada.
	a) ejemplo de codigo:
		*) int var
		*) printf("recorte la palabra: ")
		*) scanf('%d', &var) SI utilizar el símbolo ampersand(&)

6) Recortar la logintud de la palabra, mostar por pantalla la palabra recortada y su nueva longitud. El valor entero que ha ingresado el usuario se tiene que igual al codigo ASCII 0
	a) ejemplo de codigo:
    		*) vector[var-1] = 0;
   		*) printf("La palabra recortada es: %s\n", vector);
   		*) printf("Nueva longitud: %d", var);

*/

#include <stdio.h>
#include <string.h>

int main() {
    int var;
    char vector[10];

    printf("Escriba una palabra: ");
    scanf("%s", vector);
    printf("Longitud de la palabra: %d\n", strlen(vector));

    printf("Recorte la palabra con un entero: ");
    scanf("%d", &var);

    vector[var-1] = 0;
    printf("La palabra recortada es: %s\n", vector);
    printf("Nueva longitud: %d", var);


    return 0;
}