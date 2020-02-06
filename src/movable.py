from abc import ABCMeta, abstractmethod
from .point import Point


class Movable(Point, metaclass=ABCMeta):
    def __init__(self, x: int = None, y: int = None):
        Point.__init__(self, x, y)
        self.initialX = x
        self.initialY = y
        self.x_vel = 0
        self.y_vel = 0
        self.prev_x = None
        self.prev_y = None
        self.prev_x_vel = None
        self.prev_y_vel = None
        self.board = None
        self.other_movable = None

    def set_board(self, board: "Board"):
        self.board = board

    def set_other_movable(self, movables: dict):
        """Setter for dict of other movable objects.

           Movable objects may interact with each other.
           other_movable list/dict might differ depending on role in game.

        Params:
            movables: dict with Movable objects
            key is their name value is object
        """
        self.other_movable = movables

    @abstractmethod
    def step(self):
        """Make one time step.

           Overridden method can return of this abstaction
           which simply adds velocity to current positon.

        """
        newX, newY = self.x + self.x_vel, self.y + self.y_vel
        if newX == self.board.len_col:
            newX = 0
        elif newX == -1:
            newX = self.board.len_col - 1

        return newX, newY

    def get_velocity(self):
        return self.x_vel, self.y_vel

    def hitsWall(self, x, y):
        """Checks if """
        pass

    def is_ghost(self):
        return self.name in ["blue", "red", "pink", "orange"]

    def get_prev(self):
        return self.prev_x, self.prev_y

    def set_velocity(self, velocity):
        self.prev_x_vel, self.prev_y_vel = self.get_velocity()
        self.x_vel, self.y_vel = velocity

    def has_tail(self):
        """Checks if other character is not right behind this"""
        for movable in self.other_movable.values():

            if movable.x == self.prev_x and movable.y == self.prev_y:
                if movable == self:
                    return False
                return True

        return False