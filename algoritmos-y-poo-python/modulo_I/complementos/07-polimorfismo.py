class Coche:

    def desplazamiento(self):

        print('Me desplazo en cuatro ruedas')


class Moto:

    def desplazamiento(self):

        print('Me desplazo en dos ruedas')


class Camion:

    def desplazamiento(self):

        print('Me desplazo en seis ruedas!')


def desplazamientoVehiculo(vehiculo):

    vehiculo.desplazamiento()


def main():

    camion = Camion()
    desplazamientoVehiculo(camion)

    moto = Moto()
    desplazamientoVehiculo(moto)


if __name__ == '__main__':

    main()