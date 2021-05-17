"""

Tema: Algoritmo de ordenamiento burbubuja
Alumno: @edinsonrequena.

"""

import random

def ordenamiento_burbuja(lista):
    '''
    O(n) * O(n - i - 1) = O(n) * O(n) = O(n * n) = O(n^²)

    int n = []
    int n = len(n)
    return n
    '''
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)

    return lista


def main():

    tamano_lista = int(input('Tamano para lista la lista: '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)

if __name__ == '__main__':

    main()
