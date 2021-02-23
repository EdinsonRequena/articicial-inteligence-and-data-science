"""

Tema: Complejidad Algoritmica. Notacion asintotica - Ley de la multiplicacion.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

def f(n):
    '''
    Ley de la multiplicacion.
    O(n) * O(n) = O (n * n) = O(n^2)
    '''

    for i in range(n):
        for j in range(n):
            print(i, j)


def main():

    n = 20
    f(n)


if __name__ == '__main__':

    main()
