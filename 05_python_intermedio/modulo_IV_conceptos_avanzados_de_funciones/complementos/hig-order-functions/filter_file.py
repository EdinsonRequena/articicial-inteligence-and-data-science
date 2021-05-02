"""
Filter File Module
"""

from list_file import my_list

odd = list(filter(lambda x: x % 2 != 0, my_list))
