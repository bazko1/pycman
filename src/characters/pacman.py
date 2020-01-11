from src.movable import Movable


class Pacman(Movable):
    def __init__(self):
        Movable.__init__(self, 1, 1)
        self.eatenFood = 0
        self.eatenGhost = 0
        self.eatenCherry = 0
        pass

    def step(self):
        newX, newY = super().step()

        if not self.board.is_wall(newX, newY):
            self.x, self.y = newX, newY

        return self.x, self.y
