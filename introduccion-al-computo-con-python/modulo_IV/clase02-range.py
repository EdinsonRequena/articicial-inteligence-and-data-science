"""

Tema: Rangos.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

# range(comienzo, fin, pasos)

my_range = range(1, 5)
print(type(my_range))

for i in my_range:
    print(i)

my_range = range(0, 7, 2) # 0, 2, 4, 6
my_other_range = range(0, 8, 2) # 0, 2, 4, 6

print(my_range == my_other_range) # True

print(id(my_range))
print(id(my_other_range))
print(my_range is my_other_range) # False

for i in range(0, 101, 2):
    print(i)
