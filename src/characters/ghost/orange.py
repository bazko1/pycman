from src.characters.ghost.ghost import Ghost


class GhostOrange(Ghost):
    def __init__(self):
        self.name = "orange"
        Ghost.__init__(self, 15, 14)
        self.y_vel = -1
        self.r = 10

    def set_radius(self, r):
        self.r = r

    def inside(self):
        pacman = self.other_movable["pacman"]
        return (self.x - pacman.x) ** 2 + (self.y - pacman.y) ** 2 < self.r ** 2


    def chase_state_target(self):
        pacman = self.other_movable["pacman"]
        if not self.inside():
            self.target_x = pacman.x
            self.target_y = pacman.y
        else:
            self.target_x = 0
            self.target_y = len(self.board) + 5
