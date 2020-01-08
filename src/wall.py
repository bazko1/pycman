from .field import Field

class Wall(Field):
    def __init__(self, x = None, y = None):
        Field(x, y)