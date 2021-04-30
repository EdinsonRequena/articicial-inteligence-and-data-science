"""

Tema: Filter
Curso: Python.
Plataforma: Youtube.
Profesor: Juan Diaz (Pildoras informaticas).
Alumno: @edinsonrequena.

"""

numbers = [3, 4, 6, 7, 45, 32, 3, 10]
par = list(filter(lambda i: i % 2 == 0, numbers))
print(par)
