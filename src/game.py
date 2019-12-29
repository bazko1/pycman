class Game:
  """Class joining game logic and graphics. Started should output fully playable game.
    
  Attributes:
    board:
    characters:
    graphics:
    points:

  """
  def __init__(self):
    #TODO:
    self.board = Board()
    self.characters = [Ghost('blue'), Ghost('Red'), Pacman()]
    m.setMap([[]]) # create wall object from 0,1 array in size of map
    # 1 - means wall 
    # 0 - walkable space with food - can be normal - can be extra one 
    
    m.setCharacters(characters)
    
    for c in characters:
      c.setChars(characters)
      c.setMap(m)
    
    self.graphics = Graphics(m)
    self.points = 0 
    
    raise NotImplementedError()
    
    def step(self):
        """Performs one tick of a game, updating all its objects"""
        for c in charcters:
            c.step()
            if c == Pacman():
            self.calculateScore(c.getEaten())
            
        graphics.update()
        
        raise NotImplementedError()