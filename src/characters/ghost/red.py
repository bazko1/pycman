from src.characters.ghost.ghost import Ghost


class GhostRed(Ghost):
    def __init__(self):
        self.name = "red"
        Ghost.__init__(self, 13, 11)
        self.x_vel = -1

    def chase_state_target(self):
        pacman = self.other_movable["pacman"]
        self.target_x = pacman.x
        self.target_y = pacman.y
