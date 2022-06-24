'''
Tetris.py.
The main file of game.
======================

'''

import Game_logic


try:    
    Game_logic.tetris.mainloop()  
except FileNotFoundError:
    with open('Scores.txt', 'w') as score_file_w:
        pass 