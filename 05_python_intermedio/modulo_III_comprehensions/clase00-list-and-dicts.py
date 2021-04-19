"""

Tema: Listas y Diccionarios anidados
Curso: Python intermedio.
Plataforma: Platzi.
Profesor: Facundo García Martoni.
Alumno: @edinsonrequena.

"""

def main():

    my_list = [1, 'hey!', False, 35.2]
    my_dict = {'First name': 'Edinson', 'La t_name': 'Requena'}

    super_list = [
        {'First name': 'Edinson', 'Las name': 'Requena'},
        {'First name': 'Andrea', 'Last name': 'Vinas'},
        {'First name': 'Diana', 'Last name': 'Quintero'},
        {'First name': 'Vicky', 'Last name': 'Aguilar'},
    ]

    super_dict = {
        'Natural Numbers': [1, 2, 3, 4, 5],
        'Integers Numbers': [-2, -1, 0, 1, 2],
        'Racional NUmbers': [4.23, 20/5, 10/2],
    }

    for k, v in super_dict.items():
        print(k, '-', v)


if __name__ == '__main__':

    main()
