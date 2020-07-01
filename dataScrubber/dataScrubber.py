import re
import random
# this will scrub acct nums in chj files
INFILE = '/home/jrivera/Documents/Python_stuff/BC460-29.txt'
OUTFILE = '/home/jrivera/Documents/out.txt'
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
                    card_dict[cno] = nnols
                line = line.replace(cno, nno)
            fout.write(line)
