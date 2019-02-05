import re
import random
import time

INFILE = '/home/jrivera/Documents/chj.out2.txt'
OUTFILE = '/home/jrivera/Documents/chj.out3.txt'
NAMEFILE = '/home/jrivera/Documents/celebraties.txt'


with open (NAMEFILE, 'r') as f:
    f_contents = f.read()
    print(f_contents)