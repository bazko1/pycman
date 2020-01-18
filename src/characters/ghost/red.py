from src.movable import Movable
from src.characters.ghost.ghost import Ghost


class GhostRed(Movable, Ghost):
    def __init__(self):
        self.name = "red"
        Movable.__init__(self, 13, 11) # 13 11
        Ghost.__init__(self)
        self.x_vel = -1

    def step(self):
        pass
