# scrubbes corp number at the top of chj files.

import re
import random
import time

INFILE = '/home/jrivera/Documents/chj.scrubbedAcct.txt'
OUTFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corps.txt'
corp = re.compile(r'CORP\s(?P<corpnumber>\d{6})')

corp_dict = {}
card_dict = {}



with open(INFILE) as cin:
    with open(OUTFILE, 'w') as cout:
        for line in cin:
            m = corp.search(line)
            if m:
                cno = m.group('corpnumber')
                nno = corp_dict.get(cno)
                if not nno:
                    nno = str(random.randint(10000, 19999))
                    corp_dict[cno] = nno
                line = line.replace(cno, nno)
            cout.write(line)
