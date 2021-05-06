"""

Tema: Resolviendo reto.
Curso: Python intermedio.
Plataforma: Platzi.
Profesor: Facundo García Martoni.
Alumno: @edinsonrequena.

"""

def divisor(num):

    divisor_list = []

    try:
        if type(num) != int :
            raise ValueError('Solo ingresar numeros')
        for i in range(1, num + 1):
            if num % i == 0:
                divisor_list.append(i)
        return divisor_list
    except ValueError as ve:
        print(ve)


def main():

    num = int(input('type number: '))
    print(divisor(num))
    print('The program finally')


if __name__ == '__main__':

    main()