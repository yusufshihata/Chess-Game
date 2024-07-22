import pygame
from  Constants import *

class Dragger:
    def __init__(self):
        self.init_x = 0.0
        self.init_y = 0.0
        self.mouseX = 0.0
        self.mouseY = 0.0
        self.piece = None
        self.dragging = False
        self.valid_moves = []
    
    def save_initial(self, pos):
        self.init_x, self.init_y = pos

    def update_pos(self, pos):
        self.mouseX, self.mouseY = pos
    
    def drag_piece(self):
        if self.dragging:
            self.piece.x , self.piece.y = (self.mouseY//SIZE, self.mouseX//SIZE)
    
    def blit_piece(self, surface):
        piece = self.piece
        
        img = piece.texture
        imgcenter = piece.get_texture_rect()
        
        surface.blit(img, imgcenter)
