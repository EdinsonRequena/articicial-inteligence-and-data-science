"""
Tema: Programacion dinamica - Secuencia de Fibonacci.
Curso: Programacion Dinamica y Estocastica.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.
"""

import sys

# Fibonacci poco eficiente
def fibonacci_recursivo(n):

    # Caso Base
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Fibonacci mas eficiente
def fibonacci_dinamico(n, memo = {}):

    # Caso Base
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado

        return resultado


def main():
    sys.setrecursionlimit(10002)
    n = int(input('Escoge un numero: '))
    resultado = fibonacci_dinamico(n)
    print(resultado)

if __name__ == '__main__':
    main()