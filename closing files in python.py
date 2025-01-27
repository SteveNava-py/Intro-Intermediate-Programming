# To delete a file in python

import os

def word_count(name):
    if type(name) is str and os.path.exists(name):
        f = open(name)
        line_count = 0
        word_count = 0
        character_count = 0
        for l in f:
            line_count = line_count + 1
            words = l.split()
            word_count = word_count + len(words)
            for w in words:
                character_count = character_count + len(w)
    print('Line count = ' + str(line_count) + ' Word Count = ' + str(word_count + " Character Count = " + str(character_count)))
    f.close()
