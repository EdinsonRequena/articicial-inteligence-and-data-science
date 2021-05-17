"""

Tema: Programacion Orientada a Objetos.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

class Hotel:
    
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento): # Utilizamos el método especial __init__ 
                                                                                # para definir el estado inicial de nuestra instancia.
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0

    # Creamos las instancias que le daran funcionalidad a nuestra clase Hotel.
    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes
        return self.huespedes, cantidad_de_huespedes

    def checkout(self, a):
        self.huespedes -= a


    def ocupacion_total(self):
        return self.huespedes

# Definimos nuestras instancias.
hotel = Hotel(50, 20)
print(hotel.numero_maximo_de_huespedes, hotel.lugares_de_estacionamiento)
print(hotel.anadir_huespedes(60))
print(hotel.checkout(10))
print(hotel.ocupacion_total())
