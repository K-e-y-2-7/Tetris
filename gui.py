'''
gui.py.
A file that reproduces the graphical interface.  
===============================================

'''

from PIL import Image, ImageTk

from Settings import *

# Settings of game interface
canvas = tkinter.Canvas(ROOT, width=RES[1], height=RES[0],
                        bg='#6C00B5', highlightthickness=0) 
canvas.pack()

# The disign of interface
bg_image = Image.open('img/background_img.png').resize((1280, 720))
bg_image = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, anchor='nw', image=bg_image)

field_bg_image = Image.open('img/field_background.png').resize((420, 630))
field_bg_image = ImageTk.PhotoImage(field_bg_image)
canvas.create_image(495, 80, anchor='nw', image=field_bg_image)

name_img_obj = tkinter.PhotoImage(file='img/Tetris_logo.png')
canvas.create_image(50, 40, anchor='nw', image=name_img_obj)


top10_img = tkinter.PhotoImage(file='img/top_ten_image.png').subsample(2, 2)
canvas.create_image(1000, 15, anchor='nw', image=top10_img)


grid = [canvas.create_rectangle(x * TILE, y * TILE, x * TILE +
        TILE, y * TILE + TILE) for x in range(WIDTH) for y in range(HIGH)]
for item in grid:
    canvas.move(item, 495, 80)

# Creates images of our figures
i_fig = Image.open('img/I_figure.png').resize((47, 185),)
j_fig = Image.open('img/J_figure.png').resize((95, 140),)
l_fig = Image.open('img/L_figure.png').resize((95, 140),)
o_fig = Image.open('img/O_figure.png').resize((93, 93),)
s_fig = Image.open('img/S_figure.png').resize((140, 93),)
t_fig = Image.open('img/T_figure.png').resize((140, 93),)
z_fig = Image.open('img/Z_figure.png').resize((140, 93),)

# Displays which figure will be next.
def next_figure(idx):  
    figures = [i_fig, j_fig, l_fig, o_fig, s_fig, t_fig, z_fig]
    figure = ImageTk.PhotoImage(figures[idx])

    return figure


canvas.create_image(220, 300, anchor='center', image=next_figure(1))


canvas.create_text(490, 6, text='Record: ... ', font=('ProtoSans56', 35),
                   fill='#7802c2', anchor='nw', )

canvas.create_text(20, 450, text='Your nickname: \n ...', font=('ProtoSans56', 33),
                   fill='orange', anchor='nw')

canvas.create_text(20, 568, text='Score: ...', font=('ProtoSans56', 35),
                   fill='lime', anchor='nw')

canvas.mainloop()
