
my_list = [3, 4, 6, 7, 45, 32, 3, 10]

odd = list(filter(lambda x: x % 2 != 0, my_list)) #  Filter aplica una condicion

square = list(map(lambda x: x**2, my_list)) #  Map aplica una funcion

from functools import reduce
mult = reduce(lambda a, b: a*b, my_list)
