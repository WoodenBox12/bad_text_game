from random import randint, random
from os import system, name
from time import sleep
from typing import Container



#game made by woodenbox12

# todo 

# quantity count for inventory
# make attacking work
# make infinite eventially

# early weapon

riosHeel = ["Rio's High Heel", "melee/ranged", 50, 5, 2]

walshxacker = ["Walsh Whacker", "melee", 40, 10, 3]

mattsshortbarreler = ["Matt's Short Barreler", "ranged", 44, 4, 4]

jacksrifle = ["Jack's Left Handed Rifle", "melee/ranged", 100, 50, -1]

ollyscube = ["Olly's GAN", "melee/magic", 60, 20, 3]

lillyspersonality = ["Lilly's Personality", "magic", 40, 60, 2]

liamsfry = ["Liams Frying Pan", "melee", 35, 5, 3]


#mid game


jimmyStick = ["Jimmy's Stick", "melee/ranged", 250, 50, 3]

elliottscalculator = ["Elliott's Calculator", "magic", 50, 10, 42]

rishabhsorb = ["Rishabh's Orb", "magic", 75, 60, 1.2]

deviousBlade = ["Devious Blade", "melee/ranged/magic", 420, 50, 69] # cheats only

dan = ["Dan's Weapon", "ranged", 0, 0, 0]


def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def red(string):
    return f"\033[1;31;40m{string}\033[0m"

def removeChars(string, badChars):
    for char in badChars:
	    string = string.replace(char, "")
    return string
# character

def dificultyModifier( baseValue, dificulty, increase):

        if increase == True :
            
            if dificulty == 1 :
                return baseValue

            elif dificulty == 5 :
                return int(round(baseValue * 1.2, 0))

            elif dificulty == 4 :
                return int(round(baseValue * 1.15, 0))

            elif dificulty == 3 :
                return int(round(baseValue * 1.1, 0))

            elif dificulty == 2 :
                return int(round(baseValue * 1.05, 0))

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

class character:

    inventory = None
    mainWeapon = None

    Type = None
    maxHealth = None
    currentHealth = None

    meleeDefence = None
    rangedDefence = None
    magicDefence = None
    
    def Inventory(self):

        clear()
            
        weaponTypes = ("    damage type: ", "    damage: ", "    crit %: ", "    crit multiplier: ", "")

        print("items in backpack:\n")

        for i in range(len(self.inventory)):

            if self.inventory[i][1] != "heal":

                for j in range(len(self.inventory[i])):


                    if j == 5:
                        break

                    print(self.inventory[i][j], end=weaponTypes[j])

                print()

        print("\nheals:\n")

        for i in range(len(self.inventory)):

            if self.inventory[i][1] == "heal":

                print(self.inventory[i][0], end="    ")
                print(f"health gain: {self.inventory[i][2]}")
            

        choice = input(f"""
main weapon is {self.mainWeapon[0]}
+----------------------------------------------------+
| to change your main weapon type:    mw weapon-name |
| to use a heal type:                  use item-name |
+----------------------------------------------------+
>>""").lower()

        if "mw" in choice:

            choice = choice[3:]
            choice = removeChars(choice, "' ")

            for i in range(len(self.inventory)):

                name = removeChars(self.inventory[i][0].lower(), "' ")

                if choice == name:
                    
                    self.mainWeapon = self.inventory[i]

            input(f"main weapon is now {self.mainWeapon[0]}")

        elif "use" in choice:

            choice = choice[4:]
            choice = removeChars(choice, "' ")

            for i in range(len(self.inventory)):

                name = removeChars(self.inventory[i][0].lower(), "' ")

                if choice == name:
                    
                    if self.currentHealth == self.maxHealth:

                        print("already on max health")
                        sleep(2)
                        break

                    elif self.currentHealth + self.inventory[i][2] > self.maxHealth:

                        self.currentHealth = self.maxHealth
                        self.inventory.pop(i)
                        
                    else:

                        self.currentHealth += self.inventory[i][2]
                        self.inventory.pop(i)

                    print(f"now on {self.currentHealth}/{self.maxHealth}")
                    sleep(2)

    def __init__(self, Type, health, defence, startingItems):

        self.inventory = startingItems

        self.Type = Type

        self.mainWeapon = self.inventory[0]

        self.meleeDefence, self.rangedDefence, self.magicDefence = defence[0], defence[1], defence[2]

        self.currentHealth = self.maxHealth = dificultyModifier(health, dificulty, False)

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

    def Range(self, slotNum):

        if slotNum == self.distance:

            return red("X")

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

characterSelect = input("select player class\n1 for knight\n2 for barbarian\n3 for archer\n4 for mage\n>>")

if characterSelect == "1":

    knightLoadout = [
        # name, item type, d/heal, crit%, crit multiplier
        ["Biff's sword", "melee", 25, 5, 2],
        ["apple", "heal", 40, ],
        ]

    player = character(" knight", 150, (0.7, 1.1, 1), knightLoadout)

elif characterSelect == "2":

    barbarianLoadout = [
        # name, item type, d/heal, crit%, crit multiplier
        ["Nate's battle axe", "melee",  30, 1, 2],
        ["apple", "heal", 40, ],
        ]

    player = character(" barbarian", 120, (0.9, 1.1, 1), barbarianLoadout)

