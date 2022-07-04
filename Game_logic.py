'''
main_game_logic.py.
A file that reproduces the main logic of game.  
===============================================

'''

from copy import deepcopy
from random import choice, randrange
import time
from string import ascii_letters

from Gui import *

# Define main variables of game.
app_running = True
anim_count, anim_speed, anim_limit = 0, 60, 2000

# List of coordinates for each part of the figure.
figures = [[[[x_pos + WIDTH // 2, y_pos + 1, 1, 1] for x_pos, y_pos in \
                fig_pos[0]], fig_pos[1], fig_pos[2]] for fig_pos in \
                figures_possition]

# A list containing lists of zeros.
# Zeros are subsequently replaced by color and a figure is drawn in this place
field = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))

color, next_color = figure[2], next_figure[2]
get_color = lambda: (randrange(30, 256), randrange(30, 256),
                                         randrange(30, 256))


# The nickname creation and the validation functioins.
def create_nick() -> str:
    ''' Function creates nick name.

        =================
        Return: nickname.

    '''

    nickname = input('Enter your nickname.\
    \n The nickname must contain no more than 10 characters,\
    \ncannot be an empty string, and must only contain numbers,\
    \nASCII characters, and/or underscores: ')
  
    return nickname


def validate_len_nick(nick: str) -> bool:
    ''' Function validate length nick name.

        =============
        Return: Bool.

    '''

    if 0 < len(nick) < 11:
        return True
    
    messagebox.showwarning(title='Too long nick',\
            message=f'The length of your nickname = {len(nick)}\
    \n must be between 0 and 10 inclusive!')

    return False


def validate_char_nick(nick: str) -> bool:
    ''' Function validate caracter of nick name.

        =============
        Return: Bool.

    '''

    suitable_symbols = ''.join((f'{ascii_letters}', '_', '0123456789'))

    # Validation.
    for char in nick:
        if char not in suitable_symbols:
            messagebox.showwarning(title='Not valid char',\
                message=f'Character "{char}" \
                    \n not ASCII, number or "_" !')

            return False 
    else:
        return True


def nick_validation() -> str:
    ''' Function call the nickname creation and the validation
        functions in a cycle. If the nickname passed validation, 
        the function returns the nickname.

        =================
        Return: nickname.

    '''

    messagebox.showinfo(title='NICKNAME', message='\
    \n  Enter your nickname in console.\
    \n The nickname must contain no more than 10 characters, \
    \ncannot be an empty string, and must only contain numbers, \
    \nASCII characters, and/or underscores: ')

    while True:
        nickname = create_nick()
        if validate_len_nick(nickname) and validate_char_nick(nickname):
                
            return nickname


# Function for score display.
def score_update(nick: str, score) -> dict:
    ''' Function which update data in score file. '''
    
    with open(path.abspath(f'{p}/Scores.txt'), 'r') as score_file_r:
        # An explanation for the horrible incomprehensible
        # construction below.
        #
        # Disassemble in dict comprehension into a string file that
        # already consisted of dict, and build a new dict
        # from these strings.
        old_scores = {}
        for line in score_file_r:
            if line[:-2]:
                key = (line.split(' : ')[1][:-2]).split(': ')[0].strip()
                value = int((line.split(' : ')[1]).split(': ')[1])

                old_scores[key] = value
                
        if nick in old_scores.keys() and score > old_scores.get(nick):
            old_scores.update([(nick, score)])
        else:
            old_scores.update([(nick, score)])
        # We turn the dict into a list for sorting data in it
        # by our special sorting system.
        old_scores = [(key, value) for key, value in old_scores.items()]
        old_scores.sort(key=lambda item: item[1], reverse=True) 
        # Now we overwrite our file to make changes.

        with open(path.abspath(f'{p}/Scores.txt'), 'w') as score_file_w:
            # Creates new dict with updated and sorted data
            new_scores = {item[0] : int(item[1]) for item in old_scores}
            # Put our dict in a file
            for idx, (key, value) in enumerate(new_scores.items()):
                score_file_w.write(f'#{idx + 1} : {key}: {value} \n')
        
        return new_scores


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
            # If the figure does not touch the bottom board, move it.
            if not check_borders(idx):
                # Puts the name of the figure in the cells to then color them.
                for idx in range(4):
                    field[figure_old[0][idx][1]]\
                            [figure_old[0][idx][0]] = color
                figure, color = next_figure, next_color
                next_figure  = deepcopy(choice(figures))
                next_color = next_figure[2]
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
def check_borders(index: int) -> bool:
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
            anim_speed += 10
            lines += 1

    return lines

