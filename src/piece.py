import os

class Piece:
    def __init__(self, x, y, color, name=''):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.texture = self.get_texture()
    
    def get_texture(self):
        color = 'white' if self.color == 'w' else 'black'
        return os.path.join('/home/yusuf/code/chess/assets/', f'{color}_{self.name}.png')
    