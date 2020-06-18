"""

Tema: List comprehesion.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

lista = list(range(100)) # Creamos una lista con elementos que esten en el rango de 0 a 99.
print(lista)

double = [i * 2 for i in lista] # Multiplicamos por 2 los elementos de la lista.
print(double)

pares = [i for i in lista if i % 2 == 0] # Aca iteramos los elementos en lista si o solo si estos son divisibles entre 2, o sea, son pares.
print(pares)