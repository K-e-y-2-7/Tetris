'''
Tetris.py.
The main file of game.
======================

'''

import time
from random import randrange

import Exceptions
import gui

get_collor = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256)) 
def rgb_to_hex(rgb):
        return '#%02x%02x%02x' % rgb


try:
    for item in gui.grid:
        #time.sleep(0.3)
        gui.game_screen_canv.itemconfigure(item, fill=rgb_to_hex(get_collor()))

    for item in gui.grid:
        gui.game_screen_canv.itemconfigure(item, fill='')
    gui.ROOT.mainloop()
    
except Exceptions.GameOver:
        ...
except Exceptions.Quit:
    exit()
