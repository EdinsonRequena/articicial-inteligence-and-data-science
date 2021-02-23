"""

Tema: Algoritmos de busqueda y ordenamiento - Busqueda Lineal.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

import random

def busqueda_lineal(lista, objetivo):
    '''
    O(n)

    int lista = []
    int objetivo
    match = False

    if objetivo in lista:
        match = True
    return match
    '''

    match = False

    for elemento in lista: # 0(n)
        if elemento == objetivo:
            match = True
            break

    return match


def main():

    tamano_lista = int(input('Tamano de la lista: '))
    objetivo = int(input('Numero a encontrar: '))

    si_encontrado = f"el elemento {objetivo} en la lista"
    no_encontrado = f"el elemento {objetivo} no esta en la lista"

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    busqueda_lineal(lista, objetivo)
    print(lista)

    print(si_encontrado) if objetivo in lista else print(no_encontrado)


if __name__ == '__main__':

    main()
