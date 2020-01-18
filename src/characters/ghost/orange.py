from src.movable import Movable


class GhostOrange(Movable):
    def __init__(self):
        self.name = "orange"
        Movable.__init__(self, 1, 1)

    def step(self):
        pass
