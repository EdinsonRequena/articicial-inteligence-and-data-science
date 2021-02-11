"""

Tema: Programacion Orientada a Objetos. Funciones decoradoras.
Curso: Curso de python, video 73.
Plataforma: Youtube.
Profesor: Juan diaz - Pildoras informaticas.
Alumno: @edinsonrequena.

"""

def funcion_decoradora(funcion_como_parametro):

    def funcion_interior():

        print('Codigo que se ejecutara antes de llamar a la funcion a decorar')

        funcion_como_parametro()

        print('Codigo que se ejecutara despues de llamar a la funcion a decorar')

    return funcion_interior


@funcion_decoradora
def suma(): print(15+20)


def resta(): print(5-10)


@funcion_decoradora
def division(): print(8/3)

if __name__ == '__main__':
    suma()
    resta()
    division()