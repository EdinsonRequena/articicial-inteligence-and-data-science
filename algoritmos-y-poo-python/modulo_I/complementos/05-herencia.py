"""

Tema: Herencia.
Curso: Curso de python, video 31.
Plataforma: Youtube.
Profesor: Juan diaz - Pildoras informaticas.
Alumno: @edinsonrequena.

"""

class Vehiculo:

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False


    def arrancar(self): self.enmarcha = True


    def acelerar(self): self.acelera = True


    def frenar(self): self.frena = True


    def estado(self):

        print(f"""Marca: {self.marca} \n Modelo: {self.modelo} \n En marcha: 
        {self.enmarcha} \nAcelera: {self.acelera},\n Frena: {self.frena} \n""") # TODO #13


class Furgoneta(Vehiculo):

    def llevaCarga(self, carga):

        self.carga = carga
        self.siCarga = 'La furgoneta esta cargada'
        self.noCarga = 'La furgoneta no esta cargada'

        return self.siCarga if self.carga else self.noCarga


class Moto(Vehiculo):

    hcaballito = ''

    def caballito(self): self.hcaballito = 'Voy haciendo caballito'


    def estado(self):

        print(f"""Marca: {self.marca} \n Modelo: {self.modelo} \n En marcha: 
        {self.enmarcha} \nAcelera: {self.acelera},\n Frena: {self.frena} \n Caballito: {self.hcaballito}""")

class Quad(Moto): pass


class App: # TODO #16

    def crear(self):

        # Objeto Quad que esta heredando del objeto Moto que este a su vez hereda del objeto vehiculo
        """         quad = Quad('Toyota', 'Cbar')
        quad.caballito()
        quad.arrancar()
        quad.estado() """

        # Objeto Furgoneta que hereda de Vehiculo
        furgoneta = Furgoneta('Test', 'Test2')
        print(furgoneta.llevaCarga(False))
        # furgoneta.estado()

if __name__ == '__main__':

    App().crear()
