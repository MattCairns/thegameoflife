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

def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(DISPLAYSURF, DARK_GRAY, (x,0), (x,WINDOW_HEIGHT))

    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(DISPLAYSURF, DARK_GRAY, (0,y), (WINDOW_WIDTH, y))

def main():
    pygame.init()
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('The Game of Life')
    DISPLAYSURF.fill(WHITE)

    draw_grid()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        draw_grid()
        pygame.display.update()


if __name__ == '__main__':
    main()