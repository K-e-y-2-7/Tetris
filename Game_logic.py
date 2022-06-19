'''
main_game_logic.py.
A file that reproduces the main logic of game.  
===============================================

'''

from copy import deepcopy
from random import choice, randrange

from Models import *
from Settings import *

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]


figures = [[(x + WIDTH // 2, HEIGHT + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
#figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)

field = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

get_color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

def rgb_to_hex(rgb):
        return '#%02x%02x%02x' % rgb

figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
color, next_color = get_color(), get_color()




