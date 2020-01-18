import pygame, os, sys
hOffupset = 80
BOARD_HEIGHT = 620
BOARD_WIDTH = 560
# h=31 x w=28
# 20 x 20
# h=620 x w=560
locations = {
            "pacman": {
                        (1, 0) : [(365, 0, 89, 89), (545, 0, 89, 89)],
                        (0, 1) : [(458, 0, 89, 89), (641, 0, 89, 89)],
                        (-1, 0) : [(0, 0, 75, 89), (173, 0, 88, 88)],
                        (0, -1) : [(77, 0, 89, 89) ,(265, 0, 89, 89)]
                       },

            "pink": {
                        (1, 0) :  [(1, 0, 86, 89),   (94, 2, 86, 89)],
                        (0, 1) :  [(188, 0, 86, 89), (282, 2, 86, 89)],
                        (-1, 0) : [(375, 0, 86, 88), (470, 2, 86, 89)],
                        (0, -1) : [(564, 0, 86, 89), (661, 2, 86, 89)]

                    },

            "red": {
                        (1, 0) :  [(1, 0, 86, 89),   (94, 2, 86, 89)],
                        (0, 1) :  [(188, 0, 86, 89), (282, 2, 86, 89)],
                        (-1, 0) : [(375, 0, 86, 88), (470, 2, 86, 89)],
                        (0, -1) : [(564, 0, 86, 89), (661, 2, 86, 89)]

                    },

            "orange": {
                        (1, 0) :  [(1, 0, 85, 88),   (94, 0, 85, 88)],
                        (0, 1) :  [(188, 0, 85, 88), (282, 0, 85, 88)],
                        (-1, 0) : [(375, 0, 85, 88), (470, 0, 85, 88)],
                        (0, -1) : [(564, 0, 85, 88), (658, 0, 85, 88)]

                    },

            "blue": {},

            "wall": [(0, 0, 92, 94), (116, 4, 47, 88)]

            }



class Game:
    def __init__(self):
        pygame.init()
        # path = os.path.join(os.getcwd(), "data/baz/pacman.png")
        color = "pink"
        # path = os.path.join(os.getcwd(), f"data/baz/pacman_{color}.png")
        self.screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT + hOffupset))
        # image1 = pygame.image.load(path)

        path = os.path.join(os.getcwd(), "data/baz/pacman.png")
        image2 = pygame.image.load(path)

        self.draw_map()

        # self.p = [self.get_character_images("pacman", k, image2, (40, 40)) for k in locations["pacman"].keys()]
        self.p = [self.get_character_images("pacman", k, image2, (26, 26)) for k in locations["pacman"].keys()]


        self.curr = [20, hOffupset + 20]

        self.screen.blit(self.p[0][0], self.curr)
        # self.g = [self.get_character_images("pink", k, image1) for k in locations["pacman"].keys()]

        pygame.display.update()
        prev = None
        s = pygame.Surface((26, 26))
        s.fill((0, 0, 0))
        self.base_rect = s
        self.prev = []
        self.index = 0
        self.stepNR = 20


    def get_character_images(self, name, velocity, image, resize=None):
        out = [image.subsurface(rect) for rect in locations[name][velocity]]
        if resize is not None:
            out = [pygame.transform.scale(surface, resize) for surface in out]
        return out

    def draw_map(self):


        base_rect_size = (20, 20)
        path = os.path.join(os.getcwd(), "data/baz/map.jpg")
        image = pygame.image.load(path)
        # map_surface = pygame.transform.scale(image.subsurface((0, 0, *image.get_size() )), (BOARD_WIDTH, BOARD_HEIGHT))
        map_surface = pygame.transform.scale(image, (BOARD_WIDTH, BOARD_HEIGHT))
        
        path = os.path.join(os.getcwd(), "data/baz/food.png")
        image = pygame.image.load(path)
        food_surf = pygame.transform.scale(image.subsurface((0, 16, 16, 16)), (5, 5))
        food_big = pygame.transform.scale(image.subsurface((88, 6, 34, 34)), (16, 16))

        f = open(os.path.join(os.getcwd(), "data/map.txt"), "r")
        data = f.read().splitlines()

        

        for y, row in enumerate(data):
                for x, value in enumerate(row):
                    # pygame.draw.rect(map_surface, (255, 255, 255), (x * 20, y * 20, *base_rect_size), 1)
                    if value == ".":
                        map_surface.blit(food_surf, (x * 20 + 7, y * 20 + 7))
                    elif value == "o":
                        map_surface.blit(food_big, (x * 20 + 2, y * 20 + 2))

        
        self.screen.blit(map_surface, (0, hOffupset))
        

    def run(self):
        self.clock = pygame.time.Clock()
        i = 0

        while True:
            self.clock.tick_busy_loop(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.step(i)
            i+=1
            i%=30
            pygame.display.update()

    def step(self, i):
        blit = []
        # return
        self.prev = self.curr.copy()
        blit.append( (self.base_rect, self.prev) )

        if i < 11:
            self.curr[0] += self.stepNR
            p = self.p[0]
        elif i < 15:
            self.curr[1] += self.stepNR
            p = self.p[1]
        elif i < 26:
            self.curr[0] -= self.stepNR
            p = self.p[2]
        elif i < 30:
            self.curr[1] -= self.stepNR
            p = self.p[3]


        blit.append((p[self.index], self.curr))
        self.index+=1
        self.index%=2

        self.screen.blits(blit)



g = Game()
g.run()