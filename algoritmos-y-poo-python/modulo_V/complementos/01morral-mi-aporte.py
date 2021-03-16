"""
Tema: Algoritmos de optimizacion - 1-0 Problema del Morral.
Alumno: @edinsonrequena.
"""

def morral(tamano_morral, pesos, valores, n):

    # Caso base 1
    if n == 0 or tamano_morral == 0:
        return 0

    # Caso base 2
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)

    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
                morral(tamano_morral, pesos, valores, n - 1))


def main():

    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50
    n = len(valores)
    print(n)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)

if __name__ == '__main__':
    main()
