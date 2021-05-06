"""

Tema: Manejo de Excepciones.
Curso: Python intermedio.
Plataforma: Platzi.
Profesor: Facundo García Martoni.
Alumno: @edinsonrequena.

"""

def palindrome(string):

    try:
        if len(string) == 0:
            raise ValueError('No se puede ingresar una cadena vacia')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palindrome(''))
except TypeError:
    print('Solo puedes ingresar numeros!')
