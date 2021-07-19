
from .array import Array
from .grid import Grid

class Cube(object):
    """three-dimensional array"""

    def __init__(self, nrows, ncols, deep, value=None) -> None:
        """Initializes the Cube with nrows, ncols, deep and optional value"""
        self.data = Array(deep)
        for i in range(deep):
            self.data[i] = Grid(nrows, ncols, value)

    def __getdeep__(self) -> int:
        """Return the whole cube"""
        return len(self.data)

    def __str__(self) -> str:
        """Return the cube as a string"""
        result = ""
        for array in range(self.__getdeep__()):
            result += self.data[array].__str__()
            result += "\n"
        return str(result)
