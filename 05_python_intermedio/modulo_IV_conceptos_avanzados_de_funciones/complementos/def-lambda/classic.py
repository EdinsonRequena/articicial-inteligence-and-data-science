"""
Classic way to define a function in python
"""

def palindrome_def(x):
    """
    x: string
    return: string
    """

    print(x == x[::-1])