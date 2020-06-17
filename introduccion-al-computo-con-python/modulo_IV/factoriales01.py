"""

Ejercicio: Crear un programa en el que el se modifique el limite de recursion.
Curso: Pensamiento Computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

# Importamos el modulo sys que nos permitira modificar la recursion
import sys

def factorial(n):
    """Calcula el factorial de n

        n int > 0
        returns n!
    """
    print(n)
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

if __name__ == "__main__":

    n = int(input('Escribe un entero: '))

    # Imprimimos el limite de recursion que trae python por defecto con la funcion sys.getrecursionlimit() que trae el modulo sys. 
    print(sys.getrecursionlimit())

    # Modificamos el limite de recursion a 2000 con la funcion sys.setrecursionlimit() que trae el modulo sys
    sys.setrecursionlimit(2000)

    print(factorial(n))