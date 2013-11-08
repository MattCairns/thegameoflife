import pygame, sys
from pygame.locals import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 10

assert WINDOW_WIDTH % CELL_SIZE == 0, 'Window width mst be a multiple of cell size'
assert WINDOW_HEIGHT % CELL_SIZE == 0, 'Window height mst be a multiple of cell size'

CELL_WIDTH = WINDOW_WIDTH / CELL_SIZE
CELL_HEIGHT = WINDOW_HEIGHT / CELL_SIZE

BLACK = (0,0,0)
WHITE = (255,255,255)
DARK_GRAY = (40,40,40)

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('The Game of Life')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quite()
                sys.exit()
        pygame.display.update()

