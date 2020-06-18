"""

Reto: Imprimir todos los numeros enteros (opuestos a naturales tambien) pares e impares dependiendo del valor n
que escoja el usuario
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

def pares(numero):
    """ Imprime todos los numeros pares del 0 hasta n o de n hasta 0

        int n 
        returns n    
    """

    if numero < 0 and numero % 2 != 0:
        for i in range(numero+1, 0, 2):
            print(i)
    elif numero < 0 and numero % 2 == 0:
        for i in range(numero, 0, 2):
            print(i)
    else:
        for i in range(0, numero, 2):
            print(i)

def impares(numero):
    """imprime todo los numeros impares desde 1 hasta n o desde n hasta 1 
    
        int n
        returns n
    """
    if numero < 0 and numero % 2 == 0:
        for i in range(numero+1, 1, 2):
            print(i)
    elif numero < 0 and numero % 2 != 0:
        for i in range(numero, 1, 2):
            print(i)
    else:
        for i in range(1, numero, 2):
            print(i)

if __name__ == '__main__':
    num = int(input('Escribe un entero: '))

    impares(num)
    print('Numeros Impares\n')

    pares(num)
    print('Numeros Pares')