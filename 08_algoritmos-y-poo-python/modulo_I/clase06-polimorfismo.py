"""

Tema: Programacion Orientada a Objetos. Polimorfismo.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

class Cientifica:

    def __init__(self, nombre):

        self.nombre = nombre


    def habilidad(self):

        print('Soy muy inteligente')


class Fisico(Cientifica):

    def __init__(self, nombre):

        super().__init__(nombre)


    def habilidad(self):

        super().habilidad()


class Matematico(Cientifica):

    def __init__(self, nombre):

        super().__init__(nombre)

    def habilidad(self):

        super().habilidad()
        print('Todas las ciencias derivan de las matematicas, JA!')

class App:

    def main(self):

        cientifico = Cientifica('Andrea')
        cientifico.habilidad()

        fisico = Fisico('Edinson')
        fisico.habilidad()

        matematico = Matematico('Oriana')
        matematico.habilidad()

if __name__ == '__main__':

    App().main()