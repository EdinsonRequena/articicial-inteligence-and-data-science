"""

Tema: Pasar funciones por parametro a otras funciones.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

def multiplicar_por_dos(n):

    return n * 2


def sumar_dos(n):

    return n + 2


def aplicar_operacion(funcion, numeros):

    resultados = []

    for numero in numeros:
        resultado = funcion(numero)
        resultados.append(resultado)

    print(resultados)

if __name__ == '__main__':

    nums = [5, 10, -4, 14/10]

    aplicar_operacion(multiplicar_por_dos, nums)
    aplicar_operacion(sumar_dos, nums)
