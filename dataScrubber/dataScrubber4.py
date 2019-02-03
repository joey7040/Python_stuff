import re
pattern = re.compile(r'\d+\,\d+\s(?P<name>(\S+\s)+)')
txt = '4,999 WADDELL                   819 012715 053118 000000       0.00      0 ZZZZZZZZZ00Z 2101 VB051099 01 F  V'
a_match = pattern.match(txt)

print(f'parsing the string {txt[6:26]}')
print(a_match)
if a_match:
   print(a_match.group('name'))