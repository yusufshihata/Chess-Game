import piece as piece
class Bishop(piece.Piece):
    def __init__(self,x,y,color):
        super().__init__(x=x, y=y, name='bishop', color=color)
        self.texture = super().get_texture()



