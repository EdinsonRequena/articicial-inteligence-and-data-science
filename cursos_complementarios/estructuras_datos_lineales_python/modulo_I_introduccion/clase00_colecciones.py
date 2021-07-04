"""

Tema: Colecciones
Curso: Estructura de Datos Lineales (Python).
Plataforma: Platzi.
Profesor: Hector Vega.
Alumno: @edinsonrequena.

"""


# Funcion de listas
def func_list(arg1: list, arg2: list, arg3: list) -> list:

    """
    1) Son de proposito general
    2) Es la estructura mas utilizada
    3) Tama;o dinamico
    4) De tipo secuencial
    5) Ordenable
    """

    print(arg1)
    print(arg2)
    print(arg3)

    return arg1, arg2, arg3


# Funcion de tublas
def func_tuples(arg1: tuple, arg2: tuple, arg3: tuple) -> tuple:

    """
    1) Inmutable (no se pueden agregar o cambiar).
    2) Utiles para datos constantes.
    3) Mas rapidas que las listas.
    4) Son de tipo secuencial
    """

    print(arg1)
    print(arg2)
    print(arg3)

    return arg1, arg2, arg3


# Funcion de Sets
def func_sets(arg1: set, arg2: set, arg3: set) -> set:

    """
    1) Almacenan objetos no-duplicados
    2) De acceso rapido
    3) Aceptan operaciones logicas
    4) Son desordenados
    """

    print(arg1)
    print(arg2)
    print(arg3)

    return arg1, arg2, arg3


# Funcion de Diccionarios
def func_dict(arg1: dict, arg2: dict, arg3: dict) -> dict:

    """
    1) Pares de llave/valor
    2) Arrays asociativos (Hash Maps)
    3) Son desordenados
    """

    print(arg1)
    print(arg2)
    print(arg3)

    return arg1, arg2, arg3


if __name__ == '__main__':

    # listas
    list1 = list()
    list2 = [False, any, 'Hola', 5, 3.45 ]
    list3 = [n**2 for n in range(1, 100) if n%2 == 0]
    func_list(list1, list2, list3)

    # Tuplas
    tuple1 = ()
    tuple2 = (100, 200, 300)
    tuple3 = 'mulan', 'pucca', 'percy',
    func_tuples(tuple1, tuple2, tuple3)

    # Sets
    set1 = {1, 4, 5, 9, 18, 'hola'}
    set2 = set()
    numbers = [1, 2, 3, 4, 5]
    set3 = set(numbers)
    func_sets(set1, set2, set3)

    # Dicts
    dict1 = {'mulan': 1, 'pucca': 1.2, 'percy': 4}
    dict2 = dict(mulan=2, pucca=1.2, percy=4)
    dict3 = {i: i**2 for i in range(1, 101) if i % 2 == 0}
    func_dict(dict1, dict2, dict3)