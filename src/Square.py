import pygame
from Constants import *

class Square:
    def __init__(self, x , y, surface, piece=None):
        self.x = x
        self.y = y
        self.pos_x = x * SIZE
        self.pos_y = y * SIZE
        self.rect = (self.pos_x, self.pos_y, SIZE, SIZE)
        self.color = LIGHT if (self.x+self.y) % 2 == 0 else DARK
        self.piece = piece
        self.coordinate = self.get_coordinates()
        self.draw(surface)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.rect))
    

    def get_coordinates(self):
        files = 'abcdefgh'
        return files[self.x] + str(8-self.y)

    def occupyed(self):
        return self.piece != None
    