"""

Tema: Complejidad Algoritmica.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

import time

def factorial(n):

    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)


def main():

    n = 200000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)


if __name__ == '__main__':

    main()
