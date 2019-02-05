import re
import random
import time

INFILE = '/home/jrivera/Documents/chj.out2.txt'
OUTFILE = '/home/jrivera/Documents/chj.out3.txt'
NAMEFILE = '/home/jrivera/Documents/celebraties.txt'

onlyFirstNames = re.compile(r'^([^ \x21-\x26\x28-\x2C\x2E-\x40\x5B-\x60\x7B-\xAC\xAE-\xBF\xF7\xFE]+)$')
FirstAndLastNames = re.compile(r'^(([a-z]{1}[a-z]+([\-][a-z]{1}[a-z]+)?)([ ]([a-z]\.)){0,2}[ ](([a-z]{1}[a-z]*)|([O]{1}[\']{1}[a-z][a-z]{2,}))([ ](Jr\.|Sr\.|IV|III|II))?)$')
names_dict = {}

first_match = onlyFirstNames.match(INFILE.lower())
FirstAndLastNames_match = FirstAndLastNames.match(INFILE.lower())

first_match_again = onlyFirstNames.search(INFILE.lower())
FirstAndLastNames_match_again = FirstAndLastNames.search(INFILE.lower())




# to add some user interface kinda

# print('Now getting file to scrub')
# time.sleep(2)
# print('Now Scrubbing some stuff')
# time.sleep(2)
# print('finished scrubbing')



of = open(NAMEFILE, 'r')
celebNames = []
for line in iter(of):
    a_lister = line
    loc = a_lister.find('(')
    a_lister = a_lister[:loc]
    a_lister = a_lister + '\n'
    celebNames.append(a_lister)
of.close()
# print(celebNames)


def randomCeleb():
  return random.choice(celebNames)

print(random.choice(celebNames))

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            m = onlyFirstNames.search(line)
            fnl = FirstAndLastNames.search(line)
            if m:
                cno = m.find(onlyFirstNames)
                nno = names_dict.get(cno)
                if not nno:
                    nno = randomCeleb()
                    names_dict[cno] = nno
                line = line.replace(cno, nno)
            elif fnl:
                cno = fnl.find(FirstAndLastNames)
                nno = names_dict.get(cno)
                if not nno:
                    nno = randomCeleb()
                    names_dict[cno] = nno
                line = line.replace(cno, nno)
                fout.write(line)
# scrubes name 
