class Persona():

    def __init__(self, nombre, edad, lugar_residencia):

        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia


        def descripcicion(self):

            print(f"Nombre: {self.nombre}, edad: {self.edad}, lugar de residencia: {self.lugar_residencia}")


class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad


    def descripcicion(self):

        super().descripcicion()

        print(f"Salario: ", self.salario, "Antiguedad: ", self.antiguedad)

class App:

    def crear(self):

        pass

if __name__ == '__main__':

    App().crear()