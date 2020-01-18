from src.movable import Movable


class GhostPink(Movable):
    def __init__(self):
        self.name = "pink"
        Movable.__init__(self, 1, 1)

    def step(self):
        pass
