from src.characters.ghost.ghost import Ghost


class GhostBlue(Ghost):
    def __init__(self):
        self.name = "blue"
        Ghost.__init__(self, 11, 14)
        self.y_vel = -1

    def chase_state_target(self):
        pacman = self.other_movable["pacman"]
        red_ghost = self.other_movable["red"]
        if pacman.x_vel == 0 and pacman.y_vel == -1:
            self.target_x = self.x + (pacman.x - 1 - red_ghost.x) * 2
            self.target_y = self.y + (pacman.y - 1 - red_ghost.y) * 2
        else:
            self.target_x = self.x + (pacman.x + pacman.x_vel - red_ghost.x) * 2
            self.target_y = self.y + (pacman.y + pacman.y_vel - red_ghost.y) * 2
