import re

new_name = "TWEEDLE"
pattern = re.compile(r'\d+\,\d+\s(?P<name>(\S+\s)+)')
txt = '4,999 WADDELL                   819 012715 053118 000000       0.00      0 ZZZZZZZZZ00Z 2101 VB051099 01 F  V'
a_match = pattern.match(txt)

match_again = pattern.search(txt)

print(f'\nThe source string: \n\t\t{txt}\n\n')
print(f'\nthe match object looks like this: {a_match}')
if a_match:
   print(f'\nfound this: {a_match.group("name")}')

# We can use Python's String find() command on the original string to see where the matched group
# shows up, in order to nab it's starting index (location) in the original string
found_at = txt.find(a_match.group("name"))
print(f'\nthe group a_match.group("name") is located at index {found_at} in the source string')

len_of_match = len(a_match.group("name"))

new_str = f'{txt[0:found_at]}{new_name}{txt[found_at+len_of_match:]}'