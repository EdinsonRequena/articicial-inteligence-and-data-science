"""

Tema: Complejidad Algoritmica. Conteo abstracto
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

def f(x):

    respuesta = 0

    for i in range(1000):
        print(i)
        respuesta += 1

    for i in range(x):
        respuesta += x

    for i in range(x):
        for j in range(x):
            print(i)
            print(j)
            respuesta += 1
            respuesta += 1

    return respuesta


def main():

    x = 1000
    f(x)

if __name__ == '__main__':

    main()
