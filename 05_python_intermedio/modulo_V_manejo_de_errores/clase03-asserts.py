"""

Tema: Asserts Staments.
Curso: Python intermedio.
Plataforma: Platzi.
Profesor: Facundo García Martoni.
Alumno: @edinsonrequena.

"""

def palindrome(string):

    assert len(string) > 0, "Erroor"
    return string == string[::-1]

print(palindrome(''))