class Board:
    """Pacman game board"""

    def __init__(self, size):
        self.board = [[]] * size
        raise NotImplementedError()

    @classmethod
    def from_array(cls, arr):
        """Creates empty Board from array of 0 and 1's.

        1 - means that field should be wall object
        0 - walkable space with food - can be normal - can be extra one
        (#TODO Decide if there is some randomnes here or its changed in another method)

        Args:
            arr: array with 0 and 1


        """
        raise NotImplementedError()

    def set_characters(self, characters):
        """Fills board with characters objects.

        Characters should have x, y coordinates.
        Will iterate over cords and set reference to objects in its array.

        Args:
            characters: array of objects with x, y fields.

        """

        raise NotImplementedError()
