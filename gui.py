'''
gui.py.
A file that reproduces the graphical interface.  
===============================================

'''


from PIL import Image as PILImage, ImageTk 

from Settings import *

nick = 'Kirill'

# Creates images of our figures
figs_img = {
    'i-fig': PILImage.open('img/I_figure.png').resize((140, 35)),
    'j-fig': PILImage.open('img/J_figure.png').resize((70, 105)), 
    'l-fig': PILImage.open('img/L_figure.png').resize((70, 105)), 
    'o-fig': PILImage.open('img/O_figure.png').resize((70, 70)), 
    's-fig': PILImage.open('img/S_figure.png').resize((70, 105)), 
    't-fig': PILImage.open('img/T_figure.png').resize((70, 105)), 
    'z-fig': PILImage.open('img/Z_figure.png').resize((70, 105)) }

nxt_figs_img = {
    'i-fig': PILImage.open('img/I_figure.png').resize((185, 47)),
    'j-fig': PILImage.open('img/J_figure.png').resize((95, 140)), 
    'l-fig': PILImage.open('img/L_figure.png').resize((95, 140)), 
    'o-fig': PILImage.open('img/O_figure.png').resize((93, 93)), 
    's-fig': PILImage.open('img/S_figure.png').resize((93, 140)), 
    't-fig': PILImage.open('img/T_figure.png').resize((93, 140)), 
    'z-fig': PILImage.open('img/Z_figure.png').resize((93, 140)) }


def get_score(stop=None) -> list:
    ''' Finction is extraction data from file scores.txt and
        writing them in list score.

        ======================
        Return: list of score.

    '''

    with open('Scores.txt', 'r') as score_file_r:
        score = [line[:-1] for idx, line in enumerate(score_file_r)\
                                                    if idx != stop]
        
    return score

# The disign of interface
def display_top10(top, y = 40):
    ''' Function display list of best 10 players with their scores.

    '''

    for player in top:
        top_10_canv.create_text(10, y, text=f'{player}',\
                    font=('ProtoSans56', 15), fill='orange', anchor='nw')
        y += 35

# Functions displays images.
def image_generator(img: str, size_x: int, size_y: int) -> ImageTk.PhotoImage:
    ''' Function accepts name of image, x and y size.
        Creates image and resize it.

         ====================
        Return: image object.

    '''

    image = ImageTk.PhotoImage(PILImage.open(img).resize((size_x, size_y)))

    return image


def display_image(canv: Canvas, img: str, resize: tuple,
                  coordinate: tuple, anch: str)-> ImageTk.PhotoImage:
    ''' Function accepts name of image, tuple of x and y coordinate,
        canvas object, tuple of x and y size, anchor.
        Call function image_generator and display result of work image_generator.

        ====================
        Return: image object.

    '''

    image = image_generator(img, resize[0], resize[1])
    canv.create_image(coordinate[0], coordinate[1], anchor=anch, image=image)

    return image

# Functions displays game elements
def draw_figure(fig_list: list, figure: list) -> list:
    ''' Function displays a figure on the game field.
        Accept list, append figure that was displayed in list.

        =============
        Return: list.

    '''

    for idx in range(4):
        figure_rect_x = figure[0][idx][0] * TILE 
        figure_rect_y = figure[0][idx][1] * TILE
        fig_list.append(game_screen_canv.create_rectangle(figure_rect_x,
                figure_rect_y, figure_rect_x + TILE, figure_rect_y + TILE,
                fill=figure[1]))

    return fig_list


def draw_next_figure(fig_list: list, figure: list) -> list:
    ''' Function displays on screen which figure will be next.
        Accept list, append figure that was displayed in list.

        =============
        Return: list.

    '''

    global nxt_fig_img
    
    nxt_fig_img = ImageTk.PhotoImage(nxt_figs_img[figure[2]])
    fig_list.append(screen_canv.create_image(180, 450, anchor='center',
                                                  image=nxt_fig_img))

    return fig_list


def draw_field(fig_list: list, field) -> list:
    ''' Function displays a fallen figures on the game field.
        Accept list, append figure that was displayed in list.

        =============
        Return: list.

    '''

    for y_axis, raw in enumerate(field):
        for x_axis, col in enumerate(raw):
            if col:
                figure_rect_x, figure_rect_y = x_axis * TILE, y_axis * TILE
                fig_list.append(game_screen_canv.create_rectangle(
                                figure_rect_x, figure_rect_y, figure_rect_x +
                                TILE, figure_rect_y + TILE, fill=col))

    return fig_list


# Creates and display needed images
bg_img = display_image(canv=screen_canv, img='img/background_img.png',\
                        resize=(1200, 700), coordinate=(0, 0), anch=('nw'))
field_bg_img = display_image(canv=game_screen_canv, resize=(420, 630),\
            img='img/field_background.png', coordinate=(0, 0), anch=('nw'))

name_img = display_image(canv=screen_canv, img='img/Tetris_logo.png',\
                        resize=(341, 98), coordinate=(30, 10), anch=('nw'))
top10_img = display_image(canv=screen_canv, img='img/top_ten_image.png',\
                    resize=(160, 120), coordinate=(930, 20), anch=('nw'))

# Determine competition variables.
score, lines = 0, 0
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}
top_10 = get_score(stop = 10)
record = int(top_10[0].split(': ')[2])

# Creates and display needed text
rec = screen_canv.create_text(380, 13, text=f'BEST RECORD:  {record}',
                font=('ProtoSans56', 25), fill='purple', anchor='nw')

screen_canv.create_text(35, 155, text=f'Your nickname: \n {nick}',
                font=('ProtoSans56', 25), fill='blue', anchor='nw')

scr = screen_canv.create_text(35, 240, text=f'Score: {score}',
                font=('ProtoSans56', 35), fill='orange', anchor='nw')


# Creates grids for game field and scores field.
grid_1 = [game_screen_canv.create_rectangle(
            x * TILE, y * TILE, x * TILE+TILE, y * TILE+TILE)
            for x in range(WIDTH) for y in range(HEIGHT)]

grid_2 = [top_10_canv.create_rectangle(x, y * TILE, x * 309, y * TILE + TILE)\
                                     for x in range(2) for y in range(HEIGHT)]