elif characterSelect == "3":

    archerLoadout = [
        # name, item type, d/heal, crit%, crit multiplier
        ["Bens bow", "ranged",  22, 8, 2.5],
        ["apple", "heal", 40, ],
        ]

    player = character("n archer", 80, (1.3, 0.9, 1), archerLoadout)
    
elif characterSelect == "4":

    mageLoadout = [
        # name, item type, d/heal, crit%, crit multiplier
        ["fire bolt spell", "magic",  20, 12, 2.2],
        ["spotty apple", "heal", 40, ],
        ]

    player = character(" mage", 60, (1, 1, 1), mageLoadout)

elif characterSelect == "rio gets none":

    devLoadout = [
        # name, item type, d/heal, crit%, crit multiplier
        deviousBlade,
        ["spotty apple", "heal", 40, ],
        ]

    player = character(" Dev", 500, (0.5, 0.5, 0.5), devLoadout)

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
sleep(2)

print("YOUR GRANDMOTHER")

sleep(1)

while True:

    clear()

    print('       ___ \n      (___) \n     /`   `\ \n    /  /"\  \ \n    \_/o o\_/ \n     (  _  ) \n      `\ /` \n     /\\\V//\ \n    / /_ _\ \ \n    \ \___/ / \n     \/===\/ \n     ||   || \n     ||   || \n     ||___|| \n     |_____| \n       ||| \n      / Y \ \n      `"`"`')

    choice = input(f"""+-----------------------+
| 0 = player, {red("X")} = enemy | your health: {player.currentHealth}/{player.maxHealth}    their health: {grandmother.currentHealth}/{grandmother.maxHealth}
|      ___________      |
|     /   _____   \     |
|    /   /     \   \    |
|   |   |   0 {grandmother.Range(0)} | {grandmother.Range(1)} | {grandmother.Range(2)} |
|    \   \_____/   /    |
|     \___________/     |
|                       |
+-----------------------+
|  a/away to move away  |
|t/toward to move toward|
|    i for inventory    |
|                       |
|   melee/ranged/magic  |
|       for attack      |
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

    elif choice.lower() == "melee":

        if "melee" in player.mainWeapon[1]:

            if grandmother.distance == 0:

                damage = player.mainWeapon[2]
                crit = False

                if randint(1,100) <= player.mainWeapon[3]:

                    damage *= round(player.mainWeapon[4])
                    crit = True

                print(f"{damage} damage dealt", end="    ")

                if crit:
                    print("Critical hit!")

                grandmother.currentHealth -= damage

                print()
                sleep(2)

            elif grandmother.distance == 1:

                damage = round(player.mainWeapon[2] * (randint(8, 12) / 10))
                crit = False

                if randint(1,100) <= player.mainWeapon[3]:

                    damage *= round(player.mainWeapon[4])
                    crit = True

                print(f"{damage} damage dealt", end="    ")

                if crit:
                    print("Critical hit!")

                grandmother.currentHealth -= damage

                print()
                sleep(2)

            else:

                print("too far away")
                sleep(2)

        else:
            print("melee weapon not selected")
            sleep(2)

    elif choice.lower() == "ranged":

        if "ranged" in player.mainWeapon[1]:

            if grandmother.distance == 1:

                damage = player.mainWeapon[2]
                crit = False

                if randint(1,100) <= player.mainWeapon[3]:

                    damage *= round(player.mainWeapon[4])
                    crit = True

                print(f"{damage} damage dealt", end="    ")

                if crit:
                    print("Critical hit!")

                grandmother.currentHealth -= damage

                print()
                sleep(2)

            elif grandmother.distance == 2:

                damage = round(player.mainWeapon[2] * (randint(8, 12) / 10))
                crit = False

                if randint(1,100) <= player.mainWeapon[3]:

                    damage *= round(player.mainWeapon[4])
                    crit = True

                print(f"{damage} damage dealt", end="    ")

                if crit:
                    print("Critical hit!")

                grandmother.currentHealth -= damage

                print()
                sleep(2)

            else:

                print("too close")
                sleep(2)

        else:

            print("ranged weapon not selected")
            sleep(2)

    elif choice.lower() == "magic" and player.Type == " mage":

        if "magic" in player.mainWeapon[1]:

            if grandmother.distance == 0:

                damage = player.mainWeapon[2]
                crit = False

                if randint(1,100) <= player.mainWeapon[3]:

                    damage *= round(player.mainWeapon[4])
                    crit = True

                print(f"{damage} damage dealt", end="    ")

                if crit:
                    print("Critical hit!")

                grandmother.currentHealth -= damage

                print()
                sleep(2)

            elif grandmother.distance == 1:

                damage = round(player.mainWeapon[2] * (randint(8, 12) / 10))
                crit = False

                if randint(1,100) <= player.mainWeapon[3]:
   
                    damage *= round(player.mainWeapon[4])
                    crit = True

                print(f"{damage} damage dealt", end="    ")

                if crit:
                    print("Critical hit!")

                grandmother.currentHealth -= damage

                print()
                sleep(2)

            elif grandmother.distance == 2:

                damage = round(player.mainWeapon[2] * (randint(8, 12) / 10))
                crit = False

                if randint(1,100) <= player.mainWeapon[3]:
   
                    damage *= round(player.mainWeapon[4])
                    crit = True

                print(f"{damage} damage dealt", end="    ")

                if crit:
                    print("Critical hit!")

                grandmother.currentHealth -= damage

                print()
                sleep(2)

        else:

            print("ranged weapon not selected")
            sleep(2)