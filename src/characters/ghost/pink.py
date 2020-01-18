from src.movable import Movable
from src.characters.ghost.ghost import Ghost


class GhostPink(Movable, Ghost):
    def __init__(self):
        self.name = "pink"
        Movable.__init__(self, 13, 14)
        Ghost.__init__(self)
        self.y_vel = -1

    def step(self):
        pass
