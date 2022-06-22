'''
Tetris.py.
The main file of game.
======================

'''

import Exceptions
import Game_logic


try:     
    Game_logic.start()
    Game_logic.tetris.destroy()
except Exceptions.GameOver:
        print('game over')
except Exceptions.Quit:
    exit()
except FileNotFoundError:
    with open('Scores.txt', 'w') as score_file_w:
        pass