"""

Tema: Algoritmo de busqueda binaria iterativa
Alumno: @edinsonrequena.

"""

import random

def busqueda_binaria_iterativa(lista, comienzo, final, objetivo):

    while final > comienzo:
        mitad = (comienzo + final) // 2 # comiezo = 0: final = len(lista), so: mitad = (0 + len(lista)) // 2

        print(f'El numero de la mitad es: {mitad}')
        print(f'El indice de la mitad es: {lista[mitad]}')

        # if lista[mitad] == objetivo: return True # Esta linea no se 100% necesaria
        if lista[mitad] < objetivo: comienzo = mitad - 1
        elif lista[mitad] > objetivo: comienzo = mitad + 1


def main():

    tamano_lista = int(input('Tamano para la lista: '))
    objetivo = int(input('Objetivo a encontrar: '))

    si_encontrado = f"el elemento {objetivo} en la lista"
    no_encontrado = f"el elemento {objetivo} no esta en la lista"

    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

    busqueda_binaria_iterativa(lista, 0, len(lista), objetivo)
    print(lista)

    print(si_encontrado) if objetivo in lista else print(no_encontrado)

if __name__ == '__main__':

    main()