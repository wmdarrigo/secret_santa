import random
import os


def clear(): return os.system('cls')


class Player:
    def __init__(self, name):
        self.name = name

    def message(self, name_selected):
        print('Hi ' + self.name + ', you are...')
        print('')
        input('(Hit enter to see!)')
        print('')
        print('Hi ' + self.name + ', you are ' +
              name_selected + '\'s secret santa!')
        print('')
        input('(Hit enter for next player)')
        clear()


print("Welcome to Secret Santa!")
print()
num_players = int(input("How many players are playing? "))
print()

santas = list()  # generate empty list to store objects

for x in range(num_players):
    print("Player " + str(x + 1))
    name = input("Name: ")
    santas.append(Player(name))

clear()

# randomizes players
random.shuffle(santas)
# created an empty jar which will hold each player's name
jar = list()

for santa in santas:
    jar.append(santa.name)

# shake jar
random.shuffle(jar)

# santas represent the actual players
# jar holds the names of the players
# jar[0] represents the name selected from the jar
# santas may not select their own name in the jar
for santa in santas:
    if santa.name is not jar[0]:
        santa.message(jar[0])
        jar.remove(jar[0])
    else:
        santa.message(jar[1])
        jar.remove(jar[1])
    random.shuffle(jar)

print("Done!")
