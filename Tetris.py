'''
Tetris.py.
The main file of game.
======================

'''

import Exceptions
import Game_logic


try:    
    Game_logic.tetris.mainloop()  
except Exceptions.GameOver:
    print(Exceptions.GameOver)
except FileNotFoundError:
    with open('Scores.txt', 'w') as score_file_w:
        pass 