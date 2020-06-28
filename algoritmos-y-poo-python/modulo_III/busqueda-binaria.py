"""
Tema: Algoritmos de busqueda y ordenamiento - Busqueda Binaria.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.
"""


def main():
    tamano_lista = int(input('Tamano paraobjeto la lista: '))
    objetivo = int(input('Objetivo a encontrar: '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    busqueda_lineal(lista, objetivo)
    print(lista)

    if objetivo in lista:
        print(f'El elemento {objetivo} esta en la lista')
    else:
        print(f'El elemento {objetivo} no esta en la lista')
    
    #print(f'el elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

if __name__ == '__main__':
    main()