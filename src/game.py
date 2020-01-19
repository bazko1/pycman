import pygame, sys, os
from .board import Board
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

        maze = os.path.join(os.getcwd(), "data/map.txt")
        self.board = Board.from_file(maze)
        
        Ghost = characters_factory.new_ghost

        self.characters = {"blue": Ghost("Blue"),
                           "red": Ghost("Red"),
                           "pink": Ghost("Pink"),
                           "orange": Ghost("Orange"),
                           "pacman": characters_factory.Pacman(),
                           "cherry": characters_factory.Cherry()
                          }

        for c in self.characters.values():
            c.set_board(self.board)
            c.set_other_movable(self.characters)

        #TODO: Remove - test if pacman walks correctly right and stops on wall
        self.characters["pacman"].x_vel = 1

        self.graphics = Graphics(self.characters, self.board)


    def step(self):
        """Performs one tick of a game, updating all its objects"""
        for name, character in self.characters.items():

            newCords = character.step()
            if name == "pacman":
                # print('pacman x, y',self.characters["pacman"].getCords())
                self.calculate_score(character)

        self.graphics.update()


    def start(self):
        self.clock = pygame.time.Clock()
        started = False
        while True:
            curr = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    started = True
                    if event.key == pygame.K_LEFT:
                        self.characters["pacman"].x_vel = -1
                        self.characters["pacman"].y_vel = 0
                    elif event.key == pygame.K_RIGHT:
                        self.characters["pacman"].x_vel = 1
                        self.characters["pacman"].y_vel = 0
                    elif event.key == pygame.K_DOWN:
                        self.characters["pacman"].x_vel = 0
                        self.characters["pacman"].y_vel = 1
                    elif event.key == pygame.K_UP:
                        self.characters["pacman"].x_vel = 0
                        self.characters["pacman"].y_vel = -1
            if started:
                self.clock.tick_busy_loop(7)
                self.step()
            


    def calculate_score(self, pacman):
        """Calculates overall score based upon food pacman ate."""
        #TODO:
        pass
