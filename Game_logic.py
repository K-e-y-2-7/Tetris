'''
main_game_logic.py.
A file that reproduces the main logic of game.  
===============================================

'''

from copy import deepcopy
from random import choice, randrange

from Settings import *

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, 1), (0, -1), (0, 0), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)]]
figures_name = ['i-fig', 'j-fig', 'l-fig', 'o-fig', 's-fig', 't-fig', 'z-fig']
figures_color = ['#4cc9f0', '#072ac8', '#fb8500', '#ffd500', '#31cb00', '#b100e8', '#ff002b']
figures = [[(x_pos + WIDTH // 2, y_pos + 1, 1, 1) for x_pos, y_pos in fig_pos] for fig_pos in figures_pos]
figures_obj = list(zip(figures_name, figures, figures_color))

field = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

get_color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

def rgb_to_hex(rgb):
        return '#%02x%02x%02x' % rgb

figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
color, next_color = get_color(), get_color()
