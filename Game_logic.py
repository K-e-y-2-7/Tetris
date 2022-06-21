'''
main_game_logic.py.
A file that reproduces the main logic of game.  
===============================================

'''

from random import choice, randrange
from copy import deepcopy
import time

from Settings import *


nick = 'Kirill'
app_running = True
def get_score(stop=None) -> list:
    ''' Finction is extraction data from file scores.txt and
        writing them in list score.
        Return list of score.
    '''

    with open('Scores.txt', 'r') as score_file_r:
        flag = 0 
        score = []
        for line in score_file_r:
            score.append(line[:-1])
            flag += 1
            if flag == stop: break

    return score

score, lines = 0, 0
top_10 = get_score(stop = 10)
scores = {str(idx): score.split(': ')[2] for idx, score in enumerate(get_score())}
record = int(top_10[0].split(': ')[2])

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


def display_image(canv: Canvas, img: str, resize: tuple, coordinate: tuple, anch: str)-> ImageTk.PhotoImage:
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

# Creates and display needed text
rec = screen_canv.create_text(380, 13, text=f'BEST RECORD:  {record}',
                font=('ProtoSans56', 25), fill='purple', anchor='nw')

screen_canv.create_text(35, 155, text=f'Your nickname: \n {nick}',
                font=('ProtoSans56', 25), fill='blue', anchor='nw')

scr = screen_canv.create_text(35, 240, text=f'Score: {score}',
                font=('ProtoSans56', 35), fill='orange', anchor='nw')

grid_1 = [game_screen_canv.create_rectangle(x * TILE, y * TILE, x * TILE+TILE, y * TILE+TILE) for x in range(WIDTH) for y in range(HEIGHT)]
grid_2 = [top_10_canv.create_rectangle(x, y * TILE, x * 309, y * TILE + TILE)\
                                     for x in range(2) for y in range(HEIGHT)]

display_top10()


figures_pos = [[((-1, 0), (-2, 0), (0, 0), (1, 0)), '#4cc9f0', 'i-fig'],
                [((0, 0), (0, -1), (0, 1), (1, -1)), '#072ac8', 'j-fig'],
                [((0, 0), (0, -1), (0, 1), (-1, -1)), '#fb8500', 'l-fig'],
                [((0, -1), (-1, -1), (-1, 0), (0, 0)), '#ffd500', 'o-fig'],
                [((0, 0), (-1, 0), (0, 1), (-1, -1)), '#31cb00', 's-fig'],
                [((0, 0), (0, -1), (0, 1), (-1, 0)), '#b100e8', 't-fig'],
                [((-1, 0), (-1, 1), (0, 0), (0, -1)), '#ff002b', 'z-fig']]
