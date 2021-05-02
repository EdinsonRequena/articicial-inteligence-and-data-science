"""
Mi Aporte!
Tema: Map (Con lambda)
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
    Empleado('Test', 'Dev', 2500),
    Empleado('Tes2', 'Dev', 2000),
    Empleado('Tes2', 'Dev', 3000),
]

listaEmpleadosComision = [i.salario for i in listaEmpleados if i.salario <= 3000]
listaMapeada = map(lambda arg: arg * 1.03, listaEmpleadosComision)
[print(i) for i in listaMapeada]
