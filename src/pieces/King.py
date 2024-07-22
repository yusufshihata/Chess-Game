import piece as piece
class King(piece.Piece):
    def __init__(self,x,y,color):
        super().__init__(x=x, y=y, name='king', color=color)
        self.texture = super().get_texture()
        self.move_sequence = [[1,1],[1,-1],[-1,1],[-1,-1],[1,0], [0,1], [-1, 0], [0,-1]]
    
    def movement(self):
        valid_squares = []
        for move in self.move_sequence:
            if self.x + move[0] < 8 and self.x + move[0] >= 0 and self.y + move[1] < 8 and self.y + move[1] >= 0:
                valid_squares.append([self.x+move[0], self.y+move[1]])
        return valid_squares