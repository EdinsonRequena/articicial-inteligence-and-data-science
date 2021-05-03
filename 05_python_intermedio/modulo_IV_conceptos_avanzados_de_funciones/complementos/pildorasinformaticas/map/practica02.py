"""
Mi Aporte!
Tema: Map (Con lambda y operador ternario)
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

listaMapeada = map(lambda arg: arg.salario * 1.03 if arg.salario <= 3000 else arg, listaEmpleados)
[print(i) for i in listaMapeada]
