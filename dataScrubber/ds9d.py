# will scrubb issue day dates



import re
import random
import io
from datetime import datetime, timedelta

INFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-hp-bp-d1m.txt'
OUTFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-hp-bp-d1md.txt'

# RXDATE = re.compile(r'(?P<date>\d{2}\/\d{2}\/\d{2})')
acct_rx = re.compile(r'(\d{16}\s)')

IssueDate_dict = {}


new_number = ''

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            if acct_rx.match(line):
                new_number = str(random.randint(1,12))
                line = line[:73] + new_number + line[75:]
                fout.write(line)
            else:
                fout.write(line)






# def cd(self, add_days=900):
#     with open(INFILE, 'r') as fin:
#         with open(OUTFILE, 'w') as fout:
#             for line in fin:
#                 m = RXDATE.search(line)
#                 if m:
#                     Cd = m.group('date')
#                     Nd = IssueDate_dict.get(Cd)
#                 if not Nd:
#                     nline = io.StringIO(line)
#                 for Cd in re.finditer(RXDATE, line):
#                     _x = Cd.start('date')
#                     Nd = datetime.strptime(Cd.group('date'),'%m/%d/%y')
#                     nline.seek(_x)
#                     nline.write((Nd + timedelta(days=add_days)).strftime('%m/%d/%y'))
#                     line = nline.getvalue()
#                 else:
#                     fout.write(line)
