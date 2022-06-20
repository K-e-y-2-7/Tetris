'''
Tetris.py.
The main file of game.
======================

'''

import Exceptions
import Gui
import Game_logic


try:
    for item in Gui.grid_1:
        Gui.game_screen_canv.itemconfigure(item, fill=Game_logic.rgb_to_hex(Game_logic.get_color()))

    for item in Gui.grid_1:
        Gui.game_screen_canv.itemconfigure(item, fill='')
        
    Gui.ROOT.mainloop()
    
except Exceptions.GameOver:
        ...
except Exceptions.Quit:
    exit()
