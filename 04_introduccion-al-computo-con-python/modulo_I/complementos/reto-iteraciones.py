"""
Escriba un programa que simule un relog usando bucles while

-------------------- Algoritmo ------------------------
1) Crear tres variables de tipo entero que almacenen la hora, los minutos y los segundos e inicalizarlas en 0.

2) Crear un bucle while que recorra la variable hora 24 veces

3) Dentro del bucle que recorre la variable hora crear otro bucle que recorra la variable min 60 veces

4) Dentro del bucle que recorre la variable min crear otro bucle que recorra la variable seg 60 veces

5) Dentro del bucle que recorre la variable seg imprimir por pantalla el valor de todas las variables recorridas

6) Dentro del bucle que recorre la variable seg sumarle uno a la variable seg en cada iteracion.

7) Dentro del bucle que recorre la variable min (pero fuera del bucle que recorre la variable seg)
sumarle uno a min en cada interacion y resetrar a cero la variable seg.

8) Dentro del bucle que recorre la variable hora (pero fuera del bucle que recorre la variable min)
sumarle uno a hora en cada iteracion y resetear a cero la variable min.

Este ejercicio fue propuesto por el profesor David Aeroesti del curso de pensamiento computacional de platzi.
"""

hora, minu, seg = 0, 0, 0

while hora < 24:
    while minu < 60:
        while seg < 60:
            print(hora, minu, seg)
            seg += 1

        minu += 1
        seg = 0

    hora += 1
    minu = 0
