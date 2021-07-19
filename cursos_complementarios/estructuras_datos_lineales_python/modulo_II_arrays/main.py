"""The main File"""

from utils.grid import Grid
from utils.cube import Cube

if __name__ == '__main__':
    cube = Cube(3,3,3)
    print(cube)
    print('*************')
    grid = Grid(5, 3)
    grid.__fillvalues__()
    print(grid)
    print(grid.__getheight__())
    print(grid.__getwidth__())
    print(grid.__getrow__(4))
    print(grid.__getelement__(0, 1))