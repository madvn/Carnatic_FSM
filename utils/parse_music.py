'''
code that parses files copy pasted from patantara
and overwrites out music21 usable files

Madhavun Candadai
Jan, 2018
'''

import sys
from conversion import *

def parse_music(filename):

    try:
        parsed_music = ''
        for line in open(filename):
            print(line)
            for char in line:
                parsed_music += note_conversion[char]+' '
            parsed_music += '\n'
    except Exception as e:
        print(e)

    f = open(filename,'w')
    f.write(parsed_music)
    f.close()


if __name__ == '__main__':
    parse_music(filename)
