import hashlib

def pass_attack(password_hash): 

    dictionary = ['password', 123456, 'ilikejoe', 'Downwood2', 'flamingoKiller']

    password_found = False

    for dictionary_value in dictionary:
        hash_value = (hashlib.md5(dictionary_value)).hexdigest()``
        if hash_value == password.hash:
            password_found == True
            recovered_password = dictionary_value

    if password_found == True:
        print("found match fo hashed value \n"),password_hash
        print("password recovered: "),recovered_password
    else:
        print("password was not found in my dictionary")

def main():
    password_hash = str(input('enter hashed password:  '))
    pass_attack(password_hash)

if __name__ == '__main__':
    main()