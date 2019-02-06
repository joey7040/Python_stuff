import re
import random
demo_acct_rx = re.compile(r'(\d{4}\-\d{4}\-\d{4}\-\d{4})')       # escape out the dash like this \-
line = '1234-1234-1234-1234  BLAH BLAH BLAH'
print(line)
if demo_acct_rx.search(line):
   new_num = str(random.randint(4000, 9999))
   line = line[:15] + new_num + line[19:]
   print(line)