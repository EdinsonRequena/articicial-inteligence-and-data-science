"""
Tema: Algoritmos de optimizacion - 1-0 Problema del Morral.
Alumno: @edinsonrequena.
"""

import random


def morral(tamano_morral, pesos, valores, n):

    # Caso base 1
    if n == 0 or tamano_morral == 0:
        return 0

    # Caso base 2
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)

    return max(
    valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
    morral(tamano_morral, pesos, valores, n - 1)
    )


def main():

    tamano_morral = int(input('Escoge el peso del morral: '))
    cantidad = int(input('Escoge la cantidad de elementos y valores: '))

    pesos = [random.randint(0, 100) for i in range(cantidad)]
    valores = [random.randint(0, 100) for i in range(cantidad)]

    print(f'Los pesos son {pesos}')
    print(f'Los valores son {valores}')

    n = len(valores)
    print(n)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)

if __name__ == '__main__':
    main()
