from .wall import Wall
from .food import Food
from collections import namedtuple

Field = namedtuple('Field', ['character', 'food'])

class Board:
    """Pacman game board"""

    def __init__(self, rows, cols):
        self._arr = [[0] * cols] * rows

    @classmethod
    def from_array(cls, arr):
        """Creates empty Board from array of 0 and 1's.

        1 - means that field should be wall object
        0 - walkable space with food, and space for movable object 
            Tuple (Movable, Food)

        Args:
            arr: array with 0 and 1


        """
        rowN = len(arr)
        colN = len(arr[0])
        board = Board(rowN, colN)
        for row in range(rowN):
            for col in range(colN):
                if arr[row][col] == 1:
                    board._arr[row][col] = Wall(col, row)
                else:
                    board._arr[row][col] = Field(None, Food(col, row))
        
        return board

    def set_character(self, character):
        """Fills board with character object.

        Characters should have x, y coordinates.
        
        Args:
            character: array of objects with x, y fields.

        """
        col, row = character.getCords()
        self._arr[row][col] = self._arr[row][col]._replace(character=character)

    def update(character):
        pass