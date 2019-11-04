import re
import random
import io
from datetime import datetime, timedelta

INFILE = '/home/jrivera/Documents/BC460-29-Scrubbed/BC460-29.7.txt'
OUTFILE = '/home/jrivera/Documents/BC460-29-Scrubbed/BC460-29.12.07.2018.txt'


acct_rx = re.compile(r'(\d{16}\s)')

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            if acct_rx.match(line):
                new_number = str(random.randint(1,900))
                line = line[:113] + new_number + line[117:]
                fout.write(line)
            else:
                fout.write(line)