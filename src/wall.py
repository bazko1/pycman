from .point import Point

class Wall(Point):
    def __init__(self, x = None, y = None):
        Point(x, y)