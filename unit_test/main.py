from classes.validator import validator
import sys

username = sys.argv[1]

validator = validator()

if validator.user_is_valid(username):
    print('the username you chose is valid')
else:
    print('the username you chose is invalid')
