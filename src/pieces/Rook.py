from piece import *
class Rook(Piece):
    def __init__(self,x,y,color):
        super().__init__(x=x, y=y, name='rook', color=color)
        self.texture = super().get_texture()