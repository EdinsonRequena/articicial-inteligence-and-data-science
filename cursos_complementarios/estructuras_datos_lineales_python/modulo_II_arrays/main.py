"""The main File"""

from utils.grid import Grid

if __name__ == '__main__':

    grid = Grid(3,5)
    grid.__fillvalues__()
    print(grid)
    print(grid.__getheight__())
    print(grid.__getwidth__())
    print(grid.__getrow__(3))
    print(grid.__getelement__(2, 2))