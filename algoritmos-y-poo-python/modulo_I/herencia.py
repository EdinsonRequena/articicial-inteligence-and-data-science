"""

Tema: Programacion Orientada a Objetos. Herencia.
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

class PesimoPresidente: # TODO #11

    def __init__(self, nombre, pais, habilidad):
        self.nombre = nombre
        self.pais = pais
        self.habilidad = habilidad # Tambien se puede programar con sarcasmo


    def saludo(self):
        print(f'Hola mi nombre es {self.nombre}, para la poca fortuna de los habitantes de {self.pais} naci alli y mi habilidad es {self.habilidad}')


class Chavez(PesimoPresidente):

    def __init__(self, nombre, pais, habilidad):
        super().__init__(nombre, pais, habilidad)


class Trump(PesimoPresidente):

    def __init__(self, nombre, pais, habilidad):
        super().__init__(nombre, pais, habilidad)

def main():
    chavez = Chavez('Hugo chavez', 'Venezuela', 'destruir economias')
    print(chavez.saludo())

    print('\n')

    trump = Trump('Donald Trump', 'Estados Unidos', 'hacer america una basura otra vez!')
    print(trump.saludo())

if __name__ == '__main__':
    main()