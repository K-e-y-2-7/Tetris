''' This file contains tests for the Game_logic.py file.
    It tests all functions in Game_logic.py file.

'''

import unittest
from unittest.mock import Mock

from Game_logic import *


class NickTestCase(unittest.TestCase):
    def test_len(self) -> None:
        self.assertFalse(validate_len_nick('1234567891011'))

    def test_char(self) -> None:
        self.assertFalse(validate_char_nick('kирилл'))


class ScoreTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.scores = get_old_score()
        self.nick = 'k'
        self.old_score = 1
        self.new_score = 2

    def test_isinstance_get_old_score(self):
        self.assertIsInstance(self.scores, dict,\
                                     'Must be instance of dict')

    def test_write_new_score(self):
        add_scores = update_score(self.nick, self.old_score, self.scores)
        self.assertEqual(self.old_score, add_scores[self.nick])

    def test_update_score(self):
        add_scores = update_score(self.nick, self.old_score, self.scores)
        updates_scores = update_score(self.nick, self.new_score, add_scores)
        self.assertEqual(self.new_score, updates_scores[self.nick])

    def test_not_update(self):
        add_scores = update_score(self.nick, self.new_score, self.scores)
        updates_scores = update_score(self.nick, self.old_score, add_scores)
        self.assertNotEqual(self.old_score, updates_scores[self.nick])

    def test_isinstance_update_score(self):
        updates_scores = update_score(self.nick, self.old_score, self.scores)
        self.assertIsInstance(updates_scores, dict,\
                                     'Must be instance of dict')

    def test_isinstance_sort_scores(self):
        updates_scores = update_score(self.nick, self.old_score, self.scores)
        sorted_scores = sort_scores(updates_scores)
        self.assertIsInstance(sorted_scores, list, 'Must be instance of list')

    def test_sorting_sort_scores(self):
        updates_scores = {'k': 1, 'l': 100, 'a': 50, 'c': 10, 'd': 40}
        not_sorted = [(key, value) for key, value in updates_scores.items()]
        sorted = sort_scores(updates_scores)
        try: self.assertListEqual(not_sorted, sorted)
        except AssertionError: pass
        else: self.fail('Lists must be not equal')
    

class RGBTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.rgb = rgb_to_hex(get_color())
    
    def test_rgb_is_str(self):
        self.assertIsInstance(self.rgb, str,\
                                     'Must be instance of str')

    def test_len(self) -> None:
        self.assertTrue(len(self.rgb) == 7)

    def test_startwith(self) -> None:
        self.assertEqual(self.rgb[0], '#')
 

class MoveTestCase(unittest.TestCase):
    def test_rotate_move(self):
        mock = Mock()
        mock.keysym = 'Up'
        rotate = move_obj(mock)
        self.assertTrue(rotate)

    def test_fast_fall_move(self):
        mock = Mock()
        mock.keysym = 'Down'
        anim_limit = move_obj(mock)
        self.assertEqual(100, anim_limit)

    def test_left_move(self):
        mock = Mock()
        mock.keysym = 'Left'
        x_moving = move_obj(mock)
        self.assertEqual(-1, x_moving)

    def test_right_move(self):
        mock = Mock()
        mock.keysym = 'Right'
        x_moving = move_obj(mock)
        self.assertEqual(1, x_moving)


class StopTestCase(unittest.TestCase):
    def test_app_run(self):
        self.assertFalse(stop())


class CloseTestCase(unittest.TestCase):
    def test_app_run(self):
        self.assertFalse(on_closing())
