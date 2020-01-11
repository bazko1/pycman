from src.movable import Movable


class Pacman(Movable):
    def __init__(self):
        Movable.__init__(self, 0, 0)
        self.eatenFood = 0
        self.eatenGhost = 0
        self.eatenCherry = 0
        pass
    
    def step(self):
        pass