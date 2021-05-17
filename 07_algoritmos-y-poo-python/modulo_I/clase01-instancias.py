"""

Tema: Programacion Orientada a Objetos.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

class Coordenada:

    def __init__(self, x, y): # Constructor
        self.x = x
        self.y = y

    def distancia(self, otra_coordendada):
        """
        Metodo para calcular la distancia entre coordenadas.

        type x: int
        type y: int
        rtype: int
        """

        x_diff = (self.x - otra_coordendada.x)**2
        y_diff = (self.y - otra_coordendada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_1 = Coordenada(34, 100)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenada))

