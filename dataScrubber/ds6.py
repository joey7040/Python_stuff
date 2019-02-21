# will scrubb home phone numbers



import re
import random
import time

INFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corps-names.txt'
OUTFILE = '/home/jrivera/Documents/chj.scrubbed-acct-corp-names-phone.txt'

acct_rx = re.compile(r'(\d{16}\s)')
phone_dict = {}

new_number = ''

with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            if acct_rx.match(line):
                new_number = str(random.randint(8138470551, 8999999999))
                line = line[:46] + new_number + line[58:]
                fout.write(line)
            else:
                fout.write(line)




# open the file to be scrubbed
#   open the final destination file in write mode
#       for loop to read each 'line' in source file
#           if statement to search if regex pattern for an account number is found
#               # ...found a match!
#               <your code here> to replace the account numbers and slip back in the dashes
#               # ...notice that code for changing the phone and names about to be done next are
#               # ...contained in the for loop because only acct-no lines have names/numbers
#               # ...don't write out the line to the new file yet
#               <your name changing code here> applied to this line
#                    # ...notice we are still in the for loop that has read one line and we are working with that line still
#                 <your code to change phone #s> applied to this line
#                Now you can write the modified line out to the destination file
#           else
#               this line isn't an accout-no line, so write it to out file without changing it
#