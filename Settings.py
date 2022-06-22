'''
Settings.py.
File containing all constants.  
================================

'''

from tkinter import *
from tkinter import messagebox



TILE = 35  # size of one piece
WIDTH, HEIGHT = 12, 18  # how many such pieces vertically and horizontally
FPS = 80  
GAME_RESS = WIDTH * TILE, HEIGHT * TILE  # game resolution
RES = 700, 1200  # screen resolution

# Settings of window
tetris = Tk()
tetris.title('TETRIS')
tetris.wm_attributes("-topmost", 1)
tetris.geometry(f'{RES[1]}x{RES[0]}')

tetris.resizable(width=False, height=False)

# Settings of game interface
screen_canv = Canvas(tetris, width=RES[1], height=RES[0],
                        bg='#6C00B5', highlightthickness=0)
screen_canv.pack()

# Create a screen to field of game
game_screen_canv = Canvas(tetris, width=WIDTH * TILE + 1,
        height=HEIGHT * TILE + 1, bg='purple', highlightthickness=0)
game_screen_canv.place(x=415, y=60, anchor='nw')

# Create a screen to field of top 10 players
top_10_canv = Canvas(tetris, width=310,
        height=387, bg='purple', highlightthickness=0)
top_10_canv.place(x=865, y=165, anchor='nw')


# Determine the shape of the figure through its position coordinates.
# One tupple is one block of figure.
figures_possition = [[((-1, 0), (-2, 0), (0, 0), (1, 0)), '#4cc9f0', 'i-fig'],
                [((0, 0), (0, -1), (0, 1), (1, -1)), '#072ac8', 'j-fig'],
                [((0, 0), (0, -1), (0, 1), (-1, -1)), '#fb8500', 'l-fig'],
                [((0, -1), (-1, -1), (-1, 0), (0, 0)), '#ffd500', 'o-fig'],
                [((0, 0), (-1, 0), (0, 1), (-1, -1)), '#31cb00', 's-fig'],
                [((0, 0), (0, -1), (0, 1), (-1, 0)), '#b100e8', 't-fig'],
                [((-1, 0), (-1, 1), (0, 0), (0, -1)), '#ff002b', 'z-fig']]


