DATA = [
    {
        'name': 'Edinson',
        'organization': 'Conceptual',
    },
    {
        'name': 'Angel',
        'organization': 'Globant',
    },
    {
        'name': 'Andrea',
        'organization': 'Platzi',
    }
]

conceptual_workers = list(filter(lambda arg: arg['organization'] == 'Conceptual', DATA))
conceptual_workers_mapping = list(map(lambda arg: arg['name'], conceptual_workers))
[print(i) for i in conceptual_workers_mapping]

bad_salary = list(map(lambda arg: arg | {'bad salary': arg['organization'] == 'Conceptual'}, DATA))
[print(i) for i in bad_salary]