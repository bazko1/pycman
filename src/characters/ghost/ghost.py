from src.movable import Movable


class Ghost(Movable):
    def __init__(self, x: int = None, y: int = None):
        super().__init__(x, y)
        self.target_x = 0
        self.target_y = 0
        self.state = "home"
        # target just outside home
        self.out = (14, 11)

    @staticmethod
    def all_ghost_names():
        return ["blue", "red", "pink", "orange"]

    def eaten_state(self):
        self.state = "eaten"

    def frightened_state(self):
        self.state = "frightened"

    def is_frightened(self):
        return self.state == "frightened"

    def is_eaten(self):
        return self.state == "eaten"

    def chase_state(self):
        self.state = "chase"

    def backward_move(self, x, y):
        return x == 0 and y == -self.y_vel or y == 0 and x == -self.x_vel

    def shortest_path(self, backward=False):
        step_x = [0, 0, 1, -1]
        step_y = [1, -1, 0, 0]
        min_dist = float("inf")
        min_index = 0
        for i in range(len(step_x)):
            if (not self.backward_move(step_x[i], step_y[i]) or backward) and not self.board.is_wall(self.x + step_x[i],
                                                                                                     self.y + step_y[
                                                                                                         i]):
                dist = (self.x + step_x[i] - self.target_x) ** 2 + (self.y + step_y[i] - self.target_y) ** 2
                if dist < min_dist:
                    min_dist = dist
                    min_index = i
        return step_x[min_index], step_y[min_index]

    def set_velocity(self):
        self.x_vel, self.y_vel = self.shortest_path()

    def step(self):
        self.prev_x, self.prev_y = self.x, self.y
        self.set_velocity()

        newX, newY = super().step()

        if not self.board.is_wall(newX, newY): #TODO: should we check for collision? and not self.on_ghost(newX, newY):
            self.x, self.y = newX, newY

        if self.is_in_base():
            self.state = "home"
        elif self.state != "eaten" and self.state != "frightened":
            self.chase_state()

        # Hack to not redraw board
        if self.x in (13, 14) and self.y == 12 and not self.board.is_gate_closed():
            self.y += self.y_vel

    def set_target(self):
        if self.state == "home":
            self.target_x, self.target_y = self.out
        elif self.state == "eaten":
            self.target_x, self.target_y = self.initialX, self.initialY
        elif self.state == "chase":
            self.chase_state_target()
        elif self.state == "frightened":
            self.frightened_state_target()
    def chase_state_target(self):
        return

    def frightened_state_target(self):
        """Sets target to oposite edge of a map where pacman is"""
        pacman = self.other_movable["pacman"]
        XMAX, YMAX = self.board.len_col, self.board.len_row

        center_x, center_y = XMAX//2, YMAX//2

        pacman_x, pacman_y = pacman.getCords()

        self.target_x = 0 if pacman_x >= center_x else XMAX
        self.target_y = 0 if pacman_y >= center_y else YMAX

        pass

    def on_ghost(self, newX, newY):

        # check if ghost do not walk on each other
        for ghost_name in Ghost.all_ghost_names():
            ghost = self.other_movable[ghost_name]
            if ghost == self or ghost.state == "eaten":
                continue

            if (newX == ghost.x and newY == ghost.y) or \
                (newX == ghost.prev_x and newY == ghost.prev_y):
                return True

        return False

    def is_in_base(self):
        return 16 >= self.x >= 11 and 15 >= self.y >= 13

    def set_home(self):
        self.x, self.y = self.initialX, self.initialY