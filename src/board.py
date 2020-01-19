from collections import namedtuple
from .wall import Wall
from .food import Food


Field = namedtuple('Field', ['character', 'food'])

class Board:
    """Pacman game board"""

    def __init__(self, len_row, len_col):
        self._arr = [[None] * len_col] * len_row
        self.len_row = len_row
        self.len_col = len_col

    @classmethod
    def from_file(cls, file):
        """Creates empty Board from array of ' ', 1's and '.', 'o' characters.

        1 - means that field should be wall object
        ' ' - walkable space
        . - food normal
        o - food extra

        Args:
            arr: file with characters


        """
        f = open(file, "r")
        data = f.read().splitlines()
        f.close()

        row_number = len(data)
        col_number = len(data[0])
        board = Board(row_number, col_number)
        board._arr = [[board.map_array_character(el) for el in row] for row in data]

        return board

    def map_array_character(self, element):
        mapping = {"1": (Wall, ()),
                   ".": (Food , ()),
                   "o": (Food , (True,)),
                   ' ': (int, (0,))
                  }
        klass, args = mapping[element]
        
        return klass(*args)

    def is_wall(self, col, row):
        """Checks if board at x, y is Wall"""
        if col >= self.len_col or  row >= self.len_row:
            return False
        return isinstance(self._arr[row][col], Wall)

    def is_not_eaten_food(self, col, row):
        el = self._arr[row][col]
        return isinstance(el, Food) and not el.eaten
    
    def get_element(self, col, row):
        return self._arr[row][col]