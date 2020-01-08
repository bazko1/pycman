from .wall import Wall
from .food import Food

class Board:
    """Pacman game board"""

    def __init__(self, rows, cols):
        self._board = [[0] * cols] * rows

    @classmethod
    def from_array(cls, arr):
        """Creates empty Board from array of 0 and 1's.

        1 - means that field should be wall object
        0 - walkable space with food - can be normal - can be extra one

        Args:
            arr: array with 0 and 1


        """
        rowN = len(arr)
        colN = len(arr[0])
        board = Board(rowN, colN)
        for row in range(rowN):
            for col in range(colN):
                if arr[row][col] == 1:
                    board._board[row][col] = Wall(col, row)
                else:
                    board._board[row][col] = Food(col, row)
        
        return board

    def set_characters(self, characters):
        """Fills board with characters objects.

        Characters should have x, y coordinates.
        Will iterate over cords and set reference to objects in its array.

        Args:
            characters: array of objects with x, y fields.

        """

        raise NotImplementedError()
