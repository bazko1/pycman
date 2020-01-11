from src.movable import Movable


class Cherry(Movable):
    """Representing cherry running on map for pacman to eat"""
    def __init__(self):
        Movable.__init__(self, 0, 0)

    def step(self):
        pass