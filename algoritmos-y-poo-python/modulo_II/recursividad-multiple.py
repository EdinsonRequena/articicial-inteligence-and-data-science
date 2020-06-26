"""

Tema: Complejidad Algoritmica. Notacion asintotica - Recursividad multiple
Curso: Pensamiento Computacional, 2da entrega.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

def fibonacci(n):
    ''' 
    Recursividad multiple
    O(2^n)
    '''
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    n = 100
    print(fibonacci(n))