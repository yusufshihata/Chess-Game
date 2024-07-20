import piece as piece
class Knight(piece.Piece):
    def __init__(self,x,y,color):
        super().__init__(x=x, y=y, name='knight', color=color)
        self.texture = super().get_texture()

