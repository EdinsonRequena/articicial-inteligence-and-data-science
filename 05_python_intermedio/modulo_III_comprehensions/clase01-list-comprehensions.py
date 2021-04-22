"""

Tema: List Comprehensions
Curso: Python intermedio.
Plataforma: Platzi.
Profesor: Facundo García Martoni.
Alumno: @edinsonrequena.

"""


def normal_lists():

    square = []

    for i in range(1, 101):
        if i % 3 != 0:
            square.append(i**2)


def comprehensions_lists():

    square = [i for i in range(1,101) if i % 3 != 0]


def main():

    normal_lists()
    comprehensions_lists()


if __name__ == '__main__':

    main()
