'''
Tetris.py.
The main file of game.
======================

'''

import Exceptions
import Gui



try:     
    Gui.running(Gui.grid_1, Gui.draw_figure, Gui.draw_next_figure)
except Exceptions.GameOver:
        print('game over')
except Exceptions.Quit:
    exit()
except FileNotFoundError:
    with open('Scores.txt', 'w') as score_file_w:
        pass