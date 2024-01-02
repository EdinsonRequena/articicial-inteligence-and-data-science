from _collections_abc import Callable
# from typing import Callable
from typing import Dict, List, Tuple


xType = int or float
funcType = Callable[[int or float], int or float]
returnType = int or float


def high_ord_func(x: xType, func: funcType) -> returnType:
    return x + func(x)


result = high_ord_func(2, lambda x: x + 2)
# 2 + (2 + 1)
print(result)

result = high_ord_func(2, lambda x: x + 2)
print(result)
# change
result = high_ord_func(2, lambda x: x * 5)
print(result)
