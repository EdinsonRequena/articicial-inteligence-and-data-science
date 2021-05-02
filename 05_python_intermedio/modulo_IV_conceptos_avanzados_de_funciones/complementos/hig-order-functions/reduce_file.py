"""
Reduce Module
"""

from functools import reduce
from list_file import my_list

mult = reduce(lambda a, b: a*b, my_list)