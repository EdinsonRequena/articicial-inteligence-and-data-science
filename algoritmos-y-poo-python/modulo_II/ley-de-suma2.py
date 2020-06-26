"""

Tema: Complejidad Algoritmica. Notacion asintotica - Ley de suma #2
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

def f(n):
    ''' 
    Ley de suma #2
    O(n) + O(n * n) = O(n + n^2) = O(n^2)
    '''
    for i in range(n):
        print(i)
    
    for i in range(n*n):
        print(i)

n = 5
f(n)