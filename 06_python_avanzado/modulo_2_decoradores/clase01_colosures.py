from typing import Callable

"""
Vicky, 3 -> VickyVickyVicky
Edinson, 4 -> EdinsonEdinsonEdinsonEdinson
"""


from typing import Callable


def make_repeater_of(n: int) -> Callable:
    """
    Returns a function that repeats a given word n times.

    Parameters:
    n (int): The number of times the word should be repeated.

    Returns:
    Callable: A function that takes a word as input and repeats it n times.
    """
    def repeater(word: str):
        assert isinstance(word, str), 'Word should be a string'
        return word * n
    return repeater


def run():
    repeat_5 = make_repeater_of(3)
    print(repeat_5('Vicky'))
    repeat_10 = make_repeater_of(4)
    print(repeat_10('Edinson'))


if __name__ == '__main__':
    run()
