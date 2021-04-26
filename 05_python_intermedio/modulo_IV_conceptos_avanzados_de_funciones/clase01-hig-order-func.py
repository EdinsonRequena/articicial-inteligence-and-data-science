"""

Tema: Hig Order Functions
Curso: Python intermedio.
Plataforma: Platzi.
Profesor: Facundo García Martoni.
Alumno: @edinsonrequena.

"""

my_list = [1, 4, 5, 6, 9, 13, 19, 21]

#  Devolver los impares con list comprehensions
odd_list = [i for i in my_list if i % 2 != 0]
print(odd_list)

#  Devolver los impares con filter
#  odd_filter = list(filter(lambda x: x % 2, my_list))
#  odd_filter = list(filter(lambda x: x % 2 != False, my_list))
odd_filter = list(filter(lambda x: x % 2 != 0, my_list))
print(odd_filter)
