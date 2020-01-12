class Graphics:
    """Graphics class for pacman

       Should initialize all objects needed for used graphics library.
       Implements methods needed for game visualization.
    """
    def __init__(self):
        pass

    def draw_board(self, board):
        """Draw board might be called only once to draw full board"""
        pass

    def draw_character(self, character):
        """Draws character, will access its x, y coordinates"""
        pass

    def redraw_board(self, board, coordinates=None):
        """Redraws full board or specific points on it

           Will be mostly used in case pacman eaten a food on its way.
           Then when it leaves specific field we want to redraw it without food
        """
        pass
