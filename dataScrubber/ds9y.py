# will scrubb issue year dates



import re
import random
import io
from datetime import datetime, timedelta

INFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-hp-bp-d1md.txt'
OUTFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-hp-bp-d1mdy.txt'


acct_rx = re.compile(r'(\d{16}\s)')

IssueDate_dict = {}


new_number = ''

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            if acct_rx.match(line):
                new_number = str(random.randint(17,19))
                line = line[:76] + new_number + line[79:]
                fout.write(line)
            else:
                fout.write(line)

