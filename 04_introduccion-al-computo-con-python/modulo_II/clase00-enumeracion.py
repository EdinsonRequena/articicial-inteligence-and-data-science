"""

Tema: Algoritmo de enumeracion exahustiva.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

objetivo = int(input("Escribe un numero: "))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1

if respuesta**2 == objetivo: print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else: print(f'{objetivo} no tiene una raiz cuadrada exacta')