from array import Array

class Array2D:

    def __init__(self, nrows, ncols, value=None):
        self.data = Array(nrows)
        for nrow in range(nrows):
            self.data[nrow] = Array(ncols, value)

    def get_height(self) -> int:
        """Returns the Arrays's height"""
        rows = self.data
        res: int = 0
        for i in rows:
            res += 1
        return res

    def get_width(self) -> int:
        """Returns the Arrays's width"""
        cols = self.data[0]
        res: int = 0 # Probando nuevos features de python 3.9
        for i in cols:
            res += 1
        return res