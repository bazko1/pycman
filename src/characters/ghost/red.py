from src.movable import Movable


class GhostRed(Movable):
    def __init__(self):
        Movable.__init__(self, 0, 0)
        pass

    def step(self):
        pass