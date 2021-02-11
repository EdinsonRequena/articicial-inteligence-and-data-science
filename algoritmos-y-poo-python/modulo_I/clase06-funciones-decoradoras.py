"""

Tema: Programacion Orientada a Objetos. Funciones decoradoras.
Curso: Curso de python, video 74.
Plataforma: Youtube.
Profesor: Juan diaz - Pildoras informaticas.
Alumno: @edinsonrequena.

"""

def funcion_decoradora(funcion_como_parametro):

    def funcion_interior(*args, **kwargs):

        print('Codigo que se ejecutara antes de llamar a la funcion a decorar')

        funcion_como_parametro(*args, **kwargs)

        print('Codigo que se ejecutara despues de llamar a la funcion a decorar')

    return funcion_interior


@funcion_decoradora
def suma(num1, num2, num3): print(num1+num2+num3)


def resta(num1, num2): print(num1-num2)


@funcion_decoradora
def division(num1, num2): print(num1/num2)


@funcion_decoradora
def potencia(base, exponente): print(pow(base,exponente))

if __name__ == '__main__':
    suma(5,10,16)
    resta(8,6)
    potencia(base=5, exponente=10)
    division(5,7)