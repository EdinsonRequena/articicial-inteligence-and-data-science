# Reference: https://realpython.com/python-zip-function/#:~:text=Python's%20zip()%20function%20creates,programming%20problems%2C%20like%20creating%20dictionaries.

dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}

print(dict_two.keys())
print(dict_one.values())


# res = zip(dict_one.items())

# print(res)

# for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# dict_one_with_items_method = [('name', 'John'), ('last_name', 'Doe'), ('job', 'Python Consultant')]
# dict_two_with_items_method = [('name', 'John'), ('last_name', 'Doe'), ('job', 'Python Consultant')]
# zip_result = [('name', 'John', 'name', 'Jane'), ('last_name', 'Doe', 'last_name', 'Doe'), ('job', 'Python Consultant', 'job', 'Community Manage')]
