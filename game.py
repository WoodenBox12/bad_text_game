from random import randint
from os import system, name
from time import sleep
from sys import exit

#game made by woodenbox12

# todo 

# make args for fighting (easy - medium)
# make enemys drop items usinng function args (easy - medium) sometimes
# make enemy move closer sometimes
# make enemy attack function have arguments to show what attacks at different ranges
# custom attack messages

# early weapon

riosHeel = ["Rio's High Heel", "melee/ranged", 50, 5, 2, ["you attempt to cave in %s skull dealing %s damage", "you throw Rio's high heel into %s forehead dealing %s damage"]]

cavemanClub = ["caveman club", "melee", 40, 10, 3]

mattsshortbarreler = ["Matt's Short Barreler", "ranged", 44, 4, 4]

jacksrifle = ["Jack's Rifle", "melee/ranged", 80, 50, -1]

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

    def heal(self, healAmount, pop=False , i=None):

        if self.currentHealth == self.maxHealth:

            print("cannot heal    already on max health")
            sleep(2)

        elif self.currentHealth + healAmount > self.maxHealth:

            self.currentHealth = self.maxHealth

            if pop:

                self.inventory.pop(i)
                        
        else:

            self.currentHealth += healAmount
            
            if pop:

                self.inventory.pop(i)

            print(f"now on {self.currentHealth}/{self.maxHealth}")
            sleep(2)
    
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
            
        choice = input(f"\nmain weapon is {self.mainWeapon[0]} \n+----------------------------------------------------+ \n| to change your main weapon type:    mw weapon-name | \n| to use a heal type:                  use item-name | \n+----------------------------------------------------+ \n>>").lower()

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
                    
                    self.heal(self.inventory[i][2], True, i)
                    break

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

    def enemyAttack(self,enemyName, attackMsg):

        if self.distance == 0:
        
            playerDamage = round(self.meleeDamage * (randint(8, 12) / 10) * player.meleeDefence)
            print(attackMsg[0] %playerDamage)

        elif self.distance == 1:

            z = randint(0,1)

            if z == 0:

                playerDamage = round(self.meleeDamage * (randint(8, 12) / 10) * player.meleeDefence)
                print(attackMsg[0] %playerDamage)

            else:

                playerDamage = round(self.rangedDamage * (randint(8, 12) / 10) * player.rangedDefence)
                print(attackMsg[1] %playerDamage)

        elif self.distance == 2:
        
            playerDamage = round(self.rangedDamage * (randint(8, 12) / 10) * player.rangedDefence)
            print(attackMsg[1] %playerDamage)
        
        player.currentHealth -= playerDamage
        sleep(2)

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
        ["Biff's sword", "melee", 22, 5, 2, ["you swing at %s dealing %s damage"]],
        ["apple", "heal", 40, ],
        ]

    player = character(" knight", 150, (0.7, 1.1, 1), knightLoadout)

elif characterSelect == "2":

    barbarianLoadout = [
        # name, item type, d/heal, crit%, crit multiplier
        ["Nate's battle axe", "melee/ranged",  38, 5, 2],
        ["apple", "heal", 40, ],
        ]

    player = character(" barbarian", 120, (0.9, 0.8, 1), barbarianLoadout)

elif characterSelect == "3":

    archerLoadout = [
        # name, item type, d/heal, crit%, crit multiplier
        ["Bens bow", "ranged",  30, 10, 2.5],
        ["apple", "heal", 40, ],
        ]

    player = character("n archer", 80, (1.2, 0.7, 1), archerLoadout)
    
elif characterSelect == "4":

    mageLoadout = [
        # name, item type, d/heal, crit%, crit multiplier
        ["fire bolt spell", "magic",  35, 12, 2.2],
        ["spotty apple", "heal", 40, ],
        ]

    player = character(" mage", 60, (1, 1, 0.8), mageLoadout)

elif characterSelect == "golly golly gosh":

    devLoadout = [
        # name, item type, d/heal, crit%, crit multiplier
        deviousBlade,
        ["spotty apple", "heal", 40, ],
        ]

    player = character(" Dev", 500, (0.5, 0.5, 0.5), devLoadout)

sleep(2)
clear()

print (f'''                     _ \n         .=========., | \n        /_,-.___.-._\ | \n        | [_]/o\[_] |7' \n  i=I=I=|____|_|____|I=I=I=i \n |/,*`*,*`**'/ \      ,-'`.\| \n|/          /...\   (__.-._)\| \n||||||||||||TTTTT||||||||||||| \n""""""""""""HHHHH""""""""""""" \nyour journey as a{player.Type} begins \nin your grandmothers house''')

sleep(4)
clear()

print("level 1\n\nas you walk out the house you come across an enemy\n")

opponent = enemys(100, (20, 15, 0), (1, 1, 1.5), 0)
sleep(2)

print("YOUR GRANDMOTHER")

