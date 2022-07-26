''' This file contains tests for the Gui.py file.
    It tests all functions in Gui.py file.

'''

import unittest

import Gui


class CanvasTestCase(unittest.TestCase):
    def test_canvas_screen(self):
        self.assertIsInstance(Gui.screen_canv, Gui.Canvas)

    def test_game_screen_canv(self):
        self.assertIsInstance(Gui.game_screen_canv, Gui.Canvas)

    def test_top_10_canv(self):
        self.assertIsInstance(Gui.top_10_canv, Gui.Canvas)


class ScoreTestCase(unittest.TestCase):
    def test_get_score(self):
        self.assertIsInstance(Gui.get_score(2), list)


class ImageCreateTestCase(unittest.TestCase):
    def test_image_generator(self):
        self.assertIsInstance(Gui.image_generator(Gui.path.abspath(f'{Gui.p}/img/start.png'), 220, 110), Gui.ImageTk.PhotoImage)

    def test_display_image(self):
        img = Gui.display_image(canv=Gui.screen_canv, \
                    img=Gui.path.abspath(f'{Gui.p}/img/background_img.png'),\
                    resize=(1200, 700), coordinate=(0, 0), anch=('nw'))
        self.assertIsInstance(img, Gui.ImageTk.PhotoImage)


class DrawFiguresCreateTestCase(unittest.TestCase):
    def test_draw_figure(self):
        self.assertIsInstance(Gui.draw_figure([], [((-1, 0), (-2, 0), (0, 0), (1, 0)), '#4cc9f0', 'i-fig']), list)

    def test_not_empty(self):
        self.assertTrue(Gui.draw_figure([], [((-1, 0), (-2, 0), (0, 0), (1, 0)), '#4cc9f0', 'i-fig']))


class DrawNextFiguresCreateTestCase(unittest.TestCase):
    def test_draw_next_figure(self):
        self.assertIsInstance(Gui.draw_next_figure([], [((-1, 0), (-2, 0), (0, 0), (1, 0)), '#4cc9f0', 'i-fig']), list)

    def test_not_empty(self):
        self.assertTrue(Gui.draw_next_figure([], [((-1, 0), (-2, 0), (0, 0), (1, 0)), '#4cc9f0', 'i-fig']))


class DrawFieldCreateTestCase(unittest.TestCase):
    fig = Gui.draw_figure([], [((-1, 0), (-2, 0), (0, 0), (1, 0)), '#4cc9f0', 'i-fig'])
    def test_draw_field(self):
        self.assertIsInstance(Gui.draw_field(self.fig, [[0 for _ in range(Gui.WIDTH)] for _ in range(Gui.HEIGHT)]), list)

    def test_not_empty(self):
        self.assertTrue(Gui.draw_field(self.fig, [[0 for _ in range(Gui.WIDTH)] for _ in range(Gui.HEIGHT)]))


class ImagesTestCase(unittest.TestCase):
    def test_background_img(self):
        self.assertIsInstance(Gui.bg_img, Gui.ImageTk.PhotoImage)

    def test_field_background_img(self):
        self.assertIsInstance(Gui.field_bg_img, Gui.ImageTk.PhotoImage)

    def test_top_background_img(self):
        self.assertIsInstance(Gui.bg_top_img, Gui.ImageTk.PhotoImage)

    def test_name_img(self):
        self.assertIsInstance(Gui.name_img, Gui.ImageTk.PhotoImage)

    def test_top10_img(self):
        self.assertIsInstance(Gui.top10_img, Gui.ImageTk.PhotoImage)

    def test_start_img(self):
        self.assertIsInstance(Gui.start_img, Gui.ImageTk.PhotoImage)

    def test_stop_img(self):
        self.assertIsInstance(Gui.stop_img, Gui.ImageTk.PhotoImage)

    def test_quit_img(self):
        self.assertIsInstance(Gui.quit_img, Gui.ImageTk.PhotoImage)


class GridCreateTestCase(unittest.TestCase):
    def test_create_grid(self):
        self.assertIsInstance(Gui.create_grid(), list)

    def test_not_empty(self):
        self.assertTrue(Gui.create_grid())