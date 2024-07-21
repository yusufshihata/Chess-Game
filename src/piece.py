import pygame
import os
from Constants import *

class Piece:
    def __init__(self, x, y, color, name=''):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.texture = self.get_texture()
        self.texture_rect = self.get_texture_rect()
    
    def get_texture(self):
        color = 'white' if self.color == 'w' else 'black'
        return pygame.image.load(os.path.join('/home/yusuf/code/chess/assets/', f'{color}_{self.name}.png'))
    
    def get_texture_rect(self):
        col, row = (self.y, self.x)
        imgcenter = col*SIZE+SIZE//2,row*SIZE+SIZE//2
        return self.texture.get_rect(center=imgcenter)
    