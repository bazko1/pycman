import pygame, sys
from .board import Board
from .maps import TEST_MAP
from .graphics.graphics import Graphics
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

        pygame.init()
        self.graphics = Graphics()

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
        self.fps = 4 # frames/second
        


    def step(self):
        """Performs one tick of a game, updating all its objects"""
        for name, character in self.characters.items():

            newCords = character.step()
            if name == "Pacman":
                self.calculate_score(character)

        self.graphics.update()


    def start(self):
        self.clock = pygame.time.Clock()
        while True:
            curr = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.step()
            self.clock.tick_busy_loop(15)


    def calculate_score(self, pacman):
        """Calculates overall score based upon food pacman ate."""
        #TODO:
        pass
