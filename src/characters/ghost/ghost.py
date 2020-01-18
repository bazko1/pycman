class Ghost:
    def __init__(self):
        self.state = "chasing" # TODO: List possible frightened, eaten, closed ?
        pass

    def step(self):
        # TODO: Running away could be implemented here
        # TODO: Beeing eaten by pacman and going back to base
        # could be here
        pass
    
    def is_eaten(self):
        return self.state == "eaten"
    
    def set_eaten(self):
        self.state = "eaten"