"""

Tema: Manejo de Archivos
Curso: Python intermedio.
Plataforma: Platzi.
Profesor: Facundo García Martoni.
Alumno: @edinsonrequena.

"""


def read():

    numbers = []

    with open('05_python_intermedio/modulo_VI_manejo_de_archivos/archivos/numbers.txt', 'r', encoding='utf-8') as f:
        [numbers.append(int(line)) for line in f]
    print(numbers)


def write():

    names = ['Andrea', 'Angel', 'Vicky', 'Elon']

    with open('05_python_intermedio/modulo_VI_manejo_de_archivos/archivos/names.txt', 'a', encoding='utf-8') as f:
        [f.write(name) and f.write('\n') for name in names]


def main():

    write()


if __name__ == '__main__':

    main()
