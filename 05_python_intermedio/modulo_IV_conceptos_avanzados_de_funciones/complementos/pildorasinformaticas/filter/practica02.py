"""

Tema: Filter
Curso: Python.
Plataforma: Youtube.
Profesor: Juan Diaz (Pildoras informaticas).
Alumno: @edinsonrequena.

"""

class Empleado:

    def __init__(self, nombre, cargo, salario):

        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):

        return f'Mi nombre es {self.nombre} y tengo un salario de {self.salario}'


listaEmpleados = [
    Empleado('Andrea', 'Dev', 7500),
    Empleado('Ed', 'Dev', 10000),
    Empleado('Test', 'Dev', 5500),
    Empleado('Tes2', 'Dev', 2000),
]

salarios_altos = filter(lambda empleado: empleado.salario > 5000, listaEmpleados)

[print(i) for i in salarios_altos]
