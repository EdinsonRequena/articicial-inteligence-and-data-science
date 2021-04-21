
super_list = [
    {'First name': 'Edinson', 'Last name': 'Requena'},
    {'First name': 'Andrea', 'Last name': 'Vinas'},
    {'First name': 'Angel', 'Last name': 'Verde'},
    {'First name': 'Victoria', 'Last name': 'Aguilar'},
]

super_dict = {
    'Natural Numbers': [1, 2, 3, 4, 5],
    'Integers Numbers': [-2, -1, 0, 1, 2],
    'Racional Numbers': [4.23, 20/5, 10/2],
}


def dict_comprehensions(super_dict):

    {print(k, '-', v) for k, v in super_dict.items()}
    {print(k) for k in super_dict.keys()}
    {print(v) for v in super_dict.values()}


def list_comprehensions(super_list):

    [print(item) for item in super_list]
    [print(name['First name']) for name in super_list]
    [print(last['Last name']) for last in super_list]
    [print(i['First name'], '-', i['Last name']) for i in super_list]


if __name__ == '__main__':

    list_comprehensions(super_list)
    dict_comprehensions(super_dict)
