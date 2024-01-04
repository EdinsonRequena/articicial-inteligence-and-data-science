"""
Un decorador en Python es una herramienta poderosa que permite modificar el comportamiento de una función o clase de manera elegante y expresiva.

Un decorador es esencialmente una función que toma otra función como argumento,
añade alguna funcionalidad y devuelve una función modificada. Los decoradores son una forma de metaprogramación,
y permiten alterar el comportamiento de funciones o métodos de manera dinámica sin necesidad de cambiar su código fuente.

Piensa en un decorador como un embalaje o una envoltura que puedes poner alrededor de una función.
Esta envoltura puede añadir características adicionales a la función original o modificar la forma en que se comporta,
pero sin alterar el código interno de la función original.

Imagina que tienes un regalo (la función original) y lo pones en una caja (el decorador).
Esta caja puede ser bonita y tener lazos (funcionalidades adicionales)
o puede tener una etiqueta especial que dice que el regalo debe ser abierto de una manera particular (modificando el comportamiento de la función).
El regalo en sí mismo no cambia, pero la forma en que se presenta y se utiliza sí puede variar gracias a la caja.
"""

# Ejemplo 1


def decorador(funcion):
    def envoltura():
        print("¡Algo antes de ejecutar la función!")
        funcion()
        print("¡Algo después de ejecutar la función!")
    return envoltura


@decorador
def mi_funcion():
    print("¡La función está siendo ejecutada!")


mi_funcion()

# Output:
# ¡Algo antes de ejecutar la función!
# ¡La función está siendo ejecutada!
# ¡Algo después de ejecutar la función!

# Ejemplo 2


def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@uppercase
def say_hi():
    return 'hello there'


print(say_hi())  # HELLO THERE
