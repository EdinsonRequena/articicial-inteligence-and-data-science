"""

Tema: Hig Order Functions
Curso: Python intermedio.
Plataforma: Platzi.
Profesor: Facundo García Martoni.
Alumno: @edinsonrequena.

"""

my_list = [3, 6, 3, 2, 7]

#  Devolver los impares con list comprehensions
odd_list = [i for i in my_list if i % 2 != 0]
print(odd_list)

#  Devolver los impares con filter
#  odd_filter = list(filter(lambda x: x % 2, my_list))
#  odd_filter = list(filter(lambda x: x % 2 != False, my_list))
odd_filter = list(filter(lambda x: x % 2 != 0, my_list))
print(odd_filter) # Filter aplica una condicion

#  Devolver el cuadrado de los numeros en la lista con list comprehension
square_list = [i**2 for i in my_list]
print(square_list)

#  Devolver el cuadrado de los numeros en la lista con map
square_map = list(map(lambda x: x**2, my_list))
print(square_map) # Map aplica una funcion

#  Devolver la multiplicacion de todos los mumeros dentro de la lista
mult = 1
for i in my_list:
    mult *= i
print(mult)

#  Devolver la multiplicacion de todos los mumeros dentro de la lista con reduce
from functools import reduce
mult = reduce(lambda a, b: a*b, my_list)
print(mult)
