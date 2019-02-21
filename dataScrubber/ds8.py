# will scrubb bus phones numbers



import re
import random
import time

INFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-phone.txt'
OUTFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-hp-bp.txt'

acct_rx = re.compile(r'(\d{16}\s)')
phone_dict = {}

new_number = ''

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            if acct_rx.match(line):
                new_number = str(random.randint(8138470551, 8999999999))
                line = line[:58] + new_number + line[70:]
                fout.write(line)
            else:
                fout.write(line)
