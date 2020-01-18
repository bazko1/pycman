from .board import Board
from .maps import TEST_MAP
from .graphics.graphics import Graphics
from src.characters import characters_factory
import pygame
import time

class Game:
    """Class joining game logic and graphics. Started should output fully playable game.

    Attributes:
      board:
      characters:
      graphics:
      points:

    """
    def __init__(self):

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

    def step(self):
        """Performs one tick of a game, updating all its objects"""
        for name, character in self.characters.items():

            newCords = character.step()
            if name == "Pacman":
                print('pacman new x,y = ', newCords)
                self.calculate_score(character)

      # graphics.update()


    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((240, 180))
        while True:
            self.characters["Pacman"].x_vel = 0
            self.characters["Pacman"].y_vel = 0
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                self.characters["Pacman"].x_vel = 0
                self.characters["Pacman"].y_vel = 1
            elif keys[pygame.K_DOWN]:
                self.characters["Pacman"].x_vel = 0
                self.characters["Pacman"].y_vel = -1
            elif keys[pygame.K_LEFT]:
                self.characters["Pacman"].x_vel = -1
                self.characters["Pacman"].y_vel = 0
            elif keys[pygame.K_RIGHT]:
                self.characters["Pacman"].x_vel = 1
                self.characters["Pacman"].y_vel = 0

            time.sleep(0.5)
            self.step()


    def calculate_score(self, pacman):
        """Calculates overall score based upon food pacman ate."""
        #TODO:
        pass
