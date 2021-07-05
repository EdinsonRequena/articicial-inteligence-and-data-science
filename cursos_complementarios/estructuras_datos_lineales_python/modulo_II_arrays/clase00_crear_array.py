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

    def __init__(self, capacity, fill_value = None) -> None:
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

    def __iter__(self):
        """
        Method to iter the array
        """
        current = 0
        while current < len(self.items):
            yield current
            current += 1

    def __getItem__(self, index):
        """
        method to get a specific index
        """
        return self.items[index]

    def __setItem__(self, index, new_item):
        """
        Method to set item in a specific index
        """
        self.items[index] = new_item
        return self.items

arr = Array(5)
print(len(arr))
print(arr)
print(arr.__len__())
for i in range(len(arr)):
    arr[i] = i + 1
print(arr.__iter__())
print(arr.__getItem__(2))
print(arr.__setItem__(2, 'hola'))
