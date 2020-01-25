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
        self.best_score_file = os.path.join(os.getcwd(), "data/best.txt")
        self.initialize()


    def initialize(self):
        Ghost = characters_factory.new_ghost
        self.board.reset()
        self.game_over = False
        self.started = False
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

        self.score = 0
        self.pacman = self.characters["pacman"]
        self.graphics = Graphics(self.characters, self.board)

        #TODO: Set chase state to ghosts after n seconds
        self.characters["red"].chase_state()

        if not os.path.isfile(self.best_score_file):
            self.best_score = 0
        else:
            f = open(self.best_score_file, "r")
            best_score = f.read().replace("\n", "")
            f.close()
            if best_score.isdigit():
                self.best_score = int(best_score)
            else:
                print('ERROR WHILE READING BEST SCORE!')
                self.best_score = 0

        self.graphics.print_best_score(self.best_score)
        
        self.board.open_gate()

    def step(self):
        """Performs one tick of a game, updating all its objects"""
        for name, character in self.characters.items():
            newCords = character.step()
            if character.is_ghost():
                character.set_target()


        if self.pacman.lifes == 0:
            self.graphics.print_game_over()
            self.game_over = True

        self.update_score()

        self.graphics.update()


    def start(self):
        self.clock = pygame.time.Clock()
        self.main_loop()


    def main_loop(self):
        i = 0
        while True:
            curr = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.started = True
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
                    elif event.key == pygame.K_SPACE and self.game_over:
                        self.restart()

            if self.started and not self.game_over:
                self.clock.tick_busy_loop(5)
                self.step()
                if i < 21:
                    i+=1

                if i == 20:
                    #free another ghost wall y=12, x=13 , 14 dissapear
                    # FIXME: If we open gate not instantly ghost do not leave box
                    # self.board.open_gate()
                    pass

    def restart(self):
        self.initialize()


    def update_score(self):
        """Calculates overall score based upon food pacman ate."""
        pacman = self.pacman
        self.score = 10 * pacman.eatenFood + pacman.eatenSuperFood * 50
        # Current score
        self.graphics.print_score(self.score)
        if self.game_over:
            if self.score > self.best_score:
                f = open(self.best_score_file, 'w')
                f.write(str(self.score))
                f.close()
                self.graphics.print_best_score(self.best_score)


