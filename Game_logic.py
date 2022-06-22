'''
main_game_logic.py.
A file that reproduces the main logic of game.  
===============================================

'''

from random import choice, randrange
from copy import deepcopy
import time

from Settings import *
from Gui import *


app_running = True
anim_count, anim_speed, anim_limit = 0, 120, 2000

figures = [[[[x_pos + WIDTH // 2, y_pos + 1, 1, 1] for x_pos, y_pos in \
                fig_pos[0]], fig_pos[1], fig_pos[2]] for fig_pos in \
                figures_possition]

field = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))

color, next_color = figure[1], next_figure[1]
get_color = lambda: (randrange(30, 256), randrange(30, 256),
                                         randrange(30, 256))


def rgb_to_hex(rgb: tuple) -> str:
    ''' Convert color numbers to hexadecimal number.

        ===========================
        Return: hexadecimal number.

    '''

    return '#%02x%02x%02x' % rgb

# Functions responsible for moving figure.
def move_x():
    ''' Moves the figure along the x-axis. '''

    global figure
    figure_old = deepcopy(figure)
    for idx in range(4):
        figure[0][idx][0] += x_moving
        if not check_borders(idx):
            figure = deepcopy(figure_old)
            break


def move_y():
    ''' Moves the figure along the y-axis. '''

    global anim_count, anim_speed, anim_limit, figure
    global color, next_figure, next_color
    anim_count += anim_speed

    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)

        for idx in range(4):
            figure[0][idx][1] += 1
            if not check_borders(idx):

                for idx in range(4):
                    field[figure_old[0][idx][1]]\
                            [figure_old[0][idx][0]] = color
                figure, color = next_figure, next_color
                next_figure  = deepcopy(choice(figures))
                next_color = next_figure[1]
                anim_limit = 2000
                break


def overturn():
    ''' Rotates the figure along the x-axis. '''

    global figure
    center = figure[0][0]  # first element figure
    figure_old = deepcopy(figure)
    if rotate:
        for idx in range(4):
            x_pos = figure[0][idx][1] - center[1]
            y_pos = figure[0][idx][0] - center[0]
            figure[0][idx][0] = center[0] - x_pos
            figure[0][idx][1] = center[1] + y_pos
            if not check_borders(idx):
                figure = deepcopy(figure_old)
                break


def move_obj(event: str):
    ''' Traks event, and moving or rotate figure.
        Accept event.

    '''

    global rotate, anim_limit, x_moving
    if event.keysym == 'Up':
        rotate = True
    elif event.keysym == 'Down':
        anim_limit = 100
    elif event.keysym == 'Left':
        x_moving = -1
    elif event.keysym == 'Right':
        x_moving = 1

# Bind control keys.
game_screen_canv.bind_all("<KeyPress-Up>", move_obj)
game_screen_canv.bind_all("<KeyPress-Down>", move_obj)
game_screen_canv.bind_all("<KeyPress-Left>", move_obj)
game_screen_canv.bind_all("<KeyPress-Right>", move_obj)

# Functions responsible for the logic of the playing field.
def check_borders(index) -> bool:
    ''' The function compares the position of the figure with the
        edge of the field, and does not allow it to climb beyond the edge.

        =============
        Return: bool.

    '''

    if figure[0][index][0] < 0 or figure[0][index][0] > WIDTH - 1:

        return False
    elif figure[0][index][1] > HEIGHT - 1 or field[figure[0][index][1]]\
                                                  [figure[0][index][0]]:

        return False

    return True


def check_lines() -> int:
    ''' The function checks whether a line of figures has been created
        at the bottom of the field. And counts these lines.

        ==============
        Return: lines.

    '''

    global anim_speed
    line, lines = HEIGHT - 1, 0
    for row in range(HEIGHT - 1, -1, -1):
        count = 0
        for idx in range(WIDTH):
            if field[row][idx]:
                count += 1
            field[line][idx] = field[row][idx]
        if count < WIDTH:
            line -= 1
        else:
            anim_speed += 3
            lines += 1

    return lines

# Functions responsible for logic outside the game.
def game_over():
    '''Function determines behavior after the end of the game'''
    global field, anim_count, anim_speed, anim_limit
    for i in range(WIDTH):
        if field[0][i]:
            field = [[0 for i in range(WIDTH)] for i in range(HEIGHT)]
            anim_count, anim_speed, anim_limit = 0, 60, 2000
            score = 0
            for item in grid_1:
                game_screen_canv.itemconfigure(item,
                                        fill=rgb_to_hex(get_color()))
                time.sleep(0.005)
                tetris.update_idletasks()
                tetris.update()
            for item in grid_1:
                game_screen_canv.itemconfigure(item, fill="")


def on_closing():
    ''' Terminates the application. '''

    global app_running
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        app_running = False


display_top10(top_10)
x_moving, rotate = 0, False
def start():
    '''Launches the program'''

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
            fig1 = draw_figure(fig1, figure)

            # Displays a game field.
            fig1 += draw_field(fig1, field)

            # Displays a next figure.
            fig2 = draw_next_figure(fig2, next_figure)

            # Displays a changing in score and record
            screen_canv.itemconfigure(scr, text=f'Score: {score}')
            screen_canv.itemconfigure(rec, text=f'BEST RECORD:  {record}')

            # Game over
            game_over()

            # Set default values for next iteration. 
            x_moving, rotate = 0, False

            tetris.update_idletasks()
            tetris.update()
            # Delete the figure after moving.
            for id_fig in fig1: game_screen_canv.delete(id_fig)
            # Remove from the following figures, the current one.
            for id_fig in fig2: screen_canv.delete(id_fig)
        time.sleep(0.005)
