import re
import random
import time

INFILE = '/home/jrivera/Documents/chj.out.txt'
OUTFILE = '/home/jrivera/Documents/chj.out2.txt'
corp = re.compile(r'CORP\s(?P<corpnumber>\d{6})')
rx = re.compile(r'^(?P<cid>\d{16})')
corp_dict = {}
card_dict = {}



print('Now getting file to scrub')
time.sleep(2)
print('Now Scrubbing some stuff')
time.sleep(2)
print('finished scrubbing')




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