set_countries = {'col', 'mex', 'bol'}
print(set_countries)

set_countries2 = {'col', 'mex', 'bol', 'col'}
print(set_countries2)  # {'col', 'mex', 'bol'}

set_types = {1, 'hola', False, 12.12}
print(set_types)  # {False, 1, 12.12, 'hola'}

set_from_string = set('hoola')
print(set_from_string)  # {'a', 'l', 'o', 'h'}

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)  # {'as', 'abc', 'cbv'}

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)  # {1, 2, 3, 4}
unique_numbers = list(set_numbers)
print(unique_numbers)
