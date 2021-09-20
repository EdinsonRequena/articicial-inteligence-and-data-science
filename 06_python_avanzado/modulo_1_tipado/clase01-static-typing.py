"""
Pratice Static Typing
"""

from typing import Dict, List, Tuple

# Example 1
a: int = 1
b: str = 'I am a string'
c: bool = True

# Example 2
def add(a: int, b: int) -> int:
    return a + b


# Example 3
positives_numbers: List[int] = [1, 2, 3, 4, 6, 6, 7, 8]

# Example 4
users_at_platzi: Dict[str, int] = {
    'Venezuela': 5000,
    'Mx': 100000,
    'Argentina': 2000
}

# Example 5
countries: List[Dict[str, str]] = [
    {
        'name': 'Venezuela',
        'capital': 'Caracas'
    },
    {
        'name': 'Argentina',
        'capital': 'Buenos Aires'
    }
]

# Example 6
num: Tuple[int, bool, str, float] = (1, False, 'Hola', 3.5)

# Example 7
msg: str = 'This are the coordinates'
CoordinatesType = list[Dict[str, Tuple[int, int, str]]]

coordinates: CoordinatesType = [
    {
        'place1': (4, 5, msg),
        'place2': (10, 45, msg),
    },
    {
        'place1': (42, 555, msg),
        'place2': (104, 945, msg),
    },
]
