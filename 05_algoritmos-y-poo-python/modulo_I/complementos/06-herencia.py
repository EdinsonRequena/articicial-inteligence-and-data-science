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


class Moto(Vehiculo):

    hcaballito = ''

    def caballito(self): self.hcaballito = 'Voy haciendo caballito'


    def estado(self):

        super().estado()
        print(f'Caballito: {self.hcaballito}')


class VElecetricos(Vehiculo):

    def __init__(self, autonomia, marcaElec, modeloElec):

        super().__init__(marcaElec, modeloElec)

        self.autonomia = autonomia


    def estado(self):

        super().estado()
        print(f'Autonomia: {self.autonomia}')


    def cargarEnergia(self): self.cargando = True


class BiciElectrica(VElecetricos, Vehiculo): pass


class Furgoneta(Vehiculo):

    def llevaCarga(self, carga):

        self.carga = carga
        self.siCarga = 'La furgoneta esta cargada'
        self.noCarga = 'La furgoneta no esta cargada'

        return self.siCarga if self.carga else self.noCarga

    def estado(self): # TODO #22

        super().estado()

        print(f'Lleva carga?: ')



class App: # TODO #16

    def crear(self):

        # Objeto bici
        bici = BiciElectrica(100, 'Test marca', 'Test Modelo')
        bici.estado()

        # Objeto Furgoneta
        furgoneta = Furgoneta('Test', 'Test2')
        furgoneta.estado()

        # Objeto Moto
        moto = Moto('Test Moto', 'Test moto')
        moto.caballito()
        moto.estado()

if __name__ == '__main__':

    App().crear()
