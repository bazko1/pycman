from .board import Board
from .maps import testMap
import src.characters

class Game:
  """Class joining game logic and graphics. Started should output fully playable game.
    
  Attributes:
    board:
    characters:
    graphics:
    points:

  """
  def __init__(self):
    self.board = Board.from_array(testMap)
    
    # self.characters = [Ghost('blue'), Ghost('red'),  Pacman()]
    # m.setCharacters(characters)
    
    # for c in characters:
    #   c.setChars(characters)
    #   c.setMap(m)
    
    # self.graphics = Graphics(m)
    # self.points = 0 
    
    # raise NotImplementedError()
    
  def step(self):
    """Performs one tick of a game, updating all its objects"""
    for c in charcters:
        c.step()
        if c == Pacman():
          self.calculateScore(c.getEaten())
        
    graphics.update()
    
    raise NotImplementedError()
  
  def start(self):
    pass