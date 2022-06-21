'''
gui.py.
A file that reproduces the graphical interface.  
===============================================

'''

from PIL import Image, ImageTk

from Game_logic import *


# The disign of interface
def display_top10(y = 40):
    ''' Function display list of best 10 players with their scores
    '''
    for player in top_10:
        top_10_canv.create_text(10, y, text=f'{player}',\
                    font=('ProtoSans56', 15), fill='orange', anchor='nw')
        y += 35


def image_generator(img: str, size_x: int, size_y: int) -> ImageTk.PhotoImage:
    ''' Function accepts name of image, x and y size.
        Creates image and resize it. And return image object.
    '''
    image = ImageTk.PhotoImage(Image.open(img).resize((size_x, size_y)))
    return image


def display_image(canv: tkinter.Canvas, img: str, resize: tuple, coordinate: tuple, anch: str)-> ImageTk.PhotoImage:
    ''' Function accepts name of image, tuple of x and y coordinate,
        canvas object, tuple of x and y size, anchor.
        Call function image_generator and display result of work image_generator.
        Return image object.
    '''
    image = image_generator(img, resize[0], resize[1])
    canv.create_image(coordinate[0], coordinate[1], anchor=anch, image=image)
    return image

# Creates and display needed images
bg_img = display_image(canv=screen_canv, img='img/background_img.png',\
                        resize=(1200, 700), coordinate=(0, 0), anch=('nw'))
field_bg_img = display_image(canv=game_screen_canv, resize=(420, 630),\
            img='img/field_background.png', coordinate=(0, 0), anch=('nw'))

name_img = display_image(canv=screen_canv, img='img/Tetris_logo.png',\
                        resize=(341, 98), coordinate=(30, 10), anch=('nw'))
top10_img = display_image(canv=screen_canv, img='img/top_ten_image.png',\
                    resize=(160, 120), coordinate=(930, 20), anch=('nw'))

screen_canv.create_text(380, 13, text=f'BEST RECORD:  {record} ',
                font=('ProtoSans56', 25), fill='purple', anchor='nw')

screen_canv.create_text(35, 155, text='Your nickname: \n ...',
                font=('ProtoSans56', 25), fill='blue', anchor='nw')

screen_canv.create_text(35, 240, text='Score: ...',
                font=('ProtoSans56', 35), fill='orange', anchor='nw')

# Creates images of our figures
figs_img = {
    'i-fig': Image.open('img/I_figure.png').resize((140, 35)),
    'j-fig': Image.open('img/J_figure.png').resize((70, 105)), 
    'l-fig': Image.open('img/L_figure.png').resize((70, 105)), 
    'o-fig': Image.open('img/O_figure.png').resize((70, 70)), 
    's-fig': Image.open('img/S_figure.png').resize((70, 105)), 
    't-fig': Image.open('img/T_figure.png').resize((70, 105)), 
    'z-fig': Image.open('img/Z_figure.png').resize((70, 105)) }

nxt_figs_img = {
    'i-fig': Image.open('img/I_figure.png').resize((185, 47)),
    'j-fig': Image.open('img/J_figure.png').resize((95, 140)), 
    'l-fig': Image.open('img/L_figure.png').resize((95, 140)), 
    'o-fig': Image.open('img/O_figure.png').resize((93, 93)), 
    's-fig': Image.open('img/S_figure.png').resize((93, 140)), 
    't-fig': Image.open('img/T_figure.png').resize((93, 140)), 
    'z-fig': Image.open('img/Z_figure.png').resize((93, 140)) }


grid_1 = [game_screen_canv.create_rectangle(x * TILE, y * TILE, x * TILE +\
        TILE, y * TILE + TILE,) for x in range(WIDTH) for y in range(HEIGHT)]

grid_2 = [top_10_canv.create_rectangle(x, y * TILE, x * 309, y * TILE + TILE)\
                                     for x in range(2) for y in range(HEIGHT)]


def draw_next_figure():
    ''' Function displays on screen which figure will be next.
    '''
    global nxt_fig_img
    nxt_fig_img = ImageTk.PhotoImage(nxt_figs_img[def_figure(next_figure)[2]])
    screen_canv.create_image(180, 450, anchor='center', image=nxt_fig_img)
     


def draw_figure(fig_list):
    ''' Function displays a figure on the game field.
    '''
    for idx in range(4):
        figure_rect_x = figure[0][idx][0] * TILE 
        figure_rect_y = figure[0][idx][1] * TILE
        fig_list.append(game_screen_canv.create_rectangle(figure_rect_x, figure_rect_y,
                                figure_rect_x + TILE, figure_rect_y +
                                TILE, fill=figure[1]))

    return fig_list


display_top10()
