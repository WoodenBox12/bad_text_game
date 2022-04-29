from random import randint
from os import system, name
from time import sleep

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# characters

class character:

    maxHealth = None
    meleeDamage = None
    rangedDamage = None
    magicDamage = None
    Type = None

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

    def __init__(self, Type, health, melee_damage, ranged_damage, magic_damage):

        self.Type = Type

        self.maxHealth = self.dificultyModifier(health, dificulty, False)

        self.meleeDamage = self.dificultyModifier(melee_damage, dificulty, False)
        self.rangedDamage = self.dificultyModifier(ranged_damage, dificulty, False)
        self.magicDamage = self.dificultyModifier(magic_damage, dificulty, False)

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

    character = character(" knight", 150, 55, 5, 0)

elif characterSelect == "2":

    character = character(" barbarian", 120, 45, 15, 0)

elif characterSelect == "3":

    character = character("n archer", 80, 5, 55, 0)
    
elif characterSelect == "4":

    character = character(" mage", 60, 10, 10, 40)


sleep(2)
clear()

print(character.maxHealth)
print(character.meleeDamage)
print(character.rangedDamage)
print(character.magicDamage)

print (f'''
                                  _
                      .=========.%88,
                     /_,-.___.-._\88%
                   o8| [_]/o\[_] |7'
               i=I8%@|____|_|____|I=I=I=i
              |/,*`*,*`**'/ \      ,-'`.\|
             |/          /...\   (__.-._)\|
             ||||||||||||TTTTT|||||||||||||
             """"""""""""HHHHH"""""""""""""
             your journey as a{character.Type} begins
''')