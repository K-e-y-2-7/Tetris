'''
Models.py.
File containing all models.  
===========================

'''

from Settings import *

class Figure:

    FIGURES_POS = (
    [(-2, 0), (-1, 0), (0, 0), (1, 0)]
    [(0, -1), (-1, -1), (-1, 0), (0, 0)]
    [(-1, 0), (-1, 1), (0, 0), (0, -1)]
    [(0, 0), (-1, 0), (0, 1), (-1, -1)]
    [(0, 0), (0, -1), (0, 1), (-1, -1)]
    [(0, 0), (0, -1), (0, 1), (1, -1)]
    [(0, 0), (0, -1), (0, 1), (-1, 0)]
    )

    figures = [[(x + WIDTH // 2, y+ 1, 1, 1)\
                for x, y in fig_pos] for fig_pos in FIGURES_POS]

    