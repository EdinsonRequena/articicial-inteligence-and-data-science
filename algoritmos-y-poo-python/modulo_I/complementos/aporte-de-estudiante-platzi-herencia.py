"""
Aporte de un alumno de platzi

"""

class Programador:

    def __init__(self, nombre, edad, numero_de_empleado, skill):
        self.nombre = nombre
        self.edad = edad
        self.numero_de_empleado = numero_de_empleado
        self.skill = skill

    def programar(self):
        print(f'Hola, estoy programando en {self.skill}')

class ProgramadorJava(Programador):

    def __init__(self, nombre, edad, numero_de_empleado, skill = 'Java'):
        super().__init__(nombre, edad, numero_de_empleado, skill)

class ProgramadorPython(Programador):

    def __init__(self, nombre, edad, numero_de_empleado, skill = 'Python'):
        super().__init__(nombre, edad, numero_de_empleado, skill)

class ProgramadorCpp(Programador):

    def __init__(self, nombre, edad, numero_de_empleado, skill = 'C++'):
        super().__init__(nombre, edad, numero_de_empleado, skill)


def main():
    programador_java = ProgramadorJava('Ricardo', 25, 1234)
    programador_python = ProgramadorPython('Sofía', 20, 1345)
    programador_cpp = ProgramadorCpp('Gilberto', 35, 5637)

    programador_java.programar()
    programador_python.programar()
    programador_cpp.programar()


if __name__ == "__main__":
    main()
