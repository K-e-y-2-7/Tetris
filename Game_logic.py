'''
main_game_logic.py.
A file that reproduces the main logic of game.  
===============================================

'''

from copy import deepcopy
from random import choice, randrange

from Settings import *
from Models import Figure

field = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

get_collor = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256)) 
def rgb_to_hex(rgb):
        return '#%02x%02x%02x' % rgb


