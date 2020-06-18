"""

Tema: Manejo de excepciones.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

def division(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as error:
        print(f'The error is: {error}')
        return lista

if __name__ == '__main__':
    lista = list(range(10))
    divisor = int(input('Escribe un numero: '))

    print(division(lista, divisor))