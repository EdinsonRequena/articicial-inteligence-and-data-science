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

        try:
            num = int(input('type number: '))
            if len(divisor(num)) == 0:
                raise EOFError('No se pueden ingresar numeros negavtivos')
            print(divisor(num))
            print('The program finally')
        except EOFError as e:
            print(e)
        except ValueError:
            print('Solo puedes ingresar un numero')


if __name__ == '__main__':

    main()
