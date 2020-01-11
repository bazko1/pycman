from src.movable import Movable


class GhostYellow(Movable):
    def __init__(self):
        Movable.__init__(self, 1, 1)
    def step(self):
        pass