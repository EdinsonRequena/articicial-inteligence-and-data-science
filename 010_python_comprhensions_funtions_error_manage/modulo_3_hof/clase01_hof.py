

def increment(x: int) -> int:
    return x + 1


def increment_v2(x: int) -> int: return x + 1


def high_ord_func(x: int or float, func: callable) -> int or float:
    # In Python, a callable is any object that you can call using a pair of parentheses and, optionally, a series of arguments.
    # Functions, classes, and methods are all common examples of callables in Python.
    #  Besides these, you can also create custom classes that produce callable instances.
    return x + func(x)


def high_ord_func_v2(x: int, func: callable) -> int: return func(x)


result = high_ord_func(2, increment)
# 2 + (2 + 1)
print(result)

result: int = high_ord_func_v2(2, increment_v2)
print(result)
result = high_ord_func_v2(2, lambda x: x + 2)
print(result)
# change
result = high_ord_func_v2(2, lambda x: x * 5)
print(result)
