from src.movable import Movable


class Cherry(Movable):
    """Representing cherry running on map for pacman to eat"""
    def __init__(self):
        Movable.__init__(self, 1, 1)
        self.name = "cherry"

    def step(self):
        pass
