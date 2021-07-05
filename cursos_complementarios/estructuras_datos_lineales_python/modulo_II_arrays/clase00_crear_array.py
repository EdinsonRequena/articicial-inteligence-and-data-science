"""
Tema: Arrays
Curso: Estructura de Datos Lineales (Python).
Plataforma: Platzi.
Profesor: Hector Vega.
Alumno: @edinsonrequena.
"""

class Array(object):
    """
    Create a own Array
    """

    def __init__(self, capacity: int, fill_value = None) -> None:
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self) -> int:
        """
        Method to Know the array's lenght
        """
        count = 0
        for i in self.items:
            count += 1
        return count

    def __str__(self) -> str:
        """Returns string representation of the array"""
        return str(self.items)

    def __iter__(self):
        """
        Method to iter the array
        """
        current = 0
        while current < len(self.items):
            yield current
            current += 1

    def __getitem__(self, index):
        """
        method to get a specific index
        """
        return self.items[index]

    def __setitem__(self, index, new_item):
        """
        Method to set item in a specific index
        """
        self.items[index] = new_item
        return self.items

arr = Array(5)
print(len(arr))
print(arr)
for i in range(len(arr)):
    arr[i] = i + 1
print(arr)
print(arr.__len__())
print(arr.__getitem__(3))
print(arr.__setitem__(1, 'hola'))