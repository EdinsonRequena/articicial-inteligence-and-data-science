"""

Tema: Filter
Curso: Python.
Plataforma: Youtube.
Profesor: Juan Diaz (Pildoras informaticas).
Alumno: @edinsonrequena.

"""

numbers = [3, 4, 6, 7, 45, 32, 3, 10]

def par(num):

    if num % 2 == 0:
        return True

print(list(filter(par, numbers)))
