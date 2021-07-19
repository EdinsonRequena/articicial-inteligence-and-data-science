"""
Tema: Arrays
Curso: Estructura de Datos Lineales (Python).
Plataforma: Platzi.
Profesor: Hector Vega.
Alumno: @edinsonrequena.
"""

class Array(object):
    """A simple array"""

    def __init__(self, capacity: int, fill_value=None) -> None:
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

    def __getitem__(self, index: any) -> any:
        """
        returns a specific index
        """
        return self.items[index]

    def __setitem__(self, index, new_item):
        """
        set item in a specific index
        """
        self.items[index] = new_item
        return self.items

    def __fillslots__(self):
        """
        return a sequence of numbers according to the array's length
        """
        slots = self.items
        for i in range(len(slots)):
            slots[i] = i + 1
        return slots

    def __sumlements__(self) -> list or None:
        """
        return the sum of all array's elements if and only if the elements are integers
        """
        arr = self.items
        try:
            for i in range(len(arr)):
                if type(arr[i]) != int:
                    raise TypeError('Solo se pueden sumar enteros')
            return sum(arr)
        except TypeError as e:
            print(e)

    def __add__(self, index, item):
        """
        returns the array with de new element
        """
        arr = self.items
        return arr[:index] + [item] + arr[index:]

    def __append__(self, item):
        """
        returns the array with de new element at the end
        """
        arr = self.items
        return arr[:] + [item]

    def __pop__(self, index):
        """
        returns the array without the select element
        """
        arr = self.items
        arr.pop()
        return arr
