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

# character

class character:

    inventory = None

    Type = None
    maxHealth = None
    currentHealth = None
    
    meleeDamage = None
    rangedDamage = None
    magicDamage = None

    meleeDefence = None
    rangedDefence = None
    magicDefence = None
    
    def Inventory(self):

        #for i in range(len(self.inventory)):

            #for j in range(len(self.inventory))[i]:

                #if i == 0:

                    #print("")

                #print(self.inventory[i][j])




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

    def __init__(self, Type, health, damage, defence, startingItems):

        self.inventory = startingItems

        self.Type = Type

        self.meleeDefence, self.rangedDefence, self.magicDefence = defence[0], defence[1], defence[2]

        self.currentHealth = self.maxHealth = self.dificultyModifier(health, dificulty, False)


        self.meleeDamage = self.dificultyModifier(damage[0], dificulty, False)
        self.rangedDamage = self.dificultyModifier(damage[1], dificulty, False)
        self.magicDamage = self.dificultyModifier(damage[2], dificulty, False)

# enemys

class enemys:

    maxHealth = None
    currentHealth = None

    meleeDamage = None
    rangedDamage = None
    magicDamage = None

    meleeDefence = None
    rangedDefence = None
    magicDefence = None

    distance = None

    def displayRange(self, slotNum):

        if slotNum == self.distance:

            return "\033[1;31;40mX\033[0m"

        else:

            return " "

    def __init__(self, health, damage, defence, startRange):
        
        self.distance = startRange

        self.currentHealth = self.maxHealth = health

        self.meleeDamage, self.rangedDamage, self.magicDamage = damage[0], damage[1], damage[2]

        self.meleeDefence, self.rangedDefence, self.magicDefence = defence[0], defence[1], defence[2]

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

    knightLoadout = [
        # name, item type, d/heal, crit%, crit multiplier
        ["biff's sword", "weapon", 25, 0.05, 2],
        ]

    player = character(" knight", 150, (45, 5, 0), (0.7, 1.1, 1), knightLoadout)

elif characterSelect == "2":

    player = character(" barbarian", 120, (35, 15, 0), (0.9, 1.1, 1))

elif characterSelect == "3":

    player = character("n archer", 80, (5, 55, 0), (1.3, 0.9, 1))
    
elif characterSelect == "4":

    player = character(" mage", 60, (0, 0, 70), (1, 1, 1))

sleep(2)
clear()

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
your journey as a{player.Type} begins
in your grandmothers house''')

sleep(4)
clear()

print("level 1\n\nas you walk out the house you come across an enemy\n")

grandmother = enemys(100, (20, 20, 0), (1, 1, 1), 0)
sleep(1.5)

print("YOUR GRANDMOTHER")

sleep(1)

while True:

    clear()

    print('       ___ \n      (___) \n     /`   `\ \n    /  /"\  \ \n    \_/o o\_/ \n     (  _  ) \n      `\ /` \n     /\\\V//\ \n    / /_ _\ \ \n    \ \___/ / \n     \/===\/ \n     ||   || \n     ||   || \n     ||___|| \n     |_____| \n       ||| \n      / Y \ \n      `"`"`')

    choice = input(f"""+-----------------------+
| 0 = player, \033[1;31;40mX\033[0m = enemy | your health: {player.currentHealth}    their health: {grandmother.currentHealth}
|      ___________      |
|     /   _____   \     |
|    /   /     \   \    |
|   |   |   0 {grandmother.displayRange(0)} | {grandmother.displayRange(1)} | {grandmother.displayRange(2)} |
|    \   \_____/   /    |
|     \___________/     |
|                       |
+-----------------------+
|  a/away to move away  |
|t/toward to move toward|
|    i for inventory    |
+-----------------------+
>>""")
    if choice.lower() == "t" or choice.lower() == "toward":
        
        if grandmother.distance == 0:

            print("cannot move any closer")
            sleep(2)
            continue

        else:

            grandmother.distance -= 1
            continue

    elif choice.lower() == "a" or choice.lower() == "away":
        
        if grandmother.distance == 2:

            print("you attempt to run away but a mysterious force is preventing you")
            sleep(2)
            continue

        else:

            grandmother.distance += 1
            continue

    elif choice.lower() == "i":
    
        player.Inventory()
        continue