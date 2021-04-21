"""

Resolviendo Retos
alumno: @edinsonrequena

"""


def squeares():

    arr = [i**2 for i in range(1, 101)]
    #  print(arr)


def squeares_divisible_3():

    #  arr = [i**3 for i in range(1, 101) if i % 3 == 0]
    arr = [i**2 for i in range(1, 101) if i % 3 is False]
    print(arr)


def squeares_par():

    #  arr = [i**2 for i in range(1, 101) if i % 2 == 0]
    arr = [i**2 for i in range(1, 101) if i % 2 is False]
    print(arr)