figures = [[[[x_pos + WIDTH // 2, y_pos + 1, 1, 1] for x_pos, y_pos in fig_pos[0]], fig_pos[1], fig_pos[2]] for fig_pos in figures_pos]

field = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

anim_count, anim_speed, anim_limit = 0, 60, 2000

score, lines = 0, 0
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

get_color = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))

figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
color, next_color = figure[1], next_figure[1]

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def check_borders(i):
    print(i)
    if figure[0][i][0] < 0 or figure[0][i][0] > WIDTH - 1:
        return False
    elif figure[0][i][1] > HEIGHT - 1 or field[figure[0][i][1]][figure[0][i][0]]:
        return False
    return True


def on_closing():
    global app_running
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        app_running = False
        #tk.destroy()


def move_obj(event):
    global rotate, anim_limit, x_moving
    if event.keysym == 'Up':
        rotate = True
    elif event.keysym == 'Down':
        anim_limit = 100
    elif event.keysym == 'Left':
        x_moving = -1
    elif event.keysym == 'Right':
        x_moving = 1

game_screen_canv.bind_all("<KeyPress-Up>",move_obj)
game_screen_canv.bind_all("<KeyPress-Down>",move_obj)
game_screen_canv.bind_all("<KeyPress-Left>",move_obj)
game_screen_canv.bind_all("<KeyPress-Right>",move_obj)

def move_x():
    global figure
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[0][i][0] += x_moving
        if not check_borders(i):
            figure = deepcopy(figure_old)
            break


def move_y():
    global anim_count, anim_speed, anim_limit, figure
    global color, next_figure, next_color
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[0][i][1] += 1
            if not check_borders(i):
                for i in range(4):
                    field[figure_old[0][i][1]][figure_old[0][i][0]] = color
                figure, color = next_figure, next_color
                next_figure  = deepcopy(choice(figures))
                next_color = next_figure[1]
                anim_limit = 2000
                break

def overturn():
    global figure
    center = figure[0][0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[0][i][1] - center[1]
            y = figure[0][i][0] - center[0]
            figure[0][i][0] = center[0] - x
            figure[0][i][1] = center[1] + y
            if not check_borders(i):
                figure = deepcopy(figure_old)
                break


def check_lines():
    global anim_speed
    line, lines = HEIGHT - 1, 0
    for row in range(HEIGHT - 1, -1, -1):
        count = 0
        for i in range(WIDTH):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < WIDTH:
            line -= 1
        else:
            anim_speed += 3
            lines += 1

    return lines


def draw_figure(fig_list):
    ''' Function displays a figure on the game field.
    '''
    for idx in range(4):
        figure_rect_x = figure[0][idx][0] * TILE 
        figure_rect_y = figure[0][idx][1] * TILE
        fig_list.append(game_screen_canv.create_rectangle(figure_rect_x,
                figure_rect_y, figure_rect_x + TILE, figure_rect_y + TILE,
                fill=figure[1]))

    return fig_list

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


def draw_next_figure(fig_list):
    ''' Function displays on screen which figure will be next.
    '''
    global nxt_fig_img
    nxt_fig_img = ImageTk.PhotoImage(nxt_figs_img[next_figure[2]])
    fig_list.append(screen_canv.create_image(180, 450, anchor='center', image=nxt_fig_img))

    return fig_list


def draw_field(fig_list):
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                figure_rect_x, figure_rect_y = x * TILE, y * TILE
                fig_list.append(game_screen_canv.create_rectangle(figure_rect_x, figure_rect_y, figure_rect_x + TILE,
                                                    figure_rect_y + TILE, fill=col))
    return fig_list


def game_over():
    global field
    for i in range(WIDTH):
        if field[0][i]:
            field = [[0 for i in range(WIDTH)] for i in range(HEIGHT)]
            anim_count, anim_speed, anim_limit = 0, 60, 2000
            score = 0
            for item in grid_1:
                game_screen_canv.itemconfigure(item, fill=rgb_to_hex(get_color()))
                time.sleep(0.005)
                tetris.update_idletasks()
                tetris.update()
            for item in grid_1:
                game_screen_canv.itemconfigure(item, fill="")

x_moving, rotate = 0, False
def start():
    global score, x_moving, rotate
    while app_running:
        if app_running:
            # Moving our figure along the x coordinate.
            move_x()
            # Moving our figure along the y coordinate.
            move_y()
            # Rotation of our figure around its axis.
            overturn()  
            lines = check_lines()

            # Compute score
            score += scores[lines]

            fig1, fig2 = [], []
            # Displays a figure on the game field.
            fig1 = draw_figure(fig1)

            # draw field
            fig1 += draw_field(fig1)

            # draw next figure
            fig2 = draw_next_figure(fig2)

            screen_canv.itemconfigure(scr, text=f'Score: {score}')
            screen_canv.itemconfigure(rec, text=f'BEST RECORD:  {record}')

            # game over
            game_over()

            x_moving, rotate = 0, False
            tetris.update_idletasks()
            tetris.update()
            for id_fig in fig1: game_screen_canv.delete(id_fig)
            for id_fig in fig2: screen_canv.delete(id_fig)
        time.sleep(0.005)


tetris.destroy()