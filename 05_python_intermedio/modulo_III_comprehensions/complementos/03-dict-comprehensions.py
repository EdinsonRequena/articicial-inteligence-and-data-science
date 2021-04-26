
from math import sqrt

#  Reto 1
my_dict = {i: i**2 for i in range(1, 101) if i % 2 == 0}
print(my_dict)

#  Reto 2
my_dict2 = {i: sqrt(i) for i in range(1, 1001)}
print(my_dict2)

