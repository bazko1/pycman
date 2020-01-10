from .board import Board
from .maps import testMap
from src.characters import characters_factory
import src.characters.pacman as pacman_

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
    Ghost = characters_factory.new_ghost
    pacman = pacman_.Pacman()
    self.characters = [Ghost('Blue'), Ghost('Red'),
                       Ghost('Pink'), Ghost('Yellow'),
                       pacman]

    # self.board.set_characters()

    for c in self.characters:
      c.set_board(self.board)

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