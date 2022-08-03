THE GAME "Tetris"

Author: Key27
Game version: 0.2

============================================================================================================
DESCRIPTION:

The program is a simple implementation of the graphical version of the "Tetris" game, in the programming 
language Python, using the GUI package Tkinter. Also sometimes had to use an additional package Pillow
this package is listed in the requirements.txt file and you must download it. The instruction will be below. 

============================================================================================================
REQUIREMENTS:

    Programing Language
Python Version 3.10
    Third party package:
Pillow 9.1.1
    GUI built in Python:
Tkinter 8.6
    Modules built in Python:
Copy
Random

============================================================================================================
COMPOSITION:

    Files  *.py
Game_logic.py - is a file with a main logic of the game.
Gui.py - is a file with logic display of a graphical interface.
Settings.py - a file with constants and main window settings.
Tetris.py - is a file that runs the application. 

Tetris.py.lnk - Tetris.py file shortcut. 

    Files  *.txt
File Scores.txt - saves all players scores. 
File requirements.txt - saves all dependencies.
File README.txt -contains project description. You read it now by the way :)

    Directories
IMG directory - saves all the pictures for the game.
Font direcory - saves a caste Font for the game.

============================================================================================================
HOW TO INSTALL CORRECTLY

Create a virtual environment.
Create a folder to move to it in the console, write a command:
"Python3 -m venv (name of the virtual environment)", to create a virtual
environment.

Activate it.
Go to the Scripts directory in the terminal with the command:
"cd venv/Scripts", and write next command: "activate".

Unzip the archive to this folder near folder venv. Before launching the game
after downloading all game files to the virtual environment, be sure to set
the dependencies on the requirements.txt. In cmd terminal, already in the 
virtual environment for install all dependencies.

============================================================================================================
PROGRAM MANAGEMENT

Button "START" in menu - start the game.
Button "STOP" - stop the game immediately.
Button "QUIT" - quit the program.

Key: "Right arrow" - move the figure to the right by one cell.
Key: "Left arrow" - move the figure to the left by one cell.
Key: "Up arrow" - turn the figure once.
Key: "Down arrow" - add the speed of the fall of the figure.

============================================================================================================
PAY ATTENTION!
The progam for each game session asks user for a nickname in the console
window. Enter the name and press "ENTER" and then the game will start. 
The delay of in seconds after the introduction of a nickname will allow you
to switch between windows and start the game on timely manner.

============================================================================================================
GAMEPLAY
For knocking out 1 line, the game has 10 points, for knocking out.
2 lines at once - 30 points.
3 lines at once - 70 points.
4 lines at once - player get 120 points.
After each knocked line, the figures fall faster. 

When the field is filled with figures to the top, the game is over.

============================================================================================================
TESTS
The code is 60% covered by tests.
============================================================================================================
