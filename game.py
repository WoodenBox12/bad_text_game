from random import randint
from os import system, name
from time import sleep
import bad_text_game.classes.py as mymodule

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# characters

class character:

    Type = None
    maxHealth = None

    meleeDamage = None
    rangedDamage = None
    magicDamage = None

    meleeDefence = None
    rangedDefence = None
    magicDefence = None

    def dificultyModifier(self, baseValue, dificulty, increase):

        if increase == True :
            
            if dificulty == 1 :
                return baseValue

            elif dificulty == 5 :
                return int(round(baseValue * 1.4, 0))

            elif dificulty == 4 :
                return int(round(baseValue * 1.3, 0))

            elif dificulty == 3 :
                return int(round(baseValue * 1.2, 0))

            elif dificulty == 2 :
                return int(round(baseValue * 1.1, 0))

        elif increase == False :

            if dificulty == 1 :
                return baseValue

            elif dificulty == 5 :
                return int(round(baseValue * 0.6, 0))

            elif dificulty == 4 :
                return int(round(baseValue * 0.7, 0))

            elif dificulty == 3 :
                return int(round(baseValue * 0.8, 0))

            elif dificulty == 2 :
                return int(round(baseValue * 0.9, 0))

        else:
            return baseValue

    def __init__(self, Type, health, damage, defence):

        self.Type = Type

        self.meleeDefence = defence[0]
        self.rangedDefence = defence[1]
        self.magicDefence = defence[2]

        self.maxHealth = self.dificultyModifier(health, dificulty, False)

        self.meleeDamage = self.dificultyModifier(damage[0], dificulty, False)
        self.rangedDamage = self.dificultyModifier(damage[1], dificulty, False)
        self.magicDamage = self.dificultyModifier(damage[2], dificulty, False)

# dificulty select

dificulty = input("select dificulty between 1 and 5 or random: ")

if dificulty.upper() == "RANDOM":

    dificulty = randint(1,5)

else:
    try:

        if type(int(dificulty)) == int:
    
            if 1 <= int(dificulty) <= 5:

                dificulty = int(dificulty)

            else:

                dificulty = randint(1,5)

    except:

        dificulty = randint(1,5)

sleep(2)
clear()

# choose starter weapon

characterSelect = input("select player class\n1 for knight\n2 for barbarian\n3 for archer\n4 for mage\n>> ")

if characterSelect == "1":

    character = character(" knight", 150, (45, 5, 0), (0.7, 1.1, 1))

elif characterSelect == "2":

    character = character(" barbarian", 120, (35, 15, 0), (0.9, 1.1, 1))

elif characterSelect == "3":

    character = character("n archer", 80, (5, 55, 0), (1.3, 0.9, 1))
    
elif characterSelect == "4":

    character = character(" mage", 60, (0, 0, 70), (1, 1, 1))


sleep(2)
clear()

print(character.maxHealth)
print(character.meleeDamage)
print(character.rangedDamage)
print(character.magicDamage)

print(character.meleeDefence)
print(character.rangedDefence)
print(character.magicDefence)

print (f'''
                                  _
                      .=========., |
                     /_,-.___.-._\ |
                     | [_]/o\[_] |7'
               i=I=I=|____|_|____|I=I=I=i
              |/,*`*,*`**'/ \      ,-'`.\|
             |/          /...\   (__.-._)\|
             ||||||||||||TTTTT|||||||||||||
             """"""""""""HHHHH"""""""""""""
            your journey as a{character.Type} begins
               in your grandmothers house
''')

sleep(4)

