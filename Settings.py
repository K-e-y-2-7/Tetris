'''
Settings.py.
File containing all constants.  
================================

'''

import tkinter

TILE = 35  # size of one piece
WIDTH, HIGH = 12, 18  # how many such pieces vertically and horizontally
FPS = 80  
GAME_RESS = WIDTH * TILE, HIGH * TILE  # game resolution
RES = 700, 1200  # screen resolution

# Settings of window
ROOT = tkinter.Tk()
ROOT.title('TETRIS')
ROOT.geometry(f'{RES[1]}x{RES[0]}')

#ROOT.resizable(width=False, height=False)

