"""

Tema: Algoritmo de ordenamiento por insercion
Alumno: @edinsonrequena.

"""

import random


def ordenamiento_por_insercion(lista):
    """
    0) lista = [5, 2, 9, 3, 4]
    1) El primer bucle itera por todos los elementos de la lista empezando desde lista[1] (primer indice)
        en esta caso lista[1] = 2
    2) actual tomara el valor del numero en el que se este iterando en ese momento. ejemplo: si lista[i] = 2, entonces, actual = 2
    3) j sera igual al indice actual restandole una pocision. Lo que quiere decir que estara a la izquierda del indice actual,
        ejemplo: si i = 1, entonces, j = 0

    4) El segundo bucle se ejecutara si o solo si j es mayor o igual a 0
    5) si actual es mayor que lista[i+1], entonces se copiara ese elemento en lista[j]
        en nuestro ejemplo esta primera iteracion las lista quedaria: [5, 5, 9, 3, 4] en este punto.
    6) luego se reemplazara el elmento en lista[j] (que en la primera iteracion es 5)
        por el valor de la variable actual (que en la primera iteracion es 2)
    7) Se le restara 1 a j por cada vez que se ejecute el bucle while para evitar caer en un bucle infinito
    8) Siguiendo nuestro ejemplo en la primera iteracion la lista quedaria: [2, 5, 9, 3, 4]
    9) Este proceso se repetira hasta que la lista quede completamente ordenada

    Complejidad Algoritmica = O(n + len(lista)) * O(n) = O(n) * O(n) = O(n*n) = O(n^²)

    """

    print(lista)

    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1

        while j >= 0:
            if actual < lista[j]:
                lista[j+1] = lista[j]
                lista[j] = actual
                j -= 1
                print(f'la lista va asi: {lista}')
            else:
                break

    return lista



def main():

    tamano_lista = int(input('Tamano de la lista: '))
    lista = [random.randint(0,100) for i in range(tamano_lista)]

    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)


if  __name__ == '__main__':

    main()
