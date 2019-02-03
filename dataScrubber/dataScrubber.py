import re
import random

INFILE = '/home/jrivera/Downloads/chj.txt'
OUTFILE = '/home/jrivera/Documents/chj.out.txt'
rx = re.compile(r'^(?P<cid>\d{16})')
card_dict = {}

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            m = rx.match(line)
            if m:
                cno = m.group('cid')
                nno = card_dict.get(cno)
                if not nno:
                    nno = str(random.randint(4000000000000000, 4999999999999999))
                    card_dict[cno] = nno
                line = line.replace(cno, nno)
            fout.write(line)