import pygame, os, sys
BOARD_HEIGHT = 600
BOARD_WIDTH = 600

locations = {"pacman": {
                        (1, 0) : [(365, 0, 89, 89), (545, 0, 89, 89)],
                        (0, 1) : [(458, 0, 89, 89), (641, 0, 89, 89)],
                        (-1, 0) : [(0, 0, 75, 89), (173, 0, 88, 88)],
                        (0, -1) : [(77, 0, 89, 89) ,(265, 0, 89, 89)]
                       },
            
            "pink": {
                        (1, 0) : [(1, 0, 86, 89), (94, 0, 86, 89)],
                        (0, 1) : [(188, 0, 86, 89), (282, 0, 86, 89)],
                        (-1, 0) : [(375, 0, 86, 88) ,(470, 0, 86, 89)],
                        (0, -1) : [(564, 0, 86, 89), (658, 0, 86, 89)]
                        
                       }

            
            }

class Game:
    def __init__(self):
        pygame.init()
        # path = os.path.join(os.getcwd(), "data/baz/pacman.png")
        path = os.path.join(os.getcwd(), "data/baz/pacman_pink.png")
        self.screen = pygame.display.set_mode((BOARD_HEIGHT, BOARD_WIDTH))
        image1 = pygame.image.load(path)
        
        path = os.path.join(os.getcwd(), "data/baz/pacman.png")
        image2 = pygame.image.load(path)
        
        self.p = [self.get_character_images("pacman", k, image2, (40, 40)) for k in locations["pacman"].keys()]
        
        
        self.curr = [80,0]
        
        self.screen.blit(self.p[0][0], self.curr)
        self.g = [self.get_character_images("pink", k, image1) for k in locations["pacman"].keys()]
        
        pygame.display.update()
        prev = None
        s = pygame.Surface((40, 40))
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
            i%=80
            pygame.display.update()

    def step(self, i):
        blit = []
        
        self.prev = self.curr.copy()
        blit.append( (self.base_rect, self.prev) )
        
        if i < 20:
            self.curr[0] += self.stepNR
            p = self.p[0]
        elif i < 40:
            self.curr[1] += self.stepNR
            p = self.p[1]
        elif i < 60:
            self.curr[0] -= self.stepNR
            p = self.p[2]
        elif i < 80:
            self.curr[1] -= self.stepNR
            p = self.p[3]
            

        blit.append((p[self.index], self.curr))
        self.index+=1
        self.index%=2
        
        self.screen.blits(blit)
        


g = Game()
g.run()