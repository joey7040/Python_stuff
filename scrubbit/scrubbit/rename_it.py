import os

# takes source of names from a wikipedia dump and strips of dates to leave names
# then saves to a text files for use elsewhere
# assumes file has one line per composer, with dates and other info following names in parentheses, like this:
# examples:
#           Maestro Piero (before 1300 – c. 1350)
#           Gherardello da Firenze (c. 1320/1325 – c. 1362)


filename = "ItalianComposersOrig.txt"

f = open(filename, 'r')
composerNames = []
for line in iter(f):
    a_name = line

    #strip off all but name
    loc = a_name.find('(')
    a_name = a_name[:loc]
    a_name = a_name + '\n'

    composerNames.append(a_name)
f.close()

#create a new file with the names only
f2 = "composerNames.txt"
a_new_file = open(f2,'w')
for i in composerNames:
    a_new_file.write(i)
a_new_file.close()

