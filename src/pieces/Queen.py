import piece as piece
class Queen(piece.Piece):
    def __init__(self,x,y,color):
        super().__init__(x=x, y=y, name='queen', color=color)
        self.texture = super().get_texture() 

