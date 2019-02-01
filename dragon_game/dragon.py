import random
import time


def displayIntro():
    print('You are in the land of the dragons!')
    time.sleep(2)
    print('''In front of you, you see two caves.
    In one cave, a dragon lives and is friendly and will share his wisdom and trasures with you. In the other cave,
    a greedy and angry dragon lives and he will eat you on site!''', '\n')

def chooseCave():
    cave = " "
    while cave != '1' and cave != '2':
        print('which cave will you venture into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and....')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('Gives you a nice hello and shares his treasures and eternal wisdom with you')
    else:
        print('breathes fire down on you and scorches you like a bbq')

playAgain = 'yes'
while playAgain == 'yes' or playAgain =='y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    time.sleep(2)
    print('Do you want to play again? (yes or no)')
    playAgain = input()