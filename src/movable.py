from abc import ABCMeta, abstractmethod
from .point import Point

class Movable(Point, metaclass=ABCMeta):
    def __init__(self, x = None, y = None):
        Point(self, x, y)
        self.board = None

    def set_board(self, board):
        pass
        self.board = board

    @abstractmethod
    def step(self):
        pass