from src.movable import Movable


class Pacman(Movable):
    def __init__(self):
        Movable.__init__(self, 13, 23)
        self.name = "pacman"
        self.on_stereoids = 0
        # 10 points
        self.eatenFood = 0
        # 50 points and new behaviour
        self.eatenSuperFood = 0
        self.eatenGhost = 0
        self.eatenCherry = 0

    def step(self):
        newX, newY = super().step()
        self.prev_x, self.prev_y = self.x, self.y

        if self.board.is_not_eaten_food(self.x, self.y):
            self.eatenFood += 1
            food = self.board.get_element(self.x, self.y)
            food.set_eaten()
            if food.is_super:
                # TODO: Set correct number of steps for pacman to be super
                self.on_stereoids = 40

        for movable in self.other_movable.values():
            if movable.is_ghost() and not movable.is_eaten():
                if self.on_stereoids > 0:
                    movable.set_eaten()
                    self.eatenGhost += 1

            self.on_stereoids -= 1
            if self.on_stereoids == 0:
                pass

        if not self.board.is_wall(newX, newY):
            self.x, self.y = newX, newY

        return self.x, self.y
