"""

Tema: Programacion Orientada a Objetos. Decomposicion
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

class Computadora:

    def __init__(self, marca, modelo, color, tipo, sistema_operativo, estado=False):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.tipo = tipo
        self.sistema_operativo = sistema_operativo
        self.estado = estado
        self._temperatura = 0
        self._config_teclado = 'Americano'

class Procesador:

    def __init__(self, fabricante, modelo, frecuencia, nucleos, hilos, cache, funciona=True):
        self.fabricante = fabricante
        self.modelo = modelo
        self.frecuencia = frecuencia
        self.nucleos = nucleos
        self.hilos = hilos
        self.cache = cache
        self.funciona = funciona

class MemoriaRam():

    def __init__(self, fabricante, capacidad, funciona=True):
        self.fabricante = fabricante
        self.capacidad = capacidad
        self.funciona = funciona
