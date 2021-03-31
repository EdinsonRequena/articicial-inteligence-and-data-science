"""

Tema: List comprehesion.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

elements = list(range(100)) # Creamos una elements con elementos que esten en el rango de 0 a 99.
print(elements)

double = [i * 2 for i in elements] # Multiplicamos por 2 los elementos de la elements.
print(double)

pares = [i for i in elements if i % 2 == 0] # iteramos los elementos en elements si o solo si estos son divisibles entre 2, o sea, son pares.
print(pares)

impares = [num for num in elements if num % 2 != 0] # Numeros impares
print(impares)

triple = [element *3 for element in elements] # Triplica cada elemento de la lista
print(triple)

cuadrado = [element **2 for element in elements] # Eeleva al cuadrado cada elemento de la lista
print(cuadrado)

cubo_pares = [element **3 for element in elements if element % 2 != 0]
print(cubo_pares)
print('½') # No sabia de esto XD