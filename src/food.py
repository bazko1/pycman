class Food():
    def __init__(self, is_super=False):
        self.eaten = False
        self.is_super = is_super

    def set_eaten(self):
        self.eaten = True