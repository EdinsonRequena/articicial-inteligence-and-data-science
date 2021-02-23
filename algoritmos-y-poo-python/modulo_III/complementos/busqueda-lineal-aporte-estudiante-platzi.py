"""

Tema: Algoritmos de busqueda y ordenamiento - Busqueda Lineal.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.

Aporte de varios estudiantes de platzi

EXPLICACIION: Es bastante más limpio el código como lo estas planteando pero la
complejidad algoritmica seria la misma ya que internmente python aplica la función
iter() al objeto iterable “lista” para obtener cada elemento y la compara con la
variable “objetivo” para devolver un false o un true.
.
Eso quiere decir que aplicariamos la mismas iteraciones a lo largo del tiempo, un O(n)
en Big oh notation. iteraciones definidas por el tamaño del objeto iterable y recuerda
que para definir la complejidad de un algoritmo tomamos el peor de los casos es decir
cuando se recorre el objeto iterable por completo.
.
En la documentacion de python, en la direccion que comparte @danielfernando, lo dice
directamente. Las expresiones con la forma < X in S > tienen una complejidad O(n)
"""

import random

def busqueda_lineal(lista, objetivo): return objetivo in lista # O(n)


def main():

    tamano_lista = int(input('Tamano de la lista: '))
    objetivo = int(input('Numero a encontrar: '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)

    print(f'el elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

if __name__ == '__main__':

    main()
