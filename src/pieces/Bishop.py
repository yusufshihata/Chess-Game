import piece as piece
class Bishop(piece.Piece):
    def __init__(self,x,y,color):
        super().__init__(x=x, y=y, name='bishop', notation='B', color=color)
        self.texture = super().get_texture()
        self.move_sequence = [[1,1],[1,-1],[-1,1],[-1,-1]]
    
    def movement(self, board):
        valid_squares = []
        for move in self.move_sequence:
            for i in range(1, 8):
                row = self.x + (move[0]*i)
                col = self.y + (move[1]*i)
                if row >= 0 and row < 8 and col >= 0 and col < 8:
                    if board.config[row][col] != '':
                        if board.config[row][col][0] != self.color:
                            valid_squares.append([row, col])
                        break
                    else:
                        valid_squares.append([row, col])
        return valid_squares
