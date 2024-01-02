"""
Ejemplos de callable

1)Comprobación en Tiempo de Ejecución:
Puedes usar callable para verificar si un objeto puede ser llamado como una función.

2) Tomando Decisiones Basadas en la Invocabilidad:
Puedes usar callable para decidir qué acción tomar dependiendo de si un objeto es invocable o no.
"""

# Ejemplo 1


def mi_funcion():
    print("Hola Mundo!")


class MiClase:
    def __call__(self):
        print("Objeto invocable")


objeto_normal = MiClase()
objeto_no_invocable = 5

print(callable(mi_funcion))            # Salida: True
print(callable(objeto_normal))         # Salida: True
print(callable(objeto_no_invocable))   # Salida: False


# Ejemplo 2

def ejecutar_si_es_invocable(obj):
    if callable(obj):
        obj()
    else:
        print("El objeto no es invocable")


def funcion_ejemplo():
    print("Función ejecutada")


ejecutar_si_es_invocable(funcion_ejemplo)  # Salida: "Función ejecutada"
ejecutar_si_es_invocable(123)  # Salida: "El objeto no es invocable"
ejecutar_si_es_invocable("Hola Mundo!")  # Salida: "El objeto no es invocable"
