import pygame, os
from .defines import part_locations
from collections import namedtuple
from src.characters import characters_factory


FoodConfig = namedtuple('FoodConfig', ['small_size', 'big_size', 'small_offset', 'big_offset'])
# screen offset for score printing
hOffupset = 80

# Maze is splitted in base_rect_size rects
base_rect_size = 20
# Size of main maze
# It can be splited to 28 x 31 base rectangles
BOARD_HEIGHT = 31 * base_rect_size  # 620
BOARD_WIDTH = 28 * base_rect_size # 560


class Graphics:
    """Graphics class for pacman

       Should initialize all objects needed for used graphics library.
       Implements methods needed for game visualization.
    """

    def __init__(self, characters, board):
        self.characters = characters
        self.board = board
        
        self.screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT + hOffupset))
        pygame.display.set_caption("pycman")
        # Dictionary key is part name, value is either dictionary velocity : list of surfaces 
        # or only list of surfaces, filled using load_characters_animations.
        self.animations = {}
        self.initialize_maze()
        
        

    def initialize_maze(self):
        """Draw initial maze look and characters on it"""
        self.draw_maze()
        self.load_characters_animations()
        for character in ["red", "orange", "pink", "pacman"] : # TODO: Add blue
            self.draw_character(self.characters[character])
        pygame.display.update()

    def draw_maze(self):
        """Load and draw maze image, fill it with food

           Array representation of map will be read and based upon that
           food will be displayed.
        """
        map_path = os.path.join(os.getcwd(), "data/baz/map.jpg")
        map_surface = pygame.image.load(map_path)
        map_surface = pygame.transform.scale(map_surface, (BOARD_WIDTH, BOARD_HEIGHT))

        food_path = os.path.join(os.getcwd(), "data/baz/food.png")
        food_image = pygame.image.load(food_path)
        self.food_conf = FoodConfig((5, 5), (16, 16), 7, 2)
        # TODO: Add food coords to defines
        food_small = pygame.transform.scale(food_image.subsurface((0, 16, 16, 16)), self.food_conf[0])
        food_big = pygame.transform.scale(food_image.subsurface((88, 6, 34, 34)), self.food_conf[1])
        self.food_small = food_small
        self.food_big = food_big

        f = open(os.path.join(os.getcwd(), "data/map.txt"), "r")
        data = f.read().splitlines()
        f.close()
        for y, row in enumerate(data):
                for x, value in enumerate(row):
                    # For debuging draw rects
                    # pygame.draw.rect(map_surface, (255, 255, 255), (x * 20, y * 20, food_image, base_rect_size, base_rect_size), 1)

                    if value == ".":
                        map_surface.blit(food_small, (x * 20 + self.food_conf.small_offset, 
                                                      y * 20 + self.food_conf.small_offset))
                    elif value == "o":
                        map_surface.blit(food_big, (x * 20 + self.food_conf.big_offset,
                                                    y * 20 + self.food_conf.big_offset))


        self.screen.blit(map_surface, (0, hOffupset))

    def update(self):
        self.draw_character(self.characters['pacman'])
        self.animation_state += 1
        self.animation_state %= 2
        pygame.display.update()

    def load_characters_animations(self):
        """Fills dictionary with surfaces ready for each animation
        
           Each character has supposedly has 4 types of animations (going left, right, up, down)
        """
        self.character_size = (26, 26)
        
        # Which animation should we display 
        self.animation_state = 0
        
        # Black rect of base size to redraw character
        self.black_rect = pygame.Surface(self.character_size)
        self.black_rect.fill((0, 0, 0))

        # TODO: Add blue when blue.png ready
        # characters =  self.characters.keys()
        characters = ["pacman", "pink", "red", "orange", ] # "blue"
        locations = part_locations

        for character in characters:
            path = os.path.join(os.getcwd(), f"data/baz/{character}.png")
            surface = pygame.image.load(path)
            self.animations[character] = {
             location: self.get_character_images(character, location, surface, self.character_size) 
             for location in locations[character].keys()}
        
    def get_character_images(self, name, velocity, image, resize=None):
        """Returs list of surfaces (animation)
        
            Args:
                name: key in dictionary with specific parts of image location
                velocity: representation of left, right ..
                image: image to extract subimages from
                resize: tuple (width, height) to resize to after extracting
        
        """
        out = [image.subsurface(rect) for rect in part_locations[name][velocity]]
        if resize is not None:
            out = [pygame.transform.scale(surface, resize) for surface in out]
        return out

    def screen_position(self, x, y, offset=0):
        return (x * base_rect_size + offset, y * base_rect_size + offset + hOffupset)

    def draw_character(self, character):
        """Draws character, will access its x, y coordinates"""
        x, y = character.getCords()
        prev = character.get_prev()
        to_blit = []
        if None not in prev:
            if character.name in ["blue", "pink", "orange", "red", "cherry"]:
                self.redraw_food(*prev)
            else:
                to_blit.append((self.black_rect, self.screen_position(*prev)))
                to_blit.append((self.black_rect, self.screen_position(*prev)))


        velocity = character.get_velocity()
        animation = self.animations[character.name][velocity]
        screen_position = self.screen_position(x, y)
        to_blit.append((animation[self.animation_state], screen_position))
        self.screen.blits(to_blit)

    def redraw_food(self, x, y, small=True):
        to_blit = []
        offset = self.food_conf.small_offset if small else self.food_conf.big_offset
        food = self.food_small
        to_blit.append((self.black_rect, self.screen_position(x, y)))
        to_blit.append((food, self.screen_position(x, y, offset)))
        self.screen.blits(to_blit)


    def redraw_board(self, board, coordinates=None):
        """Redraws full board or specific points on it

           Will be mostly used in case pacman eaten a food on its way.
           Then when it leaves specific field we want to redraw it without food
        """
        pass
