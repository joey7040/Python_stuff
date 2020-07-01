# will scrubb d2 month numbers
# note that you will need to add zeros to the month before moving to the next step!


import re
import random
import time

INFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-hp-bp-d1mdy.txt'
OUTFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-hp-bp-d1mdy-d2m.txt'

acct_rx = re.compile(r'(\d{16}\s)')


new_number = ''

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            if acct_rx.match(line):
                new_number = str(random.randint(1,9))
                line = line[:81] + new_number + line[83:]
                fout.write(line)
            else:
                fout.write(line)
