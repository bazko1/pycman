class Field:
    def __init__(self):
        self.x = None
        self.y = None
        pass
    def getCords(self):
        return self.x, self.y

    def setCords(self, cords):
        self.x, self.y = cords