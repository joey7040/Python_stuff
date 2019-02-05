import re
import random
import time

INFILE = '/home/jrivera/Downloads/chj.txt'
OUTFILE = '/home/jrivera/Documents/chj.out.txt'
acct = re.compile(r'^(?P<cid>\d{16})')
# corp = re.compile(r'CORP\s+(\d{6})')
acct_dict = {}
# corp_dict = {}

print('Now getting file to scrub')
time.sleep(2)
print('Now Scrubbing some stuff')
time.sleep(2)
print('finished scrubbing')

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            m = acct.match(line)
            if m:
                cno = m.group('cid')
                nno = acct_dict.get(cno)
                if not nno:
                    nno = str(random.randint(4000000000000000, 4999999999999999)+1)
                    acct_dict[cno] = nno
                line = line.replace(cno, nno)
            fout.write(line)



# scrubes acct/card numbers