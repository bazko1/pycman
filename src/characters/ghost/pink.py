from src.characters.ghost.ghost import Ghost


class GhostPink(Ghost):
    def __init__(self):
        self.name = "pink"
        Ghost.__init__(self,13,14)
        self.y_vel = -1

    def chase_state_target(self):
        pacman = self.other_movable["pacman"]
        if pacman.vel_x == 0 and pacman.vel_y == -1:
            self.target_x = pacman.x - 3
            self.target_y = pacman.y - 3
        else:
            self.target_x = pacman.x - 3 * pacman.vel_x
            self.target_y = pacman.y - 3 * pacman.vel_y