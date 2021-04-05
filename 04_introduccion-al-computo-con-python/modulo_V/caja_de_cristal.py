"""

Tema: Pruebas Unitarias.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

import unittest

def mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    def test_es_mayor(self):
        edad = 12

        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado, True)
    

    def test_es_menor(self):
        edad = 20

        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado, False)

if __name__ == '__main__':
    unittest.main()