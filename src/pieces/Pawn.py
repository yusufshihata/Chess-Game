import piece as piece
class Pawn(piece.Piece):
    def __init__(self,x,y,color):
        super().__init__(x=x, y=y, name='pawn', notation='P', color=color)
        self.texture = super().get_texture()
        self.move_sequence = [[0,1], [0,-1]]
        self.has_moved = self.moved()
    
    def movement(self,board):
        valid_squares = []

        if self.color == 'w' and board.config[self.x-1][self.y-1] != '' and board.config[self.x-1][self.y-1][0] == 'b':
            valid_squares.append([self.x-1, self.y-1])
            
        if self.color == 'w' and board.config[self.x-1][self.y+1] != '' and board.config[self.x-1][self.y+1][0] == 'b':
            valid_squares.append([self.x-1, self.y+1])
            
        if self.color == 'b' and board.config[self.x+1][self.y+1] != '' and board.config[self.x+1][self.y+1][0] == 'w':
             valid_squares.append([self.x+1, self.y+1])
            
        if self.color == 'b' and board.config[self.x+1][self.y-1] != '' and board.config[self.x+1][self.y-1][0] == 'w':
             valid_squares.append([self.x+1, self.y-1])

        if self.has_moved:
            if self.color == 'w' and board.config[self.x-1][self.y] == '':
                valid_squares.append([self.x-1, self.y])
                
            if self.color == 'b' and board.config[self.x+1][self.y] == '':
                valid_squares.append([self.x+1, self.y])
        
        else:
            if self.color == 'w':
                for i in range(1,3):
                    if board.config[self.x-i][self.y] == '':
                        valid_squares.append([self.x-i, self.y])
                    else:
                        break
            else:
                for i in range(1,3):
                    if board.config[self.x+i][self.y] == '':
                        valid_squares.append([self.x+i, self.y])
                    else:
                        break
        return valid_squares
    
    def moved(self):
        if (self.color == 'w' and self.x != 6) or (self.color == 'b' and self.x != 1):
            return True
        return False
