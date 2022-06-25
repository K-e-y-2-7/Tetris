'''
Tetris.py.
The main file of game.
======================

'''

import Game_logic


try:    
    Game_logic.tetris.mainloop()  
except FileNotFoundError:
    with open(Game_logic.path.abspath(f'{Game_logic.p}/Scores.txt'), 'w')\
                                                        as score_file_w:
        pass 