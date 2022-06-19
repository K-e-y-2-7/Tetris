'''
Models.py.
File containing all models.  
===========================

'''

from Settings import *


i = [(-2, 0), (-1, 0), (0, 0), (1, 0)]
j = [(1, -1), (0, -1), (0, 0), (0, 1)]
l = [(-1, -1), (0, -1), (0, 0), (0, 1)]
o = [(-1, -1), (0, -1), (0, 0), (-1, 0)]
s = [(-1, -1), (-1, 0), (0, 0), (0, 1)]
t = [(-1, 0), (0, -1), (0, 0), (0, 1)]
z = [(-1, 1), (-1, 0), (0, 0), (0, -1)]
FIGURES_POS = (i, j, l, o, s, t, z)
    
class Figure: 
    figures = [[(x + WIDTH // 2, y+ 1, 1, 1) for x, y in fig_pos] for fig_pos in FIGURES_POS]

    def __init__ (self, image, name, form):
        self.image = image
        self.name = name
        self.form = form

    