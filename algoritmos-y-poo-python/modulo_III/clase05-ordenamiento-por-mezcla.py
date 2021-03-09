"""

Tema: Algoritmos de busqueda y ordenamiento - Ordenamiento por Mezcla.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

import random

def ordenamiento_por_mezcla(lista):

    # Caso base
    if len(lista) > 1:
        medio = len(lista) // 2 # Parte la lista a la mitad
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        # Llamada recursiva a cada mitad
        ordenamiento_por_mezcla(izquierda) # Llamada de [:mitad]
        ordenamiento_por_mezcla(derecha) # Llamada de [mitad:]

        # Iteradores para recorrer las dos sublistas
        i, j = 0, 0

        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha): # Comparar las dos sublistas
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