# Functions responsible for logic outside the game.
def game_over(grid_1: list):
    '''Function determines behavior after the end of the game'''

    global anim_count, anim_limit, anim_speed, app_running, btn_start
    global field, score, record

    for i in range(WIDTH):
        # Check if the game is over.
        if field[0][i]:
            # Remove the button to then replace it with another.
            btn_stop.destroy()
            # Sets the default values.
            field = [[0 for i in range(WIDTH)] for i in range(HEIGHT)]
            anim_count, anim_speed, anim_limit = 0, 60, 2000
            oldscore = score
            score = 0
            if grid_1:
                # Creates animation, colloring of all cells.
                for item in grid_1:
                    game_screen_canv.itemconfigure(item,
                                            fill=rgb_to_hex(get_color()))
                    time.sleep(0.004)
                    tetris.update_idletasks()
                    tetris.update()
                # Clears the game field, all cells, thereby preparing
                # it for the next session.
                for item in grid_1:
                    game_screen_canv.itemconfigure(item, fill="")
            
            app_running = False
            # Writes score in Scores.txt 
            score_update(nickname, oldscore)
            # Deletes the grid of the game session.
            for g in grid_1: game_screen_canv.delete(g)
            # Deletes the text of nickname of the game session.
            screen_canv.delete(nick)
            # Creates a button in place of the deleted one.
            btn_start = Button(screen_canv, image=start_img, command=start,\
                                         width=170, height=65, bg='#4a0a77')
            btn_start.place(x=80, y=540)
            # Updates list of top players and record 
            for x in text:
                top_10_canv.delete(x)
            display_top10()

            record = int(get_score(stop = 1)[0].split(': ')[2])


def on_closing():
    ''' Terminates the application. '''

    global app_running
    if messagebox.askokcancel('Exit Application.',\
                    'Do you want to exit the application?'):

        messagebox.showinfo('Exit Application.', 'Good bye!')
        app_running = False
        tetris.destroy() 

display_top10()

x_moving, rotate = 0, False
def game_start(grid: list):
    '''Launches the program'''
    
    global app_running, btn_stop, x_moving, rotate, score

    # Creates a button in place of the deleted one.
    btn_stop = Button(screen_canv, image=stop_img, command=stop,\
                             width=170, height=65, bg='#4a0a77')
    btn_stop.place(x=80, y=540)

    # Main cycle of game.
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
            screen_canv.itemconfigure(nick, text=f'Your nickname:\
                                                 \n {nickname}')

            # Game over
            game_over(grid)

            # Set default values for next iteration. 
            x_moving, rotate = 0, False

            tetris.update_idletasks()
            tetris.update()
            # Delete the figure after moving.
            for id_fig in fig1: game_screen_canv.delete(id_fig)
            # Remove from the following figures, the current one.
            for id_fig in fig2: screen_canv.delete(id_fig)
        # Delay for cycle update. 
        time.sleep(0.007)

    # Actions after forced termination of the game lifecycle.

    # Sets the parameter needed to execute the function game_over.
    field[0][1] = '#ff002b'
    game_over(grid)
    tetris.update_idletasks()
    tetris.update()


def start():
    ''' The function to launch the game from the game menu.
        Changed global variables. 
        Also calling the create_nickname function to display the player's,
        nickname, and later writes it with a score to the result file.
        Create grid for play field and call function start for launch game.

    '''
   
    global app_running, nickname, nick

    # Remove the button to then replace it with another.
    btn_start.destroy()

    # Sets a nickname for one game sesion. 
    nickname = nick_validation()

    # Displays the current nickname and stores it in a variable for deletion
    # after the end of the game.
    nick = screen_canv.create_text(35, 155, text=f'Your nickname:\
        \n {nickname}', font=('ProtoSans56', 25), fill='blue', anchor='nw')

    # Create grid for game sesion.
    grid = create_grid()
    # Delay. Needed so that the bі user has time to switch between windows,
    # entering a nickname in the console and the game.
    # The application stops responding for 3 seconds, it's okay, SO NECESSARY!
    time.sleep(3)
    app_running = True

    # Launch the game.
    game_start(grid)
    

def stop():
    '''Function to stop the game and go back to the game menu.'''

    global app_running
    app_running = False
    

# Creates buttons for control of application.
btn_start = Button(screen_canv, image=start_img, command=start, width=170,\
                                                 height=65, bg='#4a0a77')
btn_start.place(x=80, y=540)
btn_quit = Button(screen_canv, image=quit_img, command=on_closing, width=170,\
                                                 height=65, bg='#4a0a77')
btn_quit.place(x=80, y=610)