sleep(1)
clear()
print('       ___ \n      (___) \n     /`   `\ \n    /  /"\  \ \n    \_/o o\_/ \n     (  _  ) \n      `\ /` \n     /\\\V//\ \n    / /_ _\ \ \n    \ \___/ / \n     \/===\/ \n     ||   || \n     ||   || \n     ||___|| \n     |_____| \n       ||| \n      / Y \ \n      `"`"`')
sleep(2)

def fight(enemyName, enemyAttackMsg):

    while True:

        clear()

        print("log")

        choice = input(f"+-----------------------+ \n| 0 = player, {red('X')} = enemy | your health: {player.currentHealth}/{player.maxHealth}    their health: {opponent.currentHealth}/{opponent.maxHealth}\n|      ___________      | \n|     /   _____   \     | \n|    /   /     \   \    | \n|   |   |   0 {opponent.Range(0)} | {opponent.Range(1)} | {opponent.Range(2)} | \n|    \   \_____/   /    | \n|     \___________/     | \n|                       | \n+-----------------------+ \n|  a/away to move away  | \n|t/toward to move toward| \n|    i for inventory    | \n|                       | \n|   melee/ranged/magic  | \n|       for attack      | \n+-----------------------+ \n>>")
        
        if choice.lower() == "t" or choice.lower() == "toward":
        
            if opponent.distance == 0:

                print("cannot move any closer")
                sleep(2)

            else:

                opponent.distance -= 1
                
        elif choice.lower() == "a" or choice.lower() == "away":
        
            if opponent.distance == 2:

                print("you attempt to run away but a mysterious force is preventing you")
                sleep(2)

            else:

                opponent.distance += 1

        elif choice.lower() == "i":
    
            player.Inventory()
            continue
   
        elif choice.lower() == "melee":

            if "melee" in player.mainWeapon[1]:

                if opponent.distance == 2:

                    print("too far away")
                    sleep(2)

                else:

                    damage = player.mainWeapon[2]
                    crit = False

                    if opponent.distance == 1:

                        damage = round(damage * (randint(8, 12) / 10))

                    if randint(1,100) <= player.mainWeapon[3]:

                        damage *= round(player.mainWeapon[4])
                        crit = True

                    print(player.mainWeapon[5][0] %(enemyName, damage), end="    ")

                    if crit:
                        print("Critical hit!")

                    else:
                        print("\n")

                    opponent.currentHealth -= damage

                    print()
                    sleep(2)

            else:
                print("melee weapon not selected")
                sleep(1)
                continue

        elif choice.lower() == "ranged":

            if "ranged" in player.mainWeapon[1]:

                if opponent.distance == 0:

                    print("too close")
                    sleep(1)

                else:

                    damage = player.mainWeapon[2]
                    crit = False

                    if opponent.distance == 2:

                        damage = round(damage * (randint(8, 12) / 10))

                    if randint(1,100) <= player.mainWeapon[3]:

                        damage *= round(player.mainWeapon[4])
                        crit = True

                    print(f"{damage} damage dealt", end="    ")

                    if crit:
                        print("Critical hit!")

                    opponent.currentHealth -= damage

                    print()
                    sleep(1)

            else:

                print("ranged weapon not selected")
                sleep(2)
                continue

        elif choice.lower() == "magic":

            if player.Type == " mage":

                if "magic" in player.mainWeapon[1]:

                        damage = player.mainWeapon[2]
                        crit = False

                        if opponent.distance == 0 or opponent.distance == 2:

                            damage = round(damage * (randint(8, 12) / 10))

                        if randint(1,100) <= player.mainWeapon[3]:

                            damage *= round(player.mainWeapon[4])
                            crit = True

                        print(f"{damage} damage dealt", end="    ")

                        if crit:
                            print("Critical hit!")

                        opponent.currentHealth -= damage

                        print()
                        sleep(1)

                else:

                    print("magic weapon not selected")
                    sleep(1)
                    continue

            else:

                print("you have no magical powers")
                sleep(1)
                continue

        else:
            continue

        # logic to see if enemy dies

        if opponent.currentHealth <= 0:

            player.heal(-opponent.currentHealth)

            print(f"you defeated {'grandmother'} and gained {-opponent.currentHealth} health")
            sleep(2)
            return

        # enemy turn

        else:

            opponent.enemyAttack(enemyName, enemyAttackMsg)

        if player.currentHealth <= 0:

            print(f"\n\nsoo close buddy enemy {1} was only on {opponent.currentHealth} health")
            exit()

fight("your grandmother", ("your grandmother batters you with a rolling pin dealing %s damage", "your grandmother throws cookies at you dealing %s damage", "your grandmother attacks you with her elderly wisdom dealing %s damage"))

clear()
print("level 2\na vicious dog")
sleep(2)





opponent = enemys(115, (35, 10, 100), (1, 1, 1), 1)
fight("a vicious dog", ("the vicious dog swipes at you with its paw dealing %s damage", "the vicious dog violently spits at you dealing %s damage", "the dog opened its third eye and blasted you with a mystical beam of pure energy dealing %s damage"))