"""

Tema: Programas ramificados.
Curso: Pensamiento computacional.
Plataforma: Platzi.
Profesor: David Aroesti.
Alumno: @edinsonrequena.

"""

user_1 = input('Type your name: ')
user_1_age = int(input('Type your age: '))

user_2 = input('Type your name: ')
user_2_age = int(input('Type your age: '))

if user_1_age > user_2_age: print(f'{user_1} is older than {user_2}.')
elif user_1_age < user_2_age: print(f'{user_1} is younger than {user_2}')
elif user_1_age == user_2_age: print(f'{user_2} and {user_1} are there same age')
else: print("Try again, don't be idiot pls")
