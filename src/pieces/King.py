import piece as piece
class King(piece.Piece):
    def __init__(self,x,y,color):
        super().__init__(x=x, y=y, name='king', color=color)
        self.texture = super().get_texture()