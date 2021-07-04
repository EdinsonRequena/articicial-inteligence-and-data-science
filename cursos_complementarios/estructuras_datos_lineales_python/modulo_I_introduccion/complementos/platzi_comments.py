# Funcion de listas
def func_list() -> list:

    """
    1) Son de proposito general
    2) Es la estructura mas utilizada
    3) Tama;o dinamico
    4) De tipo secuencial
    5) Ordenable
    """

    list1 = list()
    list2 = [False, any, 'Hola', 5, 3.45]
    list3 = [n**2 for n in range(1, 100) if n % 2 == 0]

    print(list1)
    print(list2)
    print(list3)

    return list1, list2, list3


# Funcion de tublas
def func_tuples() -> tuple:

    """
    1) Inmutable (no se pueden agregar o cambiar).
    2) Utiles para datos constantes.
    3) Mas rapidas que las listas.
    4) Son de tipo secuencial
    """

    tuple1 = ()
    tuple2 = (100, 200, 300)
    tuple3 = 'mulan', 'pucca', 'percy',
    tuple4 = tuple(i for i in range(1, 100))

    print(tuple1)
    print(tuple2)
    print(tuple3)
    print(tuple4)

    return tuple1, tuple2, tuple3, tuple4


# Funcion de Sets
def func_sets() -> set:

    """
    1) Almacenan objetos no-duplicados
    2) De acceso rapido
    3) Aceptan operaciones logicas
    4) Son desordenados
    """

    set1 = {1, 4, 5, 9, 18, 'hola'}
    set2 = set()
    numbers = [1, 2, 3, 4, 5]
    set3 = set(numbers)
    set4 = {s**2 for s in range(10)}

    print(set1)
    print(set2)
    print(set3)
    print(set4)

    return set1, set2, set3, set4


# Funcion de Diccionarios
def func_dict() -> dict:

    """
    1) Pares de llave/valor
    2) Arrays asociativos (Hash Maps)
    3) Son desordenados
    """

    dict1 = {'mulan': 1, 'pucca': 1.2, 'percy': 4}
    dict2 = dict(mulan=2, pucca=1.2, percy=4)
    dict3 = {i: i**2 for i in range(1, 101) if i % 2 == 0}

    print(dict1)
    print(dict2)
    print(dict3)

    return dict1, dict2, dict3


if __name__ == '__main__':

    func_list()
    func_tuples()
    func_sets()
    func_dict()
