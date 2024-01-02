

(lambda x: x * 2)(3)  # Llamar lambda en el momento que es asignada

if __name__ == '__main__':
    lista_de_tuplas = [(2, 'b'), (3, 'c'), (1, 'a'), (4, 'd')]

# Ordenar la lista por el primer elemento de la tupla
ordenado_por_primer_elemento = sorted(
    lista_de_tuplas, key=lambda tupla: tupla[0])

print(ordenado_por_primer_elemento)  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

'''
En este ejemplo, la función lambda se utiliza como argumento de la función sorted() para especificar la clave de ordenamiento.
La lambda toma cada tupla como entrada y devuelve el valor del primer elemento de la tupla, que se utiliza para ordenar la lista.
El resultado final es la lista ordenado_por_primer_elemento que contiene las mismas tuplas, pero en orden ascendente por el valor del
primer elemento de la tupla.

Recordar que: la guía de estilos de código en python o como mejor se le conoce PEP8 nos dice que no deberíamos asignar a lambda.

referencias: https://www.flake8rules.com/rules/E731.html, https://peps.python.org/pep-0008/, https://platzi.com/comentario/4702459/
'''
