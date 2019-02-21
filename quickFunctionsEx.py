

def say_hello(name='NAME'):
    print('Hello '+ name)

say_hello('Joey')

def motivation():
    print("We all apprechiate all that you do and that you are working so hard. We are very pleased to have you as a part of our company and want to give you a raise")

def dog_string(mystring):
    return 'dog' in mystring.lower()

def pig_latin(word):
    first_letter = word[0] 
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1] + first_letter + 'ay'
    return pig_word

def if_word_even(string):
    for word in string.split():
        if len(word) % 2 == 0:
            print(word+' is even!')

def fizzbuzz():
    for num in range(1,101):
        if num%3 == 0 and num%5 == 0:
            print('fizzbuzz')
        elif num%3 == 0:
            print('fizz')
        elif num%5 == 0:
            print('buzz')


def sum_finder(a,b):
    return a+b

def multiply(a,b):
    return a*b

def myfunc(a,b,c=0):
    return sum(a,b,c)* 0.085

# *args allows you to take any number of arguments

def newfunc(*args):
    return sum( args)* 0.5
#similarly python has **kwargs that allows you to use any number of keyword arguments
def keyworded(**kwargs):
    if 'fruit' in kwargs:
        print('my {}'.format(kwargs['fruit'])+ 's bring all the boys to the yard')
    else:
        print('No fruits found bro....')

def bigChungus(C):
    for C in range(0,1000):
        C = C+1
