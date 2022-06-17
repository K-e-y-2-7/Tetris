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

# Settings of game interface
CANVAS = tkinter.Canvas(ROOT, width=RES[1], height=RES[0],\
                        bg='purple', highlightthickness=0) 
CANVAS.pack()

name_img_obj = tkinter.PhotoImage(file='img/Tetris_logo.png')
CANVAS.create_image(10, 10, anchor='nw', image=name_img_obj)

CANVAS.create_text(50, 450, text=' Score: \n123456', font=('ProtoSans56', 40),\
                   fill='yellow', anchor='nw')

