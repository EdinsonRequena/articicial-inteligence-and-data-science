"""

Tema: Herencia.
Curso: Curso de python, video 30.
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


class Moto(Vehiculo): pass


class App: # TODO #16

    def crear(self):

        objeto_moto_1 = Moto('Honda', 'CBR')
        objeto_moto_2 = Moto('Horse', 'x34')
        objeto_moto_1.estado()
        objeto_moto_2.estado()


if __name__ == '__main__':

    App().crear()
