DATA = [
    {
        'name': 'Edinson',
        'age': 25,
        'organization': 'Conceptual',
    },
    {
        'name': 'Angel',
        'age': 17,
        'organization': 'Globant',
    },
    {
        'name': 'Andrea',
        'age': 20,
        'organization': 'Platzi',
    }
]

conceptual_workers = list(filter(lambda arg: arg['organization'] == 'Conceptual', DATA))
conceptual_workers_mapping = list(map(lambda arg: arg['name'], conceptual_workers))
[print(i) for i in conceptual_workers_mapping]

rich_people = list(map(lambda arg: arg | {'rich': arg['organization'] == 'Platzi'}, DATA))
[print(i) for i in rich_people]