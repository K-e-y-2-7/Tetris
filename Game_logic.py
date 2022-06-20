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

figures = [[[x_pos + WIDTH // 2, y_pos + 1, 1, 1] for x_pos, y_pos in fig_pos] for fig_pos in figures_pos]
figures_obj = list(zip(figures_name, figures, figures_color))

field = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

anim_count, anim_speed, anim_limit = 0, 60, 2000

try:
    with open('Scores.txt', 'r') as score_file_r:
        flag = 0  
        top_10 = []
        for line in score_file_r:
            top_10.append(line[:-1])
            flag += 1
            if flag == 10: break
except FileNotFoundError:
    with open('Scores.txt', 'w') as score_file_w:
        pass

score = ''
record = int(top_10[0].split(': ')[2])


get_color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
color, next_color = get_color(), get_color()


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def check_borders():
    if figure[i][0] < 0 or figure[i][0] > WIDTH - 1:
        return False
    elif figure[i][1] > HEIGHT - 1 or field[figure[i][1]][figure[i][0]]:
        return False
    return True


