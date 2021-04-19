"""

Haciendo un manejo mas avanzado de este tipo de estructuras de datos

alumno: @edinsonrequena

"""

class App:

    def lists_and_dicts(self):

        self.super_list = [
            {'First name': 'Edinson', 'Last name': 'Requena'},
            {'First name': 'Andrea', 'Last name': 'Vinas'},
            {'First name': 'Diana', 'Last name': 'Quintero'},
            {'First name': 'Vicky', 'Last name': 'Aguilar'},
        ]

        self.super_dict = {
            'Natural Numbers': [1, 2, 3, 4, 5],
            'Integers Numbers': [-2, -1, 0, 1, 2],
            'Racional Numbers': [4.23, 20/5, 10/2],
        }

    def dict_comprehensions(self):

        self.lists_and_dicts()

        {print(k, '-' ,v) for k, v in self.super_dict.items()} # Imprime las llaves y valores
        {print(k) for k in self.super_dict.keys()} # Imprime solo las llaves
        {print(v) for v in self.super_dict.values()} # Imprime solo los valores

    def list_comprehensions(self):

        self.lists_and_dicts()

        [print(item) for item in self.super_list] # Imprime toda la lista
        [print(name['First name']) for name in self.super_list] # Imprime todos los nombres
        [print(last['Last name']) for last in self.super_list] # Imprime todos los apellidos
        [print(i['First name'], '-', i['Last name']) for i in self.super_list] # Imprime nombre y apellidos

    def run(self):

        self.dict_comprehensions()
        self.list_comprehensions()


def main():

    App().run()


if __name__ == '__main__':

    main()
