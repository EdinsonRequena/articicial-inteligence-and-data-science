"""

Tema: Complejidad Algoritmica. Notacion asintotica - Recursividad multiple
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

def fibonacci(n):
    '''
    Recursividad multiple
    O(2^n)
    '''

    if n == 0 or n == 1: return 1

    return fibonacci(n-1) + fibonacci(n-2)


def main():

    n = 5
    print(fibonacci(n))


if __name__ == '__main__':

    main()
