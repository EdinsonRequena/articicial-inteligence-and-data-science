"""

Tema: Complejidad Algoritmica. Notacion asintotica - Ley de suma
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

def f(n):
    '''
    Ley de suma.
    O(n) + O(n) = O(n+n) = O(2n) = O(n)    
    '''

    for i in range(n):
        print(i)
    
    for i in range(n):
        print(i)
