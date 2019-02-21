# scrubes acct/card numbers with dashes

import re
import random
import time

INFILE = '/home/jrivera/Documents/Python_stuff/BC460-29.txt'
OUTFILE = '/home/jrivera/Documents/chj.scrubbedAcct.txt'
acct = re.compile(r'^(?P<cid>\d{4}\-\d{4}\-\d{4}\-\d{4})')
acct_dict = {}



with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            m = acct.match(line)
            if m:
                cno = m.group('cid')
                nno = acct_dict.get(cno)
                if not nno:
                    nno = str(random.randint(4000000000000000, 4999999999999999))
                    # acct_dict[cno] = nno #this looks to see if a exisiting key value pair 
                line = line.replace(cno, nno)
            fout.write(line)



