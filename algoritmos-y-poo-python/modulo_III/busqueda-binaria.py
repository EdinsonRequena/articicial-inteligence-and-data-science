"""
Tema: Algoritmos de busqueda y ordenamiento - Busqueda Binaria.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.
"""
import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')

    if comienzo > final:
        return False
    
    mitad = (comienzo + final) // 2

    if lista[mitad] == objetivo:
        return True
    elif lista[mitad] < objetivo:
        return busqueda_binaria(lista, mitad + 1, final, objetivo)
    elif lista[mitad] > objetivo:
        return busqueda_binaria(lista, comienzo, mitad - 1, objetivo)


def main():
    tamano_lista = int(input('Tamano paraobjeto la lista: '))
    objetivo = int(input('Objetivo a encontrar: '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

    busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)

    if objetivo in lista:
        print(f'El elemento {objetivo} esta en la lista')
    else:
        print(f'El elemento {objetivo} no esta en la lista')
    
    #print(f'el elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

if __name__ == '__main__':
    main()