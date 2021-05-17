"""
Tema: Algoritmos de busqueda y ordenamiento - Ordenamiento por Inserccion.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.
"""

import random

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

        print(lista)


def main():

    tamano_lista = int(input('Tamano de la lista: '))
    lista = [random.randint(0,100) for i in range(tamano_lista)]

    ordenamiento_por_insercion(lista)


if  __name__ == '__main__':

    main()
