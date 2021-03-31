"""

Tema: Listas y mutabilidad.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

Append: permite meter un elemento en el ultimo indice de la lista
pop: permite sacar el ultimo elemento de la lista
Remove: Remueve un elemento en un indice especifico
Insert:  Inserta un indice en un indice espefico

"""

my_list = [1, 'dos', 3, True, 'cuatro', 5]
print(my_list)
print(my_list[0]) # Imprime indice 0
print(my_list[:2]) # Imprime desde el inidce 0 hasta el 2
print(my_list[1:3]) # Imprime desde indice 1 hasta el 3
print(my_list[2:]) # Imprime desde el indice 2 hasta el ultimo

my_list.append(1) # Agrega un elemento al ultimo indice de la lista, los elementos en una lista pueden repetirse.
print(my_list)

my_list[0] = 'hola' # Modificamos el indice 0 de la lista.
print(my_list)

my_list.pop() # Quitamos el ultimo indice de la lista.
print(my_list)

a = 3
my_list.insert(1, a) # Aca insertamos el valor de una variable en el indice 1 de la lista.
print(my_list)

my_list.remove(3) # Remueve el valor del elemento (no el indice).
# Si el elemento tiene el mismo valor que otro dentro de la lista se removera solo el de menor indice.
print(my_list)

for element in my_list: # Iteramos en los elementos de la lista.
    print(element)
