"""

Tema: Resolviendo reto.
Curso: Python intermedio.
Plataforma: Platzi.
Profesor: Facundo García Martoni.
Alumno: @edinsonrequena.

"""


def divisor(num):

    divisor_list = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisor_list.append(i)

    return divisor_list


def main():

    num = input('Ingrese un numero: ')
    print(divisor(int(num))) if num.isnumeric() else print('ingrese solo numeros')


if __name__ == '__main__':

    main()
