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
        return super().habilidad()

class Matematico(Cientifica):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def habilidad(self):
        print('Todas las ciencias derivan de las matematicas, JA!')


def main():
    cientifico = Cientifica('Andrea')
    cientifico.habilidad()

    fisico = Fisico('Edinson')
    fisico.habilidad()

    matematico = Matematico('Oriana')
    matematico.habilidad()

if __name__ == '__main__':
    main()