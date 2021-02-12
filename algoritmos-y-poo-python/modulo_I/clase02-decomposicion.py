"""

Tema: Programacion Orientada a Objetos. Decomposicion
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

class Computadora:

    def __init__(self, marca, tipo ,modelo, color):

        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.tipo = tipo
        self._temperatura = 0
        self._config_teclado = 'Americano'


    def encender(self, estado=False):

        encendido = f'La pc esta encencida, su temperatura es {self._temperatura + 20}!'
        apagado = f'La pc esta apagada, su temperatura es {self._temperatura}'

        if estado: print(encendido)
        else: print(apagado)


    def sistema(self, sistema_operativo):

        linux = 'Tu si que eres un verdadero cientifico computacional!'
        mac_os = 'Eres un ingeniero de software que invierte en sus equipos para optimizar su tiempo'
        windows = 'Meeeeh esa excusa de los juegos ya no sirve, hay muchisimos juegos ya para Linux. Estudia e invierte en ti!'

        if sistema_operativo == 'linux': print(linux)
        elif sistema_operativo == 'mac os': print(mac_os)
        elif sistema_operativo == 'windows': print(windows)
        else: print('Eres una persona rara!')

class Procesador:

    def __init__(self, fabricante, modelo, frecuencia, nucleos, hilos, funciona=True):

        self.fabricante = fabricante
        self.modelo = modelo
        self.frecuencia = frecuencia
        self.nucleos = nucleos
        self.hilos = hilos
        self.funciona = funciona

class MemoriaRam():

    def __init__(self, fabricante, capacidad, funciona=True):

        self.fabricante = fabricante
        self.capacidad = capacidad
        self.funciona = funciona

if __name__ == '__main__':
    pc1 = Computadora('HP', 'Laptop','Notebook pro 15', 'Negra')
    print(pc1.encender(True))
    print(pc1.sistema('linux'))

    pc1_procesador = Procesador('AMD', 'Ryzen 3 1200', '3.7', '4', '4', True)