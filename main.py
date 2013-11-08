import pygame, sys
import random
from pygame.locals import *

FPS = 20

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 5

assert WINDOW_WIDTH % CELL_SIZE == 0, 'Window width mst be a multiple of cell size'
assert WINDOW_HEIGHT % CELL_SIZE == 0, 'Window height mst be a multiple of cell size'

CELL_WIDTH = WINDOW_WIDTH / CELL_SIZE
CELL_HEIGHT = WINDOW_HEIGHT / CELL_SIZE

BLACK = (0, 0, 0)
DARK_GRAY = (40, 40, 40)
GREEN = (0, 250, 0)


def draw_grid():
    """Draws the virtual and horizontal lines that make up the grid"""
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(DISPLAYSURF, DARK_GRAY, (x,0), (x,WINDOW_HEIGHT))

    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(DISPLAYSURF, DARK_GRAY, (0,y), (WINDOW_WIDTH, y))


def blank_grid():
    """Creates a blank dictionary of items in the grid"""
    grid_dict = {}
    for y in range(CELL_HEIGHT):
        for x in range(CELL_WIDTH):
            grid_dict[x,y] = 0

    return grid_dict


def random_starting_grid(life_dict):
    for item in life_dict:
        life_dict[item] = random.randint(0,1)

    return life_dict


def colour_grid(item, life_dict):
    x = item[0]
    y = item[1]
    x *= CELL_SIZE
    y *= CELL_SIZE

    if life_dict[item] == 0:
        pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, CELL_SIZE, CELL_SIZE))

    if life_dict[item] == 1:
        pygame.draw.rect(DISPLAYSURF, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

    return None


def get_neighbours(item, life_dict):
    neighbours = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            check_cell = (item[0] + x, item[1] + y)
            if check_cell[0] < CELL_WIDTH and check_cell[0] >= 0:
                if check_cell[1] < CELL_HEIGHT and check_cell[1] >= 0:

                    if life_dict[check_cell] == 1:
                        if x == 0 and y == 0:
                            neighbours += 0
                        else:
                            neighbours += 1

    return neighbours


def tick(life_dict):
    new_tick = {}
    for item in life_dict:
        n_neighbours = get_neighbours(item, life_dict)
        if life_dict[item] == 1:

            if n_neighbours < 2:
                new_tick[item] = 0
            elif n_neighbours > 3:
                new_tick[item] = 0
            else:
                new_tick[item] = 1
        elif life_dict[item] == 0:
            if n_neighbours == 3:
                new_tick[item] = 1
            else:
                new_tick[item] = 0

    return new_tick

def main():
    pygame.init()
    global DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('The Game of Life')
    DISPLAYSURF.fill(BLACK)

    life_dict = blank_grid()  # Creates dictionary of blank life
    life_dict = random_starting_grid(life_dict)  # Assign random life to the grid
    for item in life_dict:
        colour_grid(item, life_dict)

    draw_grid()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        life_dict = tick(life_dict)

        for item in life_dict:
            colour_grid(item, life_dict)

        draw_grid()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()