"""

Tema: Recursividad y Factoriales.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

def factorial(n):
    """Calcula el factorial de n

        n int > 0
        returns n!
    """
    print(n)
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

a = int(input("Escribe un entero: "))

print(factorial(a))