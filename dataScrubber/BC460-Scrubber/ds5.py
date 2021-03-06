# scrubes name of chj files and uses celeb names

import re
import random
import time

# INFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corps.txt'
INFILE = '/home/jrivera/Downloads/BC460-29.txt'
OUTFILE = '/home/jrivera/Documents/BC460-29-names.txt'
NAMEFILE = '/home/jrivera/Documents/celebraties.txt'

acct_rx = re.compile(r'(\d{16}\s)')




celebNames = []
with open(NAMEFILE, 'r') as file_in:
    for line in file_in:
        celebNames.append(line.rstrip())     



new_name = ''

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            if acct_rx.match(line):
                new_name = random.choice(celebNames).upper()
                if len(new_name) > 23:
                    new_name = new_name[:23]
                elif len(new_name) < 23:
                    new_name = new_name.ljust(23)                       
                line = line[:23] + new_name + line[40:]
                fout.write(line)
            else:
                fout.write(line)