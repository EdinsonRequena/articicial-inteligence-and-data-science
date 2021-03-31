"""

Tema: Listas y mutabilidad.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

a = [1, 2, 3]
b = a
print(b) # Vemos como los elementos de a pasan a estar en b

print(id(a)) # Aca podemos ver como a y b estan en el mismo lugar de
print(id(b)) # memoria, lo que quiere decir que son la misma lista.

c = [a, b] # c sera una lista que contigan las listas de a y b
print(c)
print(id(c)) # Aca podemos ver como c ocupa otro lugar en memoria.

a.append(5)
print(a) # Se agrega el elemento 5
print(b) # Se agrega el elemento 5 tambien porque a y b ocupan el mismo lugar en memoria
print(c) # Esto podemos verlo como si c fuese una caja que contiene las cajas a y b pero al a y b ocupar el mismo
            # espacio en memoria cuando se modifica a tambien se modifica b y viceversa.