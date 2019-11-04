# writes the month

import re
import random
import io
from datetime import datetime, timedelta

INFILE = '/home/jrivera/Downloads/501lp/lp501.txt'
OUTFILE = '/home/jrivera/Downloads/501lp/lp510-01.12.txt'


acct_rx = re.compile(r'XXXXXXXXXXXX\d{4}')

IssueDate_dict = {}


new_number = ''

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            if acct_rx.match(line):
                new_number = str(random.randint(1000,90000))
                line = line[:25] + new_number + line[32:]
                fout.write(line)
            else:
                fout.write(line)