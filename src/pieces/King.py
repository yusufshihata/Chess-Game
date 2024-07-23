import piece as piece
class King(piece.Piece):
    def __init__(self,x,y,color):
        super().__init__(x=x, y=y, name='king', notation='K', color=color)
        self.texture = super().get_texture()
        self.move_sequence = [[1,1],[1,-1],[-1,1],[-1,-1],[1,0], [0,1], [-1, 0], [0,-1]]
    
    def movement(self,board):
        valid_squares = []
        for move in self.move_sequence:
            row = self.x + move[0]
            col = self.y + move[1]
            if row < 8 and row >= 0 and col < 8 and col >= 0:
                if board.config[row][col] != '':
                    if board.config[row][col][0] == self.color:
                        continue
                    else:
                        valid_squares.append([row, col])
                else:
                    valid_squares.append([row, col])
        return valid_squares