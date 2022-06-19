'''
gui.py.
A file that reproduces the graphical interface.  
===============================================

'''

from PIL import Image, ImageTk

from Settings import *

# Settings of game interface
screen_canv = tkinter.Canvas(ROOT, width=RES[1], height=RES[0],
                        bg='#6C00B5', highlightthickness=0) 
screen_canv.pack()

# The disign of interface
bg_image = Image.open('img/background_img.png').resize((1200, 700))
bg_image = ImageTk.PhotoImage(bg_image)
screen_canv.create_image(0, 0, anchor='nw', image=bg_image)

field_bg_image = Image.open('img/field_background.png').resize((420, 630))
field_bg_image = ImageTk.PhotoImage(field_bg_image)
screen_canv.create_image(415, 60, anchor='nw', image=field_bg_image)

name_img_obj = Image.open('img/Tetris_logo.png').resize((341, 98))
name_img_obj = ImageTk.PhotoImage(name_img_obj)
screen_canv.create_image(30, 10, anchor='nw', image=name_img_obj)

top10_img = Image.open('img/top_ten_image.png').resize((160, 120))
top10_img = ImageTk.PhotoImage(top10_img)
screen_canv.create_image(950, 20, anchor='nw', image=top10_img)


grid = [screen_canv.create_rectangle(x * TILE, y * TILE, x * TILE +
        TILE, y * TILE + TILE) for x in range(WIDTH) for y in range(HIGH)]
for item in grid:
    screen_canv.move(item, 415, 60)

# Creates images of our figures
i_fig = Image.open('img/I_figure.png').resize((47, 185))
j_fig = Image.open('img/J_figure.png').resize((95, 140))
l_fig = Image.open('img/L_figure.png').resize((95, 140))
o_fig = Image.open('img/O_figure.png').resize((93, 93))
s_fig = Image.open('img/S_figure.png').resize((140, 93))
t_fig = Image.open('img/T_figure.png').resize((140, 93))
z_fig = Image.open('img/Z_figure.png').resize((140, 93))

# Displays which figure will be next.
idx = 0

figures = [i_fig, j_fig, l_fig, o_fig, s_fig, t_fig, z_fig]
figure = ImageTk.PhotoImage(figures[idx])
screen_canv.create_image(180, 450, anchor='center', image=figure)


screen_canv.create_text(380, 13, text='BEST RECORD:  123456 ',
                font=('ProtoSans56', 25), fill='purple', anchor='nw')

screen_canv.create_text(35, 155, text='Your nickname: \n ...',
                font=('ProtoSans56', 25), fill='blue', anchor='nw')

screen_canv.create_text(35, 240, text='Score: ...',
                font=('ProtoSans56', 35), fill='orange', anchor='nw')


