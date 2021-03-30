"""

Tema: Cadenas.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

---------------------------------------

len(longitud)

idenxing(indexacion)

slicing(rebanadas)
    my_str[comienzo:fin:pasos]

"""

# Accediendo a la longitud del string
my_str = 'Platzi'
len(my_str)

# Accediendo a un indice especifico del string
my_str[0] # P
my_str[2] # a

# Notacion de slicing
my_str[2:] # atzi
my_str[:3] # Pla
my_str[:-2] # Plat
my_str[::2] # Paz

# Concatenacion
'Yo amo a ' + my_str # Yo amo a platzi
f'Yo amo a {my_str}' # Yo amo a platzi
f'Yo amo a {my_str}, ' * 100 # Yo amo a platzi, Yo amo a platzi, Yo amo a platzi, Yo amo a platzi,

"""

1) Los objetos de tipo str pueden representarse con comillas simples o dobles

2) El operador de + tiene diferente significado segun el tipo de dato (overload). Con cadenas significa concatenacion.

3) El operador * es el operador de repeticion con cadenas

4) Las cadenas son inmutables. Esto quiere decir que cuando concatenamos un valor a una variable de tipo str se genera un nuevo espacio en memoria.

"""

"""

Entradas (inputs)

1) Python tiene la funcion interna llamada input para recibir datos del usuario.

2) Input siempre regresa cadena, por lo que si queremos utilizar otro tipo, tenemos que hacer type casting

"""

name = input('Cual es tu nombre?: ')
print(name)
print(f'Tu nombre es {name}')

# Tipo str
number = input('Escribe un numero: ')
print(type(number))

# Tipo int
number = int(input('Escribe un numero: '))
print(type(number))

# Tipo float
number = float(input('Escribe un numero: '))
print(type(number))


