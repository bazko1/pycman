class Field:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y
    
    def getCords(self):
        return self.x, self.y

    def setCords(self, cords):
        self.x, self.y = cords