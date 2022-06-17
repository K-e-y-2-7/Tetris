'''
Settings.py.
File containing all constants.  
================================

'''

import tkinter

TILE = 45  # size of one piece
WIDE, HIGH = 10, 20  # how many such pieces vertically and horizontally
FPS = 80  
GAME_RESS = WIDE * TILE, HIGH * TILE  # game resolution
RES = 720, 1280  # screen resolution

# Settings of window
ROOT = tkinter.Tk()
ROOT.title('TETRIS')
ROOT.geometry(f'{RES[1]}x{RES[0]}')

#ROOT.resizable(width=False, height=False)

