'''
gui.py.
A file that reproduces the graphical interface.  
===============================================

'''

from PIL import Image as PILImage, ImageTk 

from Settings import *

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
        top_10_canv.create_text(20, y, text=f'{player}',\
                    font=('ProtoSans56', 15), fill='#8A888A', anchor='nw')
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


# Creates images of our figures
figs_img = {
    'i-fig': PILImage.open('img/I_figure_one_pxl.png').resize((35, 35)),
    'j-fig': PILImage.open('img/J_figure_one_pxl.png').resize((35, 35)), 
    'l-fig': PILImage.open('img/L_figure_one_pxl.png').resize((35, 35)), 
    'o-fig': PILImage.open('img/O_figure_one_pxl.png').resize((35, 35)), 
    's-fig': PILImage.open('img/S_figure_one_pxl.png').resize((35, 35)), 
    't-fig': PILImage.open('img/T_figure_one_pxl.png').resize((35, 35)), 
    'z-fig': PILImage.open('img/Z_figure_one_pxl.png').resize((35, 35)) }


nxt_figs_img = {
    'i-fig': PILImage.open('img/I_figure.png').resize((185, 47)),
    'j-fig': PILImage.open('img/J_figure.png').resize((95, 140)), 
    'l-fig': PILImage.open('img/L_figure.png').resize((95, 140)), 
    'o-fig': PILImage.open('img/O_figure.png').resize((93, 93)), 
    's-fig': PILImage.open('img/S_figure.png').resize((93, 140)), 
    't-fig': PILImage.open('img/T_figure.png').resize((93, 140)), 
    'z-fig': PILImage.open('img/Z_figure.png').resize((93, 140)) }


# Functions displays game elements
def draw_figure(fig_list: list, figure: list) -> list:
    ''' Function displays a figure on the game field.
        Accept list, append figure that was displayed in list.

        =============
        Return: list.

    '''

    # global is required to to display images in screen.
    global piece_img1, piece_img2, piece_img3, piece_img4
    
    # Coordinates for every pieces of figure.
    first_piece_rect_x = figure[0][0][0] * TILE 
    first_piece_rect_y = figure[0][0][1] * TILE
    second_piece_rect_x = figure[0][1][0] * TILE 
    second_piece_rect_y = figure[0][1][1] * TILE
    third_piece_rect_x = figure[0][2][0] * TILE 
    third_piece_rect_y = figure[0][2][1] * TILE
    fourth_piece_rect_x = figure[0][3][0] * TILE 
    fourth_piece_rect_y = figure[0][3][1] * TILE
    

    def piece_img_generator() -> ImageTk.PhotoImage:
        fig_img = ImageTk.PhotoImage(figs_img[figure[2]])

        return fig_img

    def disp_piece_img(fig_img, piece_rect_x, piece_rect_y) -> ImageTk.PhotoImage:
        ''' Function accepts name of image, x and y coordinate.
            Display image.

            ====================
            Return: image object.

        '''

        img = game_screen_canv.create_image(piece_rect_x, piece_rect_y, \
                                             anchor='nw',image=fig_img)

        return img

    piece_img1, piece_img2 = piece_img_generator(), piece_img_generator()
    piece_img3, piece_img4 = piece_img_generator(), piece_img_generator()

    img1 = disp_piece_img(piece_img1, first_piece_rect_x, first_piece_rect_y)
    img2 = disp_piece_img(piece_img2, second_piece_rect_x, second_piece_rect_y)
    img3 = disp_piece_img(piece_img3, third_piece_rect_x, third_piece_rect_y)
    img4 = disp_piece_img(piece_img4, fourth_piece_rect_x, fourth_piece_rect_y)

    fig_list.append((img1, img2, img3, img4))

    return fig_list


def draw_next_figure(fig_list: list, figure: list) -> list:
    ''' Function displays on screen which figure will be next.
        Accept list, append figure that was displayed in list.

        =============
        Return: list.

    '''

    global nxt_fig_img
    
    nxt_fig_img = ImageTk.PhotoImage(nxt_figs_img[figure[2]])
    fig_list.append(screen_canv.create_image(160, 420, anchor='center',
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
                                TILE, figure_rect_y + TILE, fill='purple'))

    return fig_list


# Creates and display background images.
bg_img = display_image(canv=screen_canv, img='img/background_img.png',\
                        resize=(1200, 700), coordinate=(0, 0), anch=('nw'))
field_bg_img = display_image(canv=game_screen_canv, resize=(420, 630),\
            img='img/field_background.png', coordinate=(0, 0), anch=('nw'))
bg_top_img = display_image(canv=top_10_canv, resize=(310, 470),\
            img='img/bg3.png', coordinate=(0, -70), anch=('nw'))

name_img = display_image(canv=screen_canv, img='img/Tetris_logo.png',\
                        resize=(341, 98), coordinate=(30, 10), anch=('nw'))
top10_img = display_image(canv=screen_canv, img='img/top_ten_image.png',\
                    resize=(160, 120), coordinate=(930, 20), anch=('nw'))

# Creates images for buttons.
start_img = image_generator('img/start.png', 220, 110)
stop_img = image_generator('img/stop.png', 180, 75)
quit_img = image_generator('img/quit.png', 220, 110)

# Determine competition variables.
score, lines = 0, 0
scores = {0: 0, 1: 10, 2: 30, 3: 70, 4: 120}
top_10 = get_score(stop = 10)
record = int(top_10[0].split(': ')[2])

# Creates and display needed text
rec = screen_canv.create_text(380, 13, text=f'BEST RECORD:  {record}',
                font=('ProtoSans56', 25), fill='purple', anchor='nw')

scr = screen_canv.create_text(35, 240, text=f'Score: {score}',
                font=('ProtoSans56', 35), fill='orange', anchor='nw')

# Creates grids for game field and scores field.
def create_grid() -> list:
    '''Function create grid for play field.

       ====================
       Return: list of grid

    '''

    grid_1 = [game_screen_canv.create_rectangle(
                x * TILE, y * TILE, x * TILE+TILE, y * TILE+TILE)
                for x in range(WIDTH) for y in range(HEIGHT)]
    
    return grid_1

grid_2 = [top_10_canv.create_rectangle(x, y * TILE, x * 309, y * TILE + TILE)\
                                     for x in range(2) for y in range(HEIGHT)]

