"""

Tema: Programacion Orientada a Objetos. Encapsulacion y Decoradores.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

class CasillaVotacion:

    def __init__(self, indentificador, pais):
        self._indentificador = indentificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def set_region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'la region {region} no es validad en {self._pais}')

casilla = CasillaVotacion(394, ['Caracas', 'Valencia', 'Zulia'])
print(casilla.region)
print(casilla._pais)
