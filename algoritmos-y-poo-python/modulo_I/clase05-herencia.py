"""

Tema: Programacion Orientada a Objetos. Herencia.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

class Rectangulo:

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura


    def area(self): return self.base * self.altura


class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)


class App:

    def main(self):

        rectangulo = Rectangulo(4, 16)
        print(rectangulo.area())

        cuadrado = Cuadrado(17)
        print(cuadrado.area())

if __name__ == '__main__':

    App().main()