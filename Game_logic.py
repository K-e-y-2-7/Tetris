'''
main_game_logic.py.
A file that reproduces the main logic of game.  
===============================================

'''

from copy import deepcopy
from random import choice, randrange

from Settings import *

# Determine the shape of the figure through its position coordinates.
# One tupple is one block of figure.
figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, 1), (0, -1), (0, 0), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)]]

# Determine the color and name of figure. 
figures_color = ['#4cc9f0', '#072ac8', '#fb8500', '#ffd500',
                 '#31cb00', '#b100e8', '#ff002b']
figures_name = ['i-fig', 'j-fig', 'l-fig', 'o-fig',
                's-fig', 't-fig', 'z-fig']


figures = [[[x_pos + WIDTH // 2, y_pos + 1, 1, 1] for x_pos, y_pos in fig_pos] for fig_pos in figures_pos]
# Concotinate all data of the figure in one object.
figures_obj = list(zip(figures_name, figures, figures_color)) 

field = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

get_color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
color, next_color = get_color(), get_color()

anim_count, anim_speed, anim_limit = 0, 60, 2000

def get_top() -> list:
    ''' Finction is extraction data from file scores.txt and
        writing them in list top.
        Return list of top players.
    '''

    with open('Scores.txt', 'r') as score_file_r:
        flag = 0  
        top = []
        for line in score_file_r:
            top.append(line[:-1])
            flag += 1
            if flag == 10: break

    return top


def rgb_to_hex(rgb):

    return '#%02x%02x%02x' % rgb


def check_borders():
    if figure[i][0] < 0 or figure[i][0] > WIDTH - 1:
        return False
    elif figure[i][1] > HEIGHT - 1 or field[figure[i][1]][figure[i][0]]:
        return False

    return True


def move_obj(event):
    global rotate, anim_limit, dx
    if event.keysym == 'Up':
        rotate = True
    elif event.keysym == 'Down':
        anim_limit = 100
    elif event.keysym == 'Left':
        dx = -1 
    elif event.keysym == 'Right':
        dx = 1

score, line = 0, 0
top_10 = get_top()
record = int(top_10[0].split(': ')[2])






