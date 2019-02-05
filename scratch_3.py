import re
import random

INFILE = 'chj.txt'
OUTFILE = 'chj.out.txt'
NAMEFILE = 'celebraties.txt'

acct_rx = re.compile(r'(\d{16}\s)')

# Build your celebrity names list from the file
celebNames = []
with open(NAMEFILE, 'r') as file_in:                                    # with...open is the best practices file read/write convention, typically :)
    for line in file_in:
        celebNames.append(line.rstrip())                                #rstrip removes the trailing newline
#    print(celebNames)


new_name = ''
# Open the source (in) file and the final output (fout) file
with open(INFILE) as fin:
    with open(OUTFILE, 'w') as fout:
        for line in fin:
            # in the CHJ file, the names always begin at 56 and end at 79... this suggests you don't need regex to find _where_ to put the new names; 'tis known!
            # so, you only need to know if you are on a line that needs a name...
            # seems that if a line begins with a 16 digit number, it's a line that will need a new name!
            # so use a regex to find any line that begins with 16 digits, such as \d{16}\s

            if acct_rx.match(line):                                     # this is looking only for matches to acct_rx (it will ignore all other lines)
                print(f'ORIG - {line}')                                 # for debugging - delete later
                # we have an account line... now work the magic
                new_name = random.choice(celebNames).upper()            # in this report, all names are in uppercase; make it so!
                #make sure the new name is not too long
                if len(new_name) > 23:                                  # we know 23 is length of longest name allowed by evaluating the space allotted for names in the source file
                    # print(f'long: {new_name}')                        # for debugging - delete later
                    new_name = new_name[:23]                            # name is too long: truncate the name
                elif len(new_name) < 23:
                    new_name = new_name.ljust(23)                       # name is too short: add spaces to end of name
                    # print(f'trunc.: {new_name}')                      # for debugging - delete later
                # now re-write the line with the new name in it
                line = line[:56] + new_name + line[79:]

                print(f'NEW  - {line}')                                 # for debugging - delete later

                fout.write(line)
            else:
                fout.write(line)                                        # if the pattern wasn't found, this will write out the line from the source file to the out file with no changes