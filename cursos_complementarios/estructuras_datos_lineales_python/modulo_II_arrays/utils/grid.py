"""
Tema: Arrays 2D
Curso: Estructura de Datos Lineales (Python).
Plataforma: Platzi.
Profesor: Hector Vega.
Alumno: @edinsonrequena.
"""

from .array import Array


class Grid(object):
    """Two dimensional Array """

    def __init__(self, nrows, ncols, value=None) -> None:
        """Initializes the Arrays with nrows, ncols and optional value"""
        self.data = Array(nrows)
        for nrow in range(nrows):
            self.data[nrow] = Array(ncols, value)

    def __getheight__(self) -> int:
        """Returns the Arrays's height"""
        rows = self.data
        res: int = 0
        for i in rows:
            res += 1
        return res

    def __getwidth__(self) -> int:
        """Returns the Arrays's width"""
        cols = self.data[0]
        res: int = 0 #  Probando nuevos features de python 3.9
        for i in cols:
            res += 1
        return res

    def __getrow__(self, index) -> any:
        """Returns the index-th row"""
        try:
            if index == 0:
                raise IndexError('Index out of range')
            return self.data[index - 1]
        except IndexError as e:
            print(e)

    def __getelement__(self, index_x, index_y) -> any:
        """Returns the value of the index (x,y)"""
        try:
            if index_x == 0 or index_y == 0:
                raise IndexError('Index out of range')
            return self.data[index_x][index_y]
        except IndexError as e:
            print(e)

    def __str__(self) -> str:
        """Returns string representation of the grid"""
        rows = self.data
        res = ""
        for nrow in range(self.__getheight__()):
            for ncol in range(self.__getwidth__()):
                res += str(rows[nrow][ncol]) + " "
            res += "\n"
        return res

    def __fillvalues__(self) -> None:
        """Fills the array with random values"""
        for nrow in range(self.__getheight__()):
            for ncol in range(self.__getwidth__()):
                self.data[nrow][ncol] = nrow * ncol
