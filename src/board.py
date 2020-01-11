from .wall import Wall
from .food import Food
from collections import namedtuple

Field = namedtuple('Field', ['character', 'food'])

class Board:
    """Pacman game board"""

    def __init__(self, len_row, len_col):
        self._arr = [[None] * len_col] * len_row
        self.len_row = len_row
        self.len_col = len_col

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
        board._arr = [[Wall() if el == 1 else Field(None, Food()) for el in row] for row in arr]
                    
        return board

    def set_character(self, character):
        """Fills board with character object.

        Characters should have x, y coordinates.
        
        Args:
            character: array of objects with x, y fields.

        """
        col, row = character.getCords()
        
        
        assert isinstance(self._arr[row][col], Field), f"You are trying to set character {character.__class__} on wall  x: {col}, y: {row}"
        self._arr[row][col] = self._arr[row][col]._replace(character=character)

    def update(character):
        pass

    def is_wall(self, col ,row):
        """Checks if board at x, y is Wall"""
        return isinstance(self._arr[row][col], Wall)

    