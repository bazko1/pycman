from src.characters.ghost.ghost import Ghost


class GhostBlue(Ghost):
    def __init__(self):
        self.name = "blue"
        Ghost.__init__(self, 11, 14)
        self.y_vel = -1

    def chase_state_target(self):
        pacman = self.other_movable["pacman"]
        red_ghost = self.other_movable["red"]
        if pacman.vel_x == 0 and pacman.vel_y == -1:
            self.target_x = self.x + (pacman.x - 1 - red_ghost.x) * 2
            self.target_y = self.y + (pacman.y - 1 - red_ghost.y) * 2
        else:
            self.target_x = self.x + (pacman.x + pacman.vel_x - red_ghost.x) * 2
            self.target_y = self.y + (pacman.y + pacman.vel_y - red_ghost.y) * 2
