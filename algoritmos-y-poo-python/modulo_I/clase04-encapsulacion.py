"""

Tema: Programacion Orientada a Objetos. Encapsulacion y Decoradores.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

class CasillaVotacion:

    def __init__(self, indentificador, pais):
        self.__indentificador = indentificador
        self.__pais = pais
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def set_region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'la region {region} no es validad en {self.__pais}')

casilla = CasillaVotacion(394, ['Caracas', 'Valencia', 'Zulia'])
print(casilla.region)
print(casilla.__pais)
