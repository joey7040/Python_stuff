# will scrubb phone numbers



import re
import random
import time

INFILE = '/home/jrivera/Documents/Python_stuff/BC460-29.txt'
OUTFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-phone.txt'



with open (INFILE, 'r') as f:
    f_contents = f.read()
    print(f_contents)