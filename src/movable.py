from abc import ABCMeta, abstractmethod
from .point import Point

class Movable(Point, metaclass=ABCMeta):
    def __init__(self, x: int = None, y: int = None):
        Point.__init__(self, x, y)
        self.board = None
        self.other_movable = None

    def set_board(self, board: "Board"):
        self.board = board

    def set_other_movable(self, movables: dict):
        """Setter for dict of other movable objects.
        
           Movable objects may interact with each other.
           other_movable list/dict might differ depending on role in game.
           
        Params:
            movables: dict with Movable objects 
            key is their name value is object
        """
        self.other_movable = movables

    @abstractmethod
    def step(self):
        pass