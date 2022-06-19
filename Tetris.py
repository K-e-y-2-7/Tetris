'''
Tetris.py.
The main file of game.
======================

'''

import Exceptions
import gui
import Game_logic



try:
    for item in gui.grid:
        gui.game_screen_canv.itemconfigure(item, fill=Game_logic.rgb_to_hex(Game_logic.get_collor()))

    for item in gui.grid:
        gui.game_screen_canv.itemconfigure(item, fill='')
    gui.ROOT.mainloop()
    
except Exceptions.GameOver:
        ...
except Exceptions.Quit:
    exit()
