import pygame
import sys

# Define some Constants
ASPECT = 720
FPS = 144
BLUE = (1, 122, 235)
WHITE = (255, 255, 255)
BLOCK = 90


# Setup the Pygame screen
pygame.init()
SCREEN = pygame.display.set_mode((ASPECT, ASPECT))
CLOCK = pygame.time.Clock()
SCREEN.fill(WHITE)

# The main function
def main():
    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.flip()
        CLOCK.tick(FPS)

        pygame.display.update()



# Draw the Chess Grid
def drawGrid():
    is_white = False # Check the color of the square
    for x in range(0, ASPECT, BLOCK):
        is_white = True if not is_white else False
        for y in range(0, ASPECT, BLOCK):
            rect = pygame.Rect(x,y,BLOCK,BLOCK)
            if is_white:
                pygame.draw.rect(SCREEN, WHITE, rect)
                is_white = False
            else:
                pygame.draw.rect(SCREEN, BLUE, rect)
                is_white = True

main()
