import piece as piece
class Pawn(piece.Piece):
    def __init__(self,x,y,color):
        super().__init__(x=x, y=y, name='pawn', color=color)
        self.texture = super().get_texture()