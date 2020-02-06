from src.movable import Movable


class Pacman(Movable):
    STEREOIDS_MAX_TIME = 100

    def __init__(self):
        Movable.__init__(self, 13, 23)
        self.name = "pacman"
        self.x_vel = -1
        self.on_stereoids = 0
        self.eatenFood = 0
        self.eatenSuperFood = 0
        self.eatenGhost = 0
        self.eatenCherry = 0
        self.lifes = 3
        self.spree = 0
        self.ghosts = ["red", "blue", "pink", "orange"]
    def step(self):
        newX, newY = super().step()
        self.prev_x, self.prev_y = self.x, self.y

        if self.board.is_not_eaten_food(self.x, self.y):
            self.eatenFood += 1
            food = self.board.get_element(self.x, self.y)
            food.set_eaten()
            if food.is_super:
                # TODO: Set correct number of steps for pacman to be super
                self.on_stereoids = self.STEREOIDS_MAX_TIME

        if self.on_stereoids > 0:
            for ghost_name in self.ghosts:
                    ghost = self.other_movable[ghost_name]
                    if not ghost.is_eaten():
                        ghost.frightened_state()

        for movable in self.other_movable.values():
            if movable == self:
                continue
            # FIXME: Not sure if this is right but if we check only prev or only actuall
            # cords pacman is sometimes not eaten if moves dynamically
            if self.getCords() == movable.getCords() or \
               self.get_prev() == movable.get_prev():
                if movable.is_ghost():
                    if not movable.is_eaten():
                        if self.on_stereoids > 0:
                            movable.eaten_state()
                            self.spree += 1
                            self.eatenGhost += 1 * self.spree
                        elif not movable.is_eaten():
                            # collision with living ghost and we are not on super food
                            self.die()
                            return

                # TODO: Prepare collision with other movable (cherry)


        if self.on_stereoids != 0:
            self.on_stereoids -= 1
            if self.on_stereoids == 0:
                self.spree = 0
                for ghost_name in self.ghosts:
                    ghost = self.other_movable[ghost_name]
                    if ghost.is_frightened():
                        ghost.chase_state()


        if not self.board.is_wall(newX, newY):
            self.x, self.y = newX, newY

        return self.x, self.y

    def die(self):
        self.x = self.initialX
        self.y = self.initialY
        self.lifes -= 1