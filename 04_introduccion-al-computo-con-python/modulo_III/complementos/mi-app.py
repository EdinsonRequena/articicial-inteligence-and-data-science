"""

Ejercicio: Crear un programa en el que el usuario pueda escoger cualquiera de los algoritmos creados en el modulo pasado.
Alumno: @edinsonrequena.

"""

class Logica:

    def aproximacion(self):

        objetivo = int(input('Escoge un numero: '))
        epsilon = 0.01
        paso = epsilon**2
        respuesta = 0.0

        while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
            print(abs(respuesta**2 - objetivo), respuesta)
            respuesta += paso

        if abs(respuesta**2 - objetivo) >= epsilon:
            print(f'No se encontro la raiz cuadrada {objetivo}')
        else:
            print(f'La raiz cudrada de {objetivo} es {respuesta}')

    def busqueda(self):

        objetivo = int(input('Escoge un numero: '))
        epsilon = 0.01
        bajo = 0.0
        alto = max(1.0, objetivo)
        respuesta = (alto + bajo) / 2

        while abs(respuesta**2 - objetivo) >= epsilon:
            print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
            if respuesta**2 < objetivo:
                bajo = respuesta
            else:
                alto = respuesta

            respuesta = (alto + bajo) / 2

        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

    def enumeracion(self):

        objetivo = int(input("Escribe un numero: "))
        respuesta = 0

        while respuesta**2 < objetivo:
            print(respuesta)
            respuesta += 1

        if respuesta**2 == objetivo:
            print(f'La raiz cuadrada de {objetivo} es {respuesta}')
        else:
            print(f'{objetivo} no tiene una raiz cuadrada exacta')

class App:

    def cli(self):

        print("*"*20 ,"Bienvenido, escribe la pirmera letra del algoritmo a ejecutar", "*"*20)
        print("[A]proximacion")
        print("[B]usqueda Binaria")
        print("[E]numeracion")

    def run(self):

        self.cli()

        command = input('Escogeras la letra: ')
        command = command.upper()

        if command == "A":
            Logica().aproximacion()
        elif command == "B":
            Logica().busqueda()
        elif command == 'E':
            Logica().enumeracion()


if __name__ == '__main__':

    App().run()