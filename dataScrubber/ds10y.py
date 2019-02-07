# will scrubb d2 year numbers



import re
import random
import time

INFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-hp-bp-d1mdy-d2m.txt'
OUTFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-hp-bp-d1mdy-d2my.txt'

acct_rx = re.compile(r'(\d{16}\s)')


new_number = ''

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            if acct_rx.match(line):
                new_number = str(random.randint(17,19))
                line = line[:86] + new_number + line[89:]
                fout.write(line)
            else:
                fout.write(line)
