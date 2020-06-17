"""

Tema: Recursividad y secuencia de Fibonacci.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

def fibonacci(n):
    """Calcula el la secuencia de fibonacci de n

        n int > 1
        returns (n - 1) + (n -2)
    """
    print(n)
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    n = int(input('Escriba un entero: '))

    print(fibonacci(n))