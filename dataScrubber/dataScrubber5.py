import re
import random
import time

INFILE = '/home/jrivera/Documents/chj.out2.txt'
OUTFILE = '/home/jrivera/Documents/chj.out3.txt'
names = re.compile(r'FIRST:\s(?P<first_name>\S+)\s+LAST:\s(?P<last_name>)')

names_dict = {}




print('Now getting file to scrub')
time.sleep(2)
print('Now Scrubbing some stuff')
time.sleep(2)
print('finished scrubbing')




with open(INFILE) as cin:
    with open(OUTFILE, 'w') as cout:
        for line in cin:
            m = names.search(line)
            if m:
                cno = m.group('<first_name>', 'last_name')
                nno = names_dict.get(cno)
                if not nno:
                    nno = str(random.randint(10000, 19999))
                    names_dict[cno] = nno
                line = line.replace(cno, nno)
            cout.write(line)