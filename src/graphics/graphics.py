import pygame, os

BOARD_HEIGHT = 600
BOARD_WIDTH = 600


class ImageSquarer():
    def __init__(self):
        pass
    
    def getSquare(self):
        pass
    

class Graphics:
    """Graphics class for pacman

       Should initialize all objects needed for used graphics library.
       Implements methods needed for game visualization.
    """
    
    def __init__(self):
        
        path = os.path.join(os.getcwd(), "data/1.png")
        image = pygame.image.load(path)
        self.image = image
        rect = image.get_rect()
        
        
        self.screen = pygame.display.set_mode((BOARD_HEIGHT, BOARD_WIDTH))
        pygame.display.set_caption("pycman")
        
        
        # p = self.get_image_square(0, 6, 2)
        # cropRect = (1145, 670, 100, 100)
        # p1 = self.get_image_square(12, 6)
        # p2 = self.get_image_square(13, 6)
        
        # p3 = self.get_image_square(12, 7)
        # p4 = self.get_image_square(13, 7)

        # self.screen.blits( ( (p1,(300,300)), (p2,(347,300)), (p3,(300, 347)), (p4,(347, 347)) ) )
        
        # pacman300 = [(img, (pos[0]+300, pos[1] + 300)) for img, pos in self.get_bigger_image(8,6,2,2)]
        s = pygame.Surface((47 * 2, 47 * 2))
        s.fill((0, 0, 0))
        i1 = ((s, (-47*2,-0)),*self.set_big_image_pos(self.get_bigger_image(8, 6, 2, 2), 0, 0))
        
        i2 = ((s, (0, 0)), *i1)
        i3 = self.set_big_image_pos(self.get_bigger_image(12, 6, 2, 2), 0, 0)
        
        self.update_array = [i1, i3, i2]
        
        # self.update_array += list(map(lambda x: self.set_big_image_pos(x, 47 * 2, 0), self.update_array))
        
        # self.update_array += list(map(lambda x: self.set_big_image_pos(x, 47 * 3, 0), self.update_array))
        
        self.index = 0
        self. xpos = 0

    def update(self):
        self.screen.blits(self.update_array[self.index])
        self.index += 1
        if self.index % len(self.update_array) == 0:
            self.index = 0
            if self.xpos < 5:
                self.update_array = list(map(lambda x: self.set_big_image_pos(x, 47 * 2, 0), self.update_array))
                self.xpos += 1
        pygame.display.update()
        

    def get_image_square(self, x, y):
        base_rect_size = 47
        rect_size = base_rect_size
        cropRect = (x * base_rect_size + 1 + x, y * base_rect_size + 1 + y, rect_size, rect_size)
        return self.image.subsurface(cropRect)

    def get_bigger_image(self, image_x, image_y, w, h) :
        image = []
        x, y = image_x, image_y
        for i in range(w):
            for j in range(h):
                image.append((self.get_image_square(x + i, y + j), (i * 47 ,j * 47)))
        return image
    
    def set_big_image_pos(self, big_image, screen_x, screen_y):
        out_image = [(img, (pos[0] + screen_x, pos[1] + screen_y)) for img, pos in big_image]
        return out_image

    def draw_board(self, board):
        """Draw board might be called only once to draw full board"""
        board.len_row
        board.len_col
        pass

    def draw_character(self, character):
        """Draws character, will access its x, y coordinates"""
        pass

    def redraw_board(self, board, coordinates=None):
        """Redraws full board or specific points on it

           Will be mostly used in case pacman eaten a food on its way.
           Then when it leaves specific field we want to redraw it without food
        """
        pass
