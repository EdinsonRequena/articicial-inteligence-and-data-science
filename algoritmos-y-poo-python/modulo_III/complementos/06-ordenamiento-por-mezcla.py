"""

Tema: Algoritmos de busqueda y ordenamiento - Ordenamiento por Mezcla.
Alumno: @edinsonrequena.

"""

import random

def ordenamiento_por_mezcla(lista):
    """
    ---------------------------------------Dividir-------------------------------------------------------
    0) Caso de ejemplo. lista = [4,2,44,20,12,8]
    1) En el caso base verificamos que la lista aun se pueda dividir
    2) Si aun la lista es divisible entre 2 la volvemos a dividir. Las listas quedarian: [4,2,44], [20,12,8]
    3) Almacenamos en la variable izquierda la mitad de la lista que va desde el indice 0 hasta el indice de la mitad.
        quedando de la siguiente manera: izquierda = [4,2,44]
    4)Almacenamos en la variable derecha la mitad de la lista que va desde el primer indice de la otra mitad hasta el indice final.
        quedando de la siguiente manera: derecha = [20,12,8]
    5) Llamamos la funcion recursivamente pasandole como parametro las sub-listas hasta que la logitud de estas sea 1.

    -------------------------------------------------Ordenar---------------------------------------------------------------
    0) Una vez ya tengamos todas las listas con un solo elemento, es hora de ordenarlas por mezcla
    1) Creamos 2 iteradores para recorrer las sub-listas
    2) Creamos un iterador para recorrer la lista principal
    3) El primer bucle se ejecuta si y solo si i es mayor a len(izquierda) y j es mayor a len(derecha)
        por ejemplo: i, j = 0, len(izquieda), len(derecha) = 3, entonces la condicion para que se ejecute el bucle sera cierta.

    4) Dentro de este primer bucle verificamos si izquierda[i] (que en la primera iteracion seria = izquierda[0] = 4) es menor que
        derecha[j] (que en la primera interacion seria = derecha[0] = 20), si este condicional es cierto ponemos en lista[k]
        (lista[0] en la primera iteracion) lo que hay en izquierda[i] (izquierda[0]=4 en la primera iteracion).
        Siguiendo nuestro caso de ejemplo esta condicion seria cierta, por lo que en lista[k] (lista[0] en primera interacion)
        se agregaria lo que hay en izquierda[i], quedando la lista original de la siguiente forma en esta primera iteracion:
        lista[k] = lista[0] = 4

    5) Incrimentamos i para no caer en un bucle infinito e iterar en la siguiente poscision de la sub-lista correspondiente en la
        proxima iteracion.

    6) verificamos si derecha[j] (que en la primera iteracion seria = derecha[0] = 20) es menor que
        izquierda[i] (que en la primera interacion seria = izquierda[0] = 4), si este condicional es cierto ponemos en lista[k]
        (lista[0] en la primera iteracion) lo que hay en derecha[j] (derecha[0]=20 en la primera iteracion).
        Siguiendo nuestro caso de ejemplo esta condicion seria falsa en la primera iteracion.
        Esto quiere decir que j quedaria valiendo 0 y en la siguiente iteracion derecha[j] = derecha[0] = 20.

    7) Incrimentamos k para no caer en un bucle infinito y trabajar en el indice siguiente de lista[k] que seria,
        lista[1] en la siguiente iteracion

    8)
    """

    # Caso base
    if len(lista) > 1:
        medio = len(lista) // 2 # Parte la lista a la mitad
        izquierda = lista[:medio] # De 0 hasta la mitad
        derecha = lista[medio:] # Desde la mitad hasta el final
        print(f'lista: {lista}')
        print(f'Izquierda: {izquierda}')
        print(f'Derecha: {derecha}')
        print(f'mitad: {medio}')

        # Llamada recursiva a cada mitad
        ordenamiento_por_mezcla(izquierda) # Llamada de [:mitad]
        ordenamiento_por_mezcla(derecha) # Llamada de [mitad:]

        # Iteradores para recorrer las dos sublistas
        i, j = 0, 0

        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            elif derecha[j] < izquierda[i]:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista

def main():
    '''
    Funcion principal
    '''

    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)

if __name__ == '__main__':

    main()
