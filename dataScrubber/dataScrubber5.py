import re
import random
import time

INFILE = '/home/jrivera/Documents/chj.out2.txt'
OUTFILE = '/home/jrivera/Documents/chj.out3.txt'
NAMEFILE = '/home/jrivera/Documents/celebraties.txt'

acct_rx = re.compile(r'(\d{16}\s)')

# to add some user interface kinda

# print('Now getting file to scrub')
# time.sleep(2)
# print('Now Scrubbing some stuff')
# time.sleep(2)
# print('finished scrubbing')


celebNames = []
with open(NAMEFILE, 'r') as file_in:
    for line in file_in:
        celebNames.append(line.rstrip())     
# print(celebNames)



print(random.choice(celebNames))


new_name = ''

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            if acct_rx.match(line):
                new_name = random.choice(celebNames).upper()
                if len(new_name) > 23:
                    new_name = new_name[:23]
                elif len(new_name) < 23:
                    new_name = new_name.ljust(23)                       
                line = line[:56] + new_name + line[79:]
                fout.write(line)
            else:
                fout.write(line)
# scrubes name 
