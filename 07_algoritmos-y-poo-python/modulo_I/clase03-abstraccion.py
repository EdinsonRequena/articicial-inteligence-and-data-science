"""

Tema: Programacion Orientada a Objetos. Abstraccion.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

class LibroDeMecanicaCuantica:

    def __init__(self, hermosa=True, complicada='Muchisimo'):
        self.hermosa = hermosa
        self.complicada = complicada

    def experimentos(self):
        self._doble_rendija()
        self._gato_de_schrödinger()


    def _doble_rendija(self):
        print('\n')
        print('------------------Experimento de la doble rendija------------------------------')
        print('''En una cámara oscura se deja entrar un haz de luz por una rendija estrecha.
                La luz llega a una pared intermedia con dos rendijas. Al otro lado de esta pared hay
                una pantalla de proyección o una placa fotográfica. Cuando una de las rejillas se
                cubre aparece un único pico correspondiente a la luz que proviene de la rendija abierta.
                Sin embargo, cuando ambas están abiertas en lugar de formarse una imagen de superposición
                de las obtenidas con las rendijas abiertas individualmente, se obtiene una figura de
                interferencias con rayas oscuras y otras brillantes.
        ''')


    def _gato_de_schrödinger(self):
        print('\n')
        print('------------------Experimento del gato de Schrödinger------------------------------')
        print('''Un gato, junto a un matraz con veneno y un dispositivo con una partícula radiactiva,
                dentro de una caja sellada. Si el dispositivo detecta radiación rompe el frasco,
                liberando el veneno que mata al gato. Según la interpretación de Copenhague,
                espués de un tiempo, el gato está al mismo tiempo vivo y muerto.
        ''')

if __name__ == '__main__':
    cuantica = LibroDeMecanicaCuantica()
    cuantica.experimentos()