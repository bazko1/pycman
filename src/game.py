from .board import Board
from .maps import TEST_MAP
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

        self.board = Board.from_array(TEST_MAP)

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

        #TODO: Remove - test if pacman walks correctly right and stops on wall
        self.characters["Pacman"].x_vel = 1

    def step(self):
        """Performs one tick of a game, updating all its objects"""
        for name, character in self.characters.items():

            newCords = character.step()
            if name == "Pacman":
                print('pacman new x,y = ', newCords)
                self.calculate_score(character)

      # graphics.update()


    def start(self):
        for i in range(5): #This loop will be changed for while this is for inital tests
            self.step()

            # temporary until we do not use graphics lib yet
            import time
            time.sleep(1)


    def calculate_score(self, pacman):
        """Calculates overall score based upon food pacman ate."""
        #TODO:
        pass
