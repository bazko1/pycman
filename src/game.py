from .board import Board
from .maps import testMap
from src.characters import characters_factory

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

    self.characters = {"Blue": Ghost("Blue"),
                       "Red": Ghost("Red"),
                       "Pink": Ghost("Pink"),
                       "Yellow": Ghost("Yellow"),
                       "Pacman": characters_factory.Pacman(),
                       "Cherry": characters_factory.Cherry()
                      }

    for c in self.characters.values():
      c.set_board(self.board)
      self.board.set_character(c)
      c.set_other_movable(self.characters)


  def step(self):
    """Performs one tick of a game, updating all its objects"""
    for c in charcters:

        c.step()

        if c == Pacman():
          self.calculateScore(c.getEaten())

    graphics.update()


  def start(self):
    pass