'''
Exceptions.py.
File containing custom exceptions of app.  
=========================================

'''

from random import choice, randrange

class GameOver(Exception):
    '''Class exception which completes the game session and
       update file "Scores.txt".
    '''
    def __init__ (self, nickname: str, score: int):
        self.nickname = nickname
        self.score = score

    def score_update(self):
        ''' The method which update data in score file. '''

        with open('Scores.txt', 'r') as score_file_r:
            # An explanation for the horrible incomprehensible construction below.
            #
            # Disassemble in dict comprehension into a string file that already
            # consisted of dict, and build a new dict from these strings.
            old_scores = {(line.split(' : ')[1]).split(': ')[0].strip() : \
                int((line.split(' : ')[1]).split(': ')[1]) for line in score_file_r}
            if self.nickname in old_scores.keys():
                if self.score > old_scores.get(self.nickname):
                    old_scores.update([(self.nickname, self.score)])
            else:
                old_scores.update([(self.nickname, self.score)])
            # We turn the dict into a list for sorting data in it
            # by our special sorting system.
            old_scores_list = [(key, value) for key, value in old_scores.items()]
            old_scores_list.sort(key=lambda item: item[1], reverse=True) 

            # Now we overwrite our file to make changes.
            with open('Scores.txt', 'w') as score_file_w:
                # Creates new dict with updated and sorted data
                new_scores = {item[0] : int(item[1]) for item in old_scores_list}

                # Put our dict in a file
                for idx, (key, value) in enumerate(new_scores.items()):
                    score_file_w.write(f'№{idx + 1} : {key}: {value} \n')

    def __str__ (self):
        return 'Game Over'

class Quit(Exception):
    '''Class exception which closes the program.'''

    def __str__ (self):
        return 'Good Bye!'