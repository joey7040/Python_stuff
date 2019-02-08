

import re
import random
import io
from datetime import datetime, timedelta

INFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-hp-bp.txt'
OUTFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-hp-bp-d1m.txt'

# RXDATE = re.compile(r'(?P<date>\d{2}\/\d{2}\/\d{2})')
acct_rx = re.compile(r'(\d{16}\s)')

IssueDate_dict = {}


new_number = ''

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            if acct_rx.match(line):
                new_number = str(random.randint(1,9))
                line = line[:70] + new_number + line[72:]
                fout.write(line)
            else:
                fout.write(line)

