from src.movable import Movable
from src.characters.ghost.ghost import Ghost


class GhostOrange(Movable, Ghost):
    def __init__(self):
        self.name = "orange"
        Movable.__init__(self, 15, 14)
        self.y_vel = -1
        Ghost.__init__(self)
    
    def step(self):
        pass
