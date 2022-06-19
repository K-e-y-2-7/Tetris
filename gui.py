'''
gui.py.
A file that reproduces the graphical interface.  
===============================================

'''

from email.mime import image
from PIL import Image, ImageTk

from Game_logic import *

# Settings of game interface
screen_canv = tkinter.Canvas(ROOT, width=RES[1], height=RES[0],
                        bg='#6C00B5', highlightthickness=0)
screen_canv.pack()

# Create a screen to field of game
game_screen_canv = tkinter.Canvas(ROOT, width=WIDTH * TILE + 1,
        height=HEIGHT * TILE + 1, bg='purple', highlightthickness=0)
game_screen_canv.place(x=415, y=60, anchor='nw')

# The disign of interface
bg_image = Image.open('img/background_img.png').resize((1200, 700))
bg_image = ImageTk.PhotoImage(bg_image)
screen_canv.create_image(0, 0, anchor='nw', image=bg_image)

field_bg_image = Image.open('img/field_background.png').resize((420, 630))
field_bg_image = ImageTk.PhotoImage(field_bg_image)
game_screen_canv.create_image(0, 0, anchor='nw', image=field_bg_image)

name_img_obj = Image.open('img/Tetris_logo.png').resize((341, 98))
name_img_obj = ImageTk.PhotoImage(name_img_obj)
screen_canv.create_image(30, 10, anchor='nw', image=name_img_obj)

top10_img = Image.open('img/top_ten_image.png').resize((160, 120))
top10_img = ImageTk.PhotoImage(top10_img)
screen_canv.create_image(950, 20, anchor='nw', image=top10_img)

# Creates images of our figures

figures_img = {
    'i-fig': Image.open('img/I_figure.png').resize((140, 35)),
    'j-fig': Image.open('img/J_figure.png').resize((70, 105)), 
    'l-fig': Image.open('img/L_figure.png').resize((70, 105)), 
    'o-fig': Image.open('img/O_figure.png').resize((70, 70)), 
    's-fig': Image.open('img/S_figure.png').resize((70, 105)), 
    't-fig': Image.open('img/T_figure.png').resize((70, 105)), 
    'z-fig': Image.open('img/Z_figure.png').resize((70, 105)) }

next_figures_img = {
    'i-fig': Image.open('img/I_figure.png').resize((185, 47)),
    'j-fig': Image.open('img/J_figure.png').resize((95, 140)), 
    'l-fig': Image.open('img/L_figure.png').resize((95, 140)), 
    'o-fig': Image.open('img/O_figure.png').resize((93, 93)), 
    's-fig': Image.open('img/S_figure.png').resize((93, 140)), 
    't-fig': Image.open('img/T_figure.png').resize((93, 140)), 
    'z-fig': Image.open('img/Z_figure.png').resize((93, 140)) }



# Displays which figure will be next.
for fig in figures_obj:
    if fig[1] == next_figure:
        next_figure_img = ImageTk.PhotoImage(next_figures_img[fig[0]])
        screen_canv.create_image(180, 450, anchor='center', image=next_figure_img)
        break

# draw figure


grid = [game_screen_canv.create_rectangle(x * TILE, y * TILE, x * TILE +
        TILE, y * TILE + TILE) for x in range(WIDTH) for y in range(HEIGHT)]


for idx in range(4):
    figure_rect_x = figure[idx][0] * TILE 
    figure_rect_y = figure[idx][1] * TILE
    game_screen_canv.create_rectangle(figure_rect_x, figure_rect_y,
        figure_rect_x + TILE, figure_rect_y + TILE, fill=rgb_to_hex(color))
    for fig in figures_obj:
        if fig[1] == figure:
            figure_img = ImageTk.PhotoImage(figures_img[fig[0]])
            game_screen_canv.create_image(figure_rect_x, figure_rect_y, anchor='nw', image=figure_img)
            break
    
 

screen_canv.create_text(380, 13, text='BEST RECORD:  123456 ',
                font=('ProtoSans56', 25), fill='purple', anchor='nw')

screen_canv.create_text(35, 155, text='Your nickname: \n ...',
                font=('ProtoSans56', 25), fill='blue', anchor='nw')

screen_canv.create_text(35, 240, text='Score: ...',
                font=('ProtoSans56', 35), fill='orange', anchor='nw')


