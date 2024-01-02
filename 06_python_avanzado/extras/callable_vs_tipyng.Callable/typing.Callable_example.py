"""
Ejemplos de typing.Callable

1) Anotación de Tipo para un Argumento de Función:
Supongamos que tienes una función aplicar_funcion que toma otra función como argumento y un valor sobre el cual aplicar esa función.
Puedes usar typing.Callable para anotar el tipo de la función argumento.

2) Especificando Tipos de Argumentos y Retorno:
Puedes ser más específico con typing.Callable indicando los tipos de los argumentos y del valor de retorno de la función que se pasará.
"""

from typing import Callable


def aplicar_funcion(func: Callable[[int], int], valor: int) -> int:
    return func(valor)


def cuadrado(x: int) -> int:
    return x * x


# Uso de la función
resultado = aplicar_funcion(cuadrado, 5)
print(resultado)  # Salida: 25


def procesar_dato(func: Callable[[str], bool], dato: str) -> bool:
    return func(dato)


def es_mayuscula(cadena: str) -> bool:
    return cadena.isupper()


# Uso de la función
print(procesar_dato(es_mayuscula, "HOLA"))  # Salida: True
print(procesar_dato(es_mayuscula, "Hola"))  # Salida: False


def make_repeater_of(n: int) -> Callable[[str], str]:
    def repeater(word: str):
        assert isinstance(word, str), 'Word should be a string'
        return word * n
    return repeater


print(make_repeater_of(3)('Vicky'))  # VickyVickyVicky
print(make_repeater_of(4)('Edinson'))  # EdinsonEdinsonEdinsonEdinson
