"""

Tema: Listas y mutabilidad.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

my_list = [1, 'dos', 3, True, 'cuatro', 5]
print(my_list[0]) # Imprime indice 0
print(my_list[:2]) # Imprime desde el inidce 0 hasta el 2
print(my_list[1:3]) # Imprime desde indice 1 hasta el 3
print(my_list[2:]) # Imprime desde el indice 2 hasta el ultimo

my_list.append(1) # Agrega un elemento al ultimo indice de la lista, los elementos en una lista pueden repetirse.
print(my_list)