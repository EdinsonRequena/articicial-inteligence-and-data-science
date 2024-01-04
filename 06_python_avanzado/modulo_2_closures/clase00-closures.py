"""
- Los closures son funciones que retornan otras funciones,
es decir, una función que retorna un closure, retorna una función.

- Los closures son funciones que pueden acceder a variables que no están definidas dentro de ellas mismas,
sino en el ámbito (scope) en el que fueron creadas.

- Los closures son funciones que recuerdan el estado de las variables al momento de ser invocadas,
y conservan este estado a través de reiteradas ejecuciones.
Es decir, el scope de las variables no se reinicia con cada llamado de la función, sino que se conserva.
"""

# Ejemplo 1


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

print(times3(9))  # 27
print(times5(3))  # 15
print(times5(times3(2)))  # 30


# Ejemplo 2
# Definición de la función externa
def outer_function(x):
    # Definición de la función interna (closure)
    def inner_function(y):
        return x + y
    return inner_function


# Creación de un closure
closure = outer_function(5)

# Uso del closure
result = closure(3)
print(result)  # Output: 8


# Ejemplo 3

def outer_function(message):
    """
    Esta es la función externa que toma un mensaje como entrada y
    devuelve una función interna.
    La función interna imprime el mensaje cuando se llama.
    """

    def inner_function():
        print(message)
    return inner_function


greeting = outer_function("Hello, world!")
greeting()  # Output: Hello, world!
