import piece as piece
class Queen(piece.Piece):
    def __init__(self,x,y,color):
        super().__init__(x=x, y=y, name='queen', notation='Q', color=color)
        self.texture = super().get_texture()
        self.move_sequence = [[1,1],[1,-1],[-1,1],[-1,-1],[1,0], [0,1], [-1, 0], [0,-1]]
    
    def movement(self):
        valid_squares = []
        for move in self.move_sequence:
            for i in range(8):
                if self.x + (move[0]*i) < 8 and self.x + (move[0]*i) >= 0 and self.y + (move[1]*i) < 8 and self.y + (move[1]*i) >= 0:
                    valid_squares.append([self.x+(move[0]*i), self.y+(move[1]*i)])
        return valid_squares
