import pygame, os, sys
BOARD_HEIGHT = 600
BOARD_WIDTH = 600

locations = {"pacman": {
                        (1, 0) : [(365, 0, 89, 89), (545, 0, 89, 89)],
                        (0, 1) : [(458, 0, 89, 89), (641, 0, 89, 89)],
                        (-1, 0) : [(0, 0, 75, 89), (173, 0, 88, 88)],
                        (0, -1) : [(77, 0, 89, 89) ,(265, 0, 89, 89)]
                       }

            }

class Game:
    def __init__(self):
        pygame.init()
        path = os.path.join(os.getcwd(), "data/baz/pacman.png")
        self.screen = pygame.display.set_mode((BOARD_HEIGHT, BOARD_WIDTH))
        self.image = pygame.image.load(path)
        # self.screen.fill((255,255,255))
        self.c1 = self.get_character_images("pacman", (1, 0))
        self.c2 = self.get_character_images("pacman", (0, 1))
        self.c3 = self.get_character_images("pacman", (-1, 0))
        self.c4 = self.get_character_images("pacman", (0, -1))
        # self.c = c1
        # c = [(surface, (id * 89, 0)) for id, surface in enumerate(c)]
        self.screen.blit(self.c1[1], (0,0))
        self.curr = [0,0]
        pygame.display.update()
        prev = None
        s = pygame.Surface((89, 89))
        s.fill((0, 0, 0))
        self.base_rect = s
        self.prev = []
        self.index = 0
        self.stepNR = 20
    def get_character_images(self, name, velocity):
        return [self.image.subsurface(rect) for rect in locations[name][velocity]]



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
        
        
        # if self.index % 2 ==1:
        self.prev = self.curr.copy()
        blit.append( (self.base_rect, self.prev) )
        
        if i < 20:
            self.curr[0] += self.stepNR
            self.c = self.c1
        elif i < 40:
            self.curr[1] += self.stepNR
            self.c = self.c2
        elif i < 60:
            self.curr[0] -= self.stepNR
            self.c = self.c3
        elif i < 80:
            self.curr[1] -= self.stepNR
            self.c = self.c4
            

        blit.append((self.c[self.index], self.curr))
        self.index+=1
        self.index%=2
        
        self.screen.blits(blit)
        


g = Game()
g.run()