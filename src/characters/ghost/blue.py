from src.movable import Movable
from src.characters.ghost.ghost import Ghost


class GhostBlue(Movable, Ghost):
    def __init__(self):
        self.name = "blue"
        Movable.__init__(self, 11, 14)
        Ghost.__init__(self)

    def step(self):
        pass
