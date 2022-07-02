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
    NotImplemented


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

class MoveXTestCase(unittest.TestCase):
    NotImplemented


class MoveYTestCase(unittest.TestCase):
    NotImplemented


class RotateTestCase(unittest.TestCase):
    NotImplemented  


class MoveTestCase(unittest.TestCase):
    NotImplemented


class CheckBordersTestCase(unittest.TestCase):
    NotImplemented


class CheckLinesTestCase(unittest.TestCase):
    NotImplemented


class GameOverTestCase(unittest.TestCase):
    NotImplemented


class ClosingTestCase(unittest.TestCase):
    NotImplemented


class StartGameTestCase(unittest.TestCase):
    NotImplemented


class StartTestCase(unittest.TestCase):
    NotImplemented


class StopTestCase(unittest.TestCase):
    NotImplemented