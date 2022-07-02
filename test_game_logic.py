''' This file contains tests for the Game_logic.py file.
    It tests all functions in Game_logic.py file.

'''

import unittest
from unittest.mock import Mock

from Game_logic import *


mock = Mock()


class NickTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        user_input = mock.user_input
        user_input.create_nick.side_effect = ['кирилл', '1234567891011',]
        self.user_input = user_input.create_nick() 

    def test_len(self) -> None:
        self.assertFalse(validate_len_nick(self.user_input))

    def test_char(self) -> None:
        self.assertFalse(validate_char_nick(self.user_input))



class ScoreTestCase(unittest.TestCase):
    NotImplemented


class RGBTestCase(unittest.TestCase):
    NotImplemented


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