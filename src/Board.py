from Constants import *
from Square import Square


class Board:
    def __init__(self, surface):
        self.config = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP']
            ]
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        self.turn = 'white'
        self.surface = surface
        self.configure()
    
    def configure(self):
        for row in range(8):
            for col in range(8):
                self.squares[row][col] = Square(row, col, self.surface)
    