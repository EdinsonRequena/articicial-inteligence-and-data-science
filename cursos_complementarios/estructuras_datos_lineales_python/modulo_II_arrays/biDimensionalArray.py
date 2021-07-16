from array import Array

class Array2D:

    def __init__(self, nrows, ncols, value=None):
        self._the_rows = Array(nrows)
        for nrow in range(nrows):
            self._the_rows[nrow] = Array(ncols, value)

    def get_height(self):
        """Returns the Arrays's height"""
        row = self._the_rows
        