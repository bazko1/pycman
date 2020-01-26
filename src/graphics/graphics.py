import pygame, os
from .defines import part_locations
from collections import namedtuple
from src.characters import characters_factory


FoodConfig = namedtuple('FoodConfig', ['small_size', 'big_size', 'small_offset', 'big_offset'])


# Maze is splitted in base_rect_size rects, should be dividible by 4
base_rect_size = 4 * 6
# Size of main maze
# It can be splited to 28 x 31 base rectangles
BOARD_HEIGHT = 31 * base_rect_size  # 620
BOARD_WIDTH = 28 * base_rect_size # 560

# screen offset for score printing
hOffupset = BOARD_HEIGHT // 8

class Graphics:
    """Graphics class for pacman

       Should initialize all objects needed for used graphics library.
       Implements methods needed for game visualization.
    """

    def __init__(self, characters, board):
        self.characters = characters
        self.board = board
        self.game_over = False
        self.screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT + hOffupset))
        pygame.display.set_caption("pycman")
        # Dictionary key is part name, value is either dictionary velocity : list of surfaces
        # or only list of surfaces, filled using load_characters_animations.
        self.animations = {}
        self.other_images = {}
        self.initialize_maze()

    def initialize_maze(self):
        """Draw initial maze look and characters on it"""
        self.draw_maze()
        self.load_characters_animations()
        for character in ["red", "orange", "pink", "pacman", "blue"]:
            self.draw_character(self.characters[character])

        self.load_other_images()

        self.print_text("score", x = BOARD_WIDTH // 4 - 6 * base_rect_size, y = hOffupset - base_rect_size)
        self.print_text("best", x = BOARD_WIDTH // 2 - 2 * base_rect_size, y = 4)
        self.print_score(0)

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
        small_size = base_rect_size // 4
        big_size = base_rect_size // 2
        small_offset = base_rect_size // 2 - small_size // 2
        self.food_conf = FoodConfig((small_size, small_size), (big_size, big_size), small_offset, base_rect_size // 4)
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
                    # pygame.draw.rect(map_surface, (255, 255, 255), (x * base_rect_size, y * base_rect_size, base_rect_size, base_rect_size), 1)

                    if value == ".":
                        map_surface.blit(food_small, (x * base_rect_size + self.food_conf.small_offset,
                                                      y * base_rect_size + self.food_conf.small_offset))
                    elif value == "o":
                        map_surface.blit(food_big, (x * base_rect_size + self.food_conf.big_offset,
                                                    y * base_rect_size + self.food_conf.big_offset))


        self.screen.blit(map_surface, (0, hOffupset))

    def update(self):
        if not self.game_over:
            for character in ["red", "pacman", "orange", "pink", "blue"]: # TODO: cherry is not implemented yet
                self.draw_character(self.characters[character])

            self.animation_state += 1
            self.animation_state %= 2

        pygame.display.update()

    def load_characters_animations(self):
        """Fills dictionary with surfaces ready for each animation

           Each character has supposedly has 4 types of animations (going left, right, up, down)
        """
        self.character_size = (base_rect_size, base_rect_size)

        # Which animation should we display
        self.animation_state = 0

        # Black rect of base size to redraw character
        self.black_rect = pygame.Surface(self.character_size)
        self.black_rect.fill((0, 0, 0))

        characters =  self.characters.keys()
        characters = ["pacman", "pink", "red", "orange", "blue", "eyes", "scared"] # TODO: cherry is not implemented yet
        locations = part_locations

        for character in characters:
            path = os.path.join(os.getcwd(), f"data/baz/{character}.png")
            surface = pygame.image.load(path)
            if isinstance(locations[character], dict):
                self.animations[character] = {
                location: self.get_character_images(character, location, surface, self.character_size)
                for location in locations[character].keys()}
            else:
                self.animations[character] = self.get_character_images(character, None, surface, self.character_size)

    def load_other_images(self):
        for image in ["numbers",]:
            path = os.path.join(os.getcwd(), f"data/baz/{image}.png")
            surface = pygame.image.load(path)
            self.other_images[image] = self.get_character_images(image, None, surface, (base_rect_size, base_rect_size))

        path = os.path.join(os.getcwd(), f"data/baz/letters.png")
        self.letters = pygame.image.load(path)

    def get_character_images(self, name, velocity, image, resize=None):
        """Returs list of surfaces (animation)

            Args:
                name: key in dictionary with specific parts of image location
                velocity: representation of left, right ..
                image: image to extract subimages from
                resize: tuple (width, height) to resize to after extracting

        """

        data = part_locations[name]

        if velocity is not None:
            data = data[velocity]

        out = [image.subsurface(rect) for rect in data]
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
            if character.name in ["blue", "pink", "orange", "red", "cherry"] \
               and self.board.is_not_eaten_food(*prev):
                small = not self.board.get_element(*prev).is_super
                to_blit += self.redraw_food(*prev, small)
            else:
                to_blit.append((self.black_rect, self.screen_position(*prev)))


        velocity = character.get_velocity()
        if character.is_ghost():
            pacman = self.characters["pacman"]
            if character.is_eaten():
                animation = self.animations["eyes"][velocity]
            elif 20 >= pacman.on_stereoids > 0:
                animation = self.animations["scared"][0:2]
            elif 40 > pacman.on_stereoids > 20:
                animation = self.animations["scared"][2:4]
            else:
                animation = self.animations[character.name][velocity]
        else:
            animation = self.animations[character.name][velocity]

        screen_position = self.screen_position(x, y)
        to_blit.append((animation[self.animation_state], screen_position))
        self.screen.blits(to_blit)

    def redraw_food(self, x, y, small=True):
        to_blit = []
        offset = self.food_conf.small_offset if small else self.food_conf.big_offset
        food = self.food_small if small else self.food_big
        to_blit.append((self.black_rect, self.screen_position(x, y)))
        to_blit.append((food, self.screen_position(x, y, offset)))
        return to_blit


    def print_score(self, score, x = BOARD_WIDTH // 4, y = hOffupset - base_rect_size):
        xoffset = 10

        start_x = x
        numbers = self.other_images["numbers"]
        to_blit = []
        for index, digit in enumerate([int(x) for x in str(score)]):
            pos = (start_x + (base_rect_size + xoffset) * index, y)
            to_blit.append((self.black_rect, pos))
            to_blit.append((numbers[digit], pos))

        self.screen.blits(to_blit)

        pass

    def print_text(self, text, x=0, y=0, size=base_rect_size, offset = 10):
        to_blit = []
        text = text.lower()
        letter_w = self.letters.get_width() // 26
        letter_h = self.letters.get_height()

        for index, letter in enumerate(text):
            num = (ord(letter) - 97) % 26
            rect = (num * letter_w, 0, letter_w, letter_h)
            surface = pygame.transform.scale(self.letters.subsurface(rect), (size, size))

            pos = (x + index * size, y)
            erase = (pygame.transform.scale(self.black_rect, (size, size)), pos)
            to_blit.append(erase)
            to_blit.append((surface, pos))


        self.screen.blits(to_blit)

    def print_game_over(self):
        self.game_over = True
        x, y = self.screen_position(10, 13)
        self.print_text("GAME", x=x, y=y)
        x, y = self.screen_position(15, 13)
        self.print_text("OVER", x=x, y=y)

    def print_best_score(self, score):
        x, y = BOARD_WIDTH // 2 + 3 * base_rect_size , 4
        self.print_score(score, x=x, y=y)
        pygame.display.update()

    def print_pacman_lifes(self, lifes_num , x=None, y=None):
        """Print num of pacman images at desired destination

           Saves last x, y to use for lifes update (see pacman_lifes_minus)
        """
        to_blit = []
        x = BOARD_WIDTH // 4 - 6 * base_rect_size or x
        y = hOffupset // 4 or y
        image = self.animations["pacman"][(1, 0)][0]
        for nr in range(lifes_num):
            cords = (nr * image.get_width() + x, y)
            to_blit.append((image, cords))

        self.lifes_last_cords = list(cords)

        self.screen.blits(to_blit)
        pygame.display.update()

    def pacman_life_minus(self, num=1):
        self.screen.blit(self.black_rect, self.lifes_last_cords)
        self.lifes_last_cords[0] -= self.black_rect.get_width()
