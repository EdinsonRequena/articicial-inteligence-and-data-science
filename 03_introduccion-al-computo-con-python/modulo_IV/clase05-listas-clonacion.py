"""

Tema: Listas, mutabilidad y clonacion.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

a = [1, 2, 3]
b = a
print(b)

print(id(a)) # Aca podemos ver como a y b estan en el mismo lugar de
print(id(b)) # memoria, lo que quiere decir que son la misma lista.

c = list(a) # Aca estamos clonando lo que hay en a en c.
print(c) # Aca podemos ver que tienen los mismos elementos.
print(id(c)) # Aca podemos ver que ocupan distintos lugares en memoria, lo que quiere decir que son listas distintas.

a.append(5) # Modificamos a, lo que quiere decir que tambien se modifica b
print(a)
print(c) # Aca como podemos ver no se modifica c porque no ocupa el mismo lugar en memoria que a
            # ya que anteriormente habiamos clonado los elementos

d = a [::] # Otra forma de clonar una lista en otra en donde le indicamos que lo hara desde el indice 0 hasta el ultimo.
print(d)
print(id(d)) # Aca podemos ver que ocupan distintos lugares en memoria, lo que quiere decir que si se modifica a no se modificara d.

e = a [0:2] # Aca clonamos los elementos del 0 al 2 en el indice a
print(e)
print(id(e)) # Aca podemos ver que ocupa un lugar distinto en memoria.
