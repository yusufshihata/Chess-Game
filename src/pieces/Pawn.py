import piece as piece
class Pawn(piece.Piece):
    def __init__(self,x,y,color):
        super().__init__(x=x, y=y, name='pawn', notation='P', color=color)
        self.texture = super().get_texture()
        self.move_sequence = [[0,1], [0,-1]]
        self.has_moved = False
    
    def movement(self,board):
        valid_squares = []
        if self.has_moved:
            if self.color == 'w':
                valid_squares.append([self.x-1, self.y])
            else:
                valid_squares.append([self.x+1, self.y])
        else:
            if self.color == 'w':
                valid_squares.append([self.x-1, self.y])
                valid_squares.append([self.x-2, self.y])
            else:
                valid_squares.append([self.x+1, self.y])
                valid_squares.append([self.x+2, self.y])
        return valid_squares