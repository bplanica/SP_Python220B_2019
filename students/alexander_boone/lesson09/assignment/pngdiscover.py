'''
HP Norton keeps pictures of all their furniture in png files
that are stored on their file server. They have a very crude
program that starts by discovering all directories on the
server and then looking in each of those for the png files.
They have discovered a problem, though: png files are not
found when they are stored in directories that are more than
one level deep from the root directory. Your job is to write
a png discovery program in Python, using recursion, that works
from a parent directory called images provided on the command line.
The program will take the parent directory as input. As output, it
will return a list of lists structured like this:
[“full/path/to/files”, [“file1.png”, “file2.png”,…],...]
'''

import os
import pprint

PATH = "./data/"


def png_discover(path):
    '''Recursively searches for png files in directories in path.'''
    png_list = []
    for root, d_names, f_names in os.walk(path):
        if f_names:
            f_names = [name for name in f_names if '.png' in name]
            png_list.append(root)
            png_list.append(f_names)
    return png_list


PNG_LIST = png_discover(PATH)
pprint.pprint(PNG_LIST)
