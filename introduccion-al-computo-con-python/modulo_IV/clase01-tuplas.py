"""

Tema: Tuplas.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

my_tuple = ()
print(type(my_tuple))

my_tuple = (1, 'two', False)
print(my_tuple[0])
print(my_tuple[2])

my_tuple = (1)
print(type(my_tuple))

my_tuple = (1,)
print(type(my_tuple))

my_other_tuple = (2, 3, 4)
print(my_other_tuple)
my_tuple += my_other_tuple
print(my_tuple)

x, y, z = my_other_tuple
print(x)
print(y)
print(z)
print(my_other_tuple)

# a, b, c, d, f = my_other_tuple ValueError: not enough values to unpack (expected 5, got 3)
# print(my_other_tuple) ValueError: not enough values to unpack (expected 5, got 3)

def cooderdenadas_func():
    return (5, 4)

cooderdenadas_tuple = cooderdenadas_func()
print(cooderdenadas_tuple)

x, y = cooderdenadas_func()
print(x)
print(y)
