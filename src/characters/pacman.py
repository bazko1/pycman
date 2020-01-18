from src.movable import Movable


class Pacman(Movable):
    def __init__(self):
        Movable.__init__(self, 13, 23)
        self.name = "pacman"
        self.eatenFood = 0
        self.eatenGhost = 0
        self.eatenCherry = 0

    def step(self):
        newX, newY = super().step()
        self.prev_x, self.prev_y = self.x, self.y
        
        if self.board.is_not_eaten_food(self.x, self.y):
            self.eatenFood += 1
            self.board.get_element(self.x, self.y).set_eaten()

        if not self.board.is_wall(newX, newY):
            self.x, self.y = newX, newY

        return self.x, self.y
