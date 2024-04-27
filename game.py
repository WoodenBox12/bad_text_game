from random import choice,randint
from os import system, name, path
from time import sleep
from sys import exit
from files import *

#game made by woodenbox12   v1.3

# todo 

# make xp gain higher if higher dificulty

# fix a rule in item pickup
# make enemy move closer sometimes
# custom crit messages
# make overhealed with decay possible   if magical 
# enemy crit chance
# end credits contain elliott and ben

itemsPath = path.abspath("./items.json")

weapons = readjs(itemsPath)[0]
heals = readjs(itemsPath)[1]
    

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
            
            match dificulty:

                case 1 :
                    return baseValue

                case 5 :
                    return int(round(baseValue * 1.2, 0))

                case 4 :
                    return int(round(baseValue * 1.15, 0))

                case 3 :
                    return int(round(baseValue * 1.1, 0))

                case 2 :
                    return int(round(baseValue * 1.05, 0))

        elif increase == False :

            match dificulty:

                case 1 :
                    return baseValue

                case 5 :
                    return int(round(baseValue * 0.6, 0))

                case 4 :
                    return int(round(baseValue * 0.7, 0))

                case 3 :
                    return int(round(baseValue * 0.8, 0))

                case 2 :
                    return int(round(baseValue * 0.9, 0))

class character:

    inventory = None
    mainWeapon = None
    level = 1
    damageMultiplier = 1

    Type = None
    maxHealth = None
    currentHealth = None

    xp = 0
    xpReq = [200,240,390,345,400,450,500,550,600,650,700]

    def levelUp(self):
        
        while True:

            if self.xp >= self.xpReq[self.level - 1]:

                self.xp -= self.xpReq[self.level - 1]
                self.level += 1

                if round(self.maxHealth * 1.08 - self.maxHealth) > 10:

                    self.maxHealth = round(self.maxHealth * 1.08)
                    self.currentHealth += round(self.maxHealth * 1.08 - self.maxHealth)

                else:

                    self.maxHealth += 10
                    self.currentHealth += 10

                self.damageMultiplier += 0.05

                print(f"Leveled up, now on level {self.level}")

                if self.level % 5 == 0:

                    self.heal(500, display=True)
            
            else:
                sleep(1)
                break

    def heal(self, healAmount, pop=False , i=None, display=False):

        if self.currentHealth == self.maxHealth:

            if display:
                print("cannot heal    already on max health")
            return

        elif self.currentHealth + healAmount > self.maxHealth:
            self.currentHealth = self.maxHealth
                        
        else:
            self.currentHealth += healAmount
            
        if pop:

            self.inventory.pop(i)

        if display:
            print(f"now on {self.currentHealth}/{self.maxHealth}")
    
    def Inventory(self):

        clear()
            
        weaponTypes = ("    damage type: ", "    base damage: ", "    crit %: ", "    crit multiplier: ", "")

        print("items in backpack:\n")

        for i in range(len(self.inventory)):

            if self.inventory[i][1] != "heal":

                for j in range(len(self.inventory[i])):

                    if j == 5:
                        break

                    print(self.inventory[i][j], end=weaponTypes[j])

                print()

        print("\nheals:\n")
        #"".translate(None, )
        for i in range(len(self.inventory)):

            if self.inventory[i][1] == "heal":

                print(self.inventory[i][0], end="    ")
                print(f"health gain: {self.inventory[i][2]}")
            
        choice = input(f"\nmain weapon is {self.mainWeapon[0]} \n+----------------------------------------------------+ \n| to change your main weapon type:    mw weapon-name | \n| to use a heal type:                  use item-name | \n+----------------------------------------------------+ \n>>")

        if "mw" in choice.lower():

            choice = choice[3:]
            choice = removeChars(choice, "' ")

            for i in range(len(self.inventory)):

                name = removeChars(self.inventory[i][0].lower(), "' ")

                if choice == name:
                    
                    self.mainWeapon = self.inventory[i]

            input(f"main weapon is now {self.mainWeapon[0]}")

        elif "use" in choice.lower():

            choice = choice[4:]
            choice = removeChars(choice, "' ")

            for i in range(len(self.inventory)):

                name = removeChars(self.inventory[i][0].lower(), "' ")

                if choice == name:
                    
                    if "heal" in self.inventory[i][1]:

                        self.heal(self.inventory[i][2], True, i, True)
                        sleep(2)
                        break

        elif "golly" in choice:

            choice = choice[6:]

            if "weapon" in choice:

                choice = choice[7:]
                try:
                    player.inventory.append(weapons[choice])
                    print("3")

                except:
                    print("item not found")
                    sleep(2)

            elif "heals" in choice:

                choice = choice[6:]

                try:
                    player.inventory.append(heals[choice])
                except:
                    print("item not found")
                    sleep(2)

    def __init__(self, Type, health, defence, startingItems):

        self.inventory = startingItems

        self.Type = Type

        self.mainWeapon = self.inventory[0]

        self.defence = {"melee":defence[0], "ranged":defence[1], "magic":defence[2]}

        self.currentHealth = self.maxHealth = dificultyModifier(health, dificulty, False)

# enemys

class enemys:

    maxHealth = None
    currentHealth = None
    
    distance = None

    def calculateScore(self, attacks):

        score = self.maxHealth
        totalAverage = 0
        averageAttack = 0

        for i in range(len(attacks)):

            total = 0

            for j in range(len(attacks[i])):

                total += 1
                averageAttack += self.attackDamage[attacks[i][j]]

            totalAverage += averageAttack / total

        score += round((totalAverage / 3) * 2)

        return score

    def itemDrop(self, drops, numOfDrops):

        totalWeight = 0
        items = []
        weightPos = []
        currentPos = 0
        drop = []

        for i in range(len(drops)):

            totalWeight += drops[i][1]

            items.append(drops[i][0])
            weightPos.append(drops[i][1])

        for i in range(numOfDrops):

            selector = randint(1, totalWeight)

            for j in range(len(weightPos)):

                currentPos += weightPos[j]

                if selector < currentPos:

                    drop.append(items[j])
                    break

        return drop

    def enemyAttack(self, attackMsg, distance0, distance1, distance2):

        match self.distance:

            case 0:

                closeAttack = choice(distance0)   # returns random from the list
            
                playerDamage = round(self.attackDamage[closeAttack] * (randint(8, 12) / 10) * player.defence[closeAttack])
                print(attackMsg[closeAttack] %(playerDamage))

            case 1:

                midAttack = choice(distance1)   # returns random from the list
            
                playerDamage = round(self.attackDamage[midAttack] * (randint(8, 12) / 10) * player.defence[midAttack])
                print(attackMsg[midAttack] %(playerDamage))

            case 2:

                farAttack = choice(distance2)   # returns random from the list
            
                playerDamage = round(self.attackDamage[farAttack] * (randint(8, 12) / 10) * player.defence[farAttack])
                print(attackMsg[farAttack] %(playerDamage))

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

        self.attackDamage = {"melee":damage[0],"ranged":damage[1],"magic":damage[2]}

        self.defence = {"melee":defence[0], "ranged":defence[1], "magic":defence[2]}

# dificulty select

dificulty = input("select dificulty between 1 and 5 or random: ")

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

match characterSelect.lower():

    case "1":

        knightLoadout = [
            # name, item type, d/heal, crit%, crit multiplier
            weapons["Biff's Sword"],
            heals["Apple"],
            ]

        player = character(" knight", 150, [0.7, 1.1, 1], knightLoadout)

    case "2":

        barbarianLoadout = [
            # name, item type, d/heal, crit%, crit multiplier
            weapons["Nate's Battle Axe"],
            heals["Apple"],
            ]

        player = character(" barbarian", 120, [0.9, 0.8, 1], barbarianLoadout)

    case "3":

        archerLoadout = [
            # name, item type, d/heal, crit%, crit multiplier
            weapons["Ben's Bow"],
            heals["Apple"],
            ]

        player = character("n archer", 80, [1.2, 0.7, 1], archerLoadout)
    
    case "4":

        mageLoadout = [
            # name, item type, d/heal, crit%, crit multiplier
            weapons["Fire Bolt Spell"],
            heals["Spotty Apple"],
            ]

        player = character(" mage", 60, [1, 1, 0.8], mageLoadout)

    case "golly golly gosh":

        devLoadout = [
            # name, item type, d/heal, crit%, crit multiplier
            weapons["Dev-10s Blade"],
            heals["Dev Apple"],
            ]

        player = character(" Dev", 500, [0.5, 0.5, 0.5], devLoadout)

sleep(2)
clear()

print (f'''                     _ \n         .=========., | \n        /_,-.___.-._\ | \n        | [_]/o\[_] |7' \n  i=I=I=|____|_|____|I=I=I=i \n |/,*`*,*`**'/ \      ,-'`.\| \n|/          /...\   (__.-._)\| \n||||||||||||TTTTT||||||||||||| \n""""""""""""HHHHH""""""""""""" \nyour journey as a{player.Type} begins \nin your grandmothers house''')
sleep(4)
clear()

print("level 1\n\nas you walk out the house you come across an enemy\n")

sleep(2)

print("YOUR GRANDMOTHER")

sleep(1.5)
clear()
print('       ___ \n      (___) \n     /`   `\ \n    /  /"\  \ \n    \_/o o\_/ \n     (  _  ) \n      `\ /` \n     /\\\V//\ \n    / /_ _\ \ \n    \ \___/ / \n     \/===\/ \n     ||   || \n     ||   || \n     ||___|| \n     |_____| \n       ||| \n      / Y \ \n      `"`"`')
sleep(2)

enemyNum = 0
def fight(enemyName, enemyAttackMsg, closeAttacks, midAttacks, farAttacks, possibleLoot, lootAmount):

    global enemyNum 
    enemyNum += 1

    while enemyNum <= 10:

        clear()

        print(f"Level {enemyNum}\n{enemyName}")

        choice = input(f"+-----------------------+ \n| 0 = player, {red('X')} = enemy | your health: {player.currentHealth}/{player.maxHealth}    their health: {opponent.currentHealth}/{opponent.maxHealth}\n|      ___________      | {player.xpReq[player.level - 1]-player.xp} xp away from level {player.level + 1}\n|     /   _____   \     | \n|    /   /     \   \    | \n|   |   |   0 {opponent.Range(0)} | {opponent.Range(1)} | {opponent.Range(2)} | \n|    \   \_____/   /    | \n|     \___________/     | \n|                       | \n+-----------------------+ \n|  a/away to move away  | \n|t/toward to move toward| \n|    i for inventory    | \n|                       | \n|   melee/ranged/magic  | \n|       for attack      | \n+-----------------------+ \n>>")
        
        match choice.lower():

            case "t" | "toward":
        
                if opponent.distance == 0:

                    print("cannot move any closer")
                    sleep(2)
                    continue
                opponent.distance -= 1
                
            case "a" | "away":   
        
                if opponent.distance == 2:

                    print("you attempt to run away but a mysterious force is preventing you")
                    sleep(2)
                    continue
                opponent.distance += 1

            case "i":
                player.Inventory()
                continue
   
            case "me" | "melee":

                if not ("melee" in player.mainWeapon[1]):

                    print("melee weapon not selected")
                    sleep(1)
                    continue

                if opponent.distance == 2:

                    print("too far away")
                    sleep(1)
                    continue

                damage = round(player.mainWeapon[2] * player.damageMultiplier * opponent.defence["melee"])
                player.xp += 5
                crit = False

                if opponent.distance == 1:

                    damage = round(damage * (randint(8, 12) / 10))

                if randint(1,100) <= player.mainWeapon[3]:

                    damage *= round(player.mainWeapon[4])
                    player.xp += 40
                    crit = True

                print(player.mainWeapon[5][0] %(enemyName, damage), end="    ")

                if crit:
                    print("Critical hit!",end="\n\n")

                else:
                    print("",end="\n\n")

                opponent.currentHealth -= damage
                sleep(2)

            case "ra" | "ranged":

                if not ("ranged" in player.mainWeapon[1]):

                    print("ranged weapon not selected")
                    sleep(2)
                    continue

                if opponent.distance == 0:

                    print("too close")
                    sleep(1)
                    continue

                damage = round(player.mainWeapon[2] * player.damageMultiplier * opponent.defence["ranged"])
                player.xp += 5
                crit = False

                if opponent.distance == 2:

                    damage = round(damage * (randint(8, 12) / 10))

                if randint(1,100) <= player.mainWeapon[3]:

                    damage *= round(player.mainWeapon[4])
                    player.xp += 40
                    crit = True

                print(player.mainWeapon[5][1] %(enemyName, damage), end="    ")

                if crit:
                    print("Critical hit!",end="\n\n")

                else:
                    print("",end="\n\n")

                opponent.currentHealth -= damage
                sleep(1)

            case "ma" | "magic":

                if not (player.Type == " mage"):
                    print("you have no magical powers")
                    sleep(1)
                    continue

                if not ("magic" in player.mainWeapon[1]):
                    print("magic weapon not selected")
                    sleep(1)
                    continue

                damage = round(player.mainWeapon[2] * player.damageMultiplier * opponent.defence["melee"])
                player.xp += 5
                crit = False

                if opponent.distance == 0 or opponent.distance == 2:

                    damage = round(damage * (randint(8, 12) / 10))

                if randint(1,100) <= player.mainWeapon[3]:

                    damage *= round(player.mainWeapon[4])
                    player.xp += 40
                    crit = True

                print(player.mainWeapon[5][2] %(enemyName, damage), end="    ")

                if crit:
                    print("Critical hit!",end="\n\n")

                else:
                    print("",end="\n\n")

                opponent.currentHealth -= damage
                sleep(2)

            case _:
                continue

        # logic to see if enemy dies

        if opponent.currentHealth <= 0:

            player.heal(-opponent.currentHealth)

            newItems = opponent.itemDrop(possibleLoot, lootAmount)

            for i in range(len(newItems)):

                player.inventory.append(newItems[i])
                print(f"you found {newItems[i][0]} on the floor next to {enemyName}'s carcus so you pick it up")
                sleep(2)

            opponent.calculateScore([closeAttacks, midAttacks, farAttacks])

            print(f"you defeated {enemyName} and gained {-opponent.currentHealth} health")

            player.xp += opponent.calculateScore([closeAttacks, midAttacks, farAttacks])
            
            player.levelUp()


            sleep(2)
            return        

        # enemy turn

        else:

            opponent.enemyAttack( enemyAttackMsg, closeAttacks, midAttacks, farAttacks)

        player.levelUp()

        if player.currentHealth <= 0:

            print(f"\n\nsoo close buddy enemy {enemyNum} was only on {opponent.currentHealth} health")
            exit()


opponent = enemys(100, (20, 15, 0), (1, 1, 1.5), 0)
fight("your grandmother", {"melee":"your grandmother batters you with a rolling pin dealing %s damage", "ranged":"your grandmother throws cookies at you dealing %s damage", "magic":"your grandmother attacks you with her elderly wisdom dealing %s damage"},
    ["melee"], ["melee", "ranged"], ["ranged"],
    [[weapons["Liam's Fry"], 2], [weapons["Elliott's Calculator"], 1], [weapons["Rolling Pin"], 10], [heals["Stale Cookie"], 10]], 1)

opponent = enemys(115, (35, 10, 100), (1, 1, 1), 1)
fight("a vicious dog", {"melee":"the vicious dog swipes at you with its paw dealing %s damage", "ranged":"the vicious dog violently spits at you dealing %s damage", "magic":"the dog opened its third eye and blasted you with a mystical beam of pure energy dealing %s damage"},
     ["melee"], ["melee","ranged"], ["magic"],
     [[weapons["Dog Spit"], 4], [heals["Apple"], 10]], 2)

opponent = enemys(125, (10, 15, 30), (1, 1, 0.8), 2)
fight("a magician", {"melee":"the magician pulls a hammer out of his hat and hits you with it dealing %s damage", "ranged":"the magician violently throws a rabbit at you at you dealing %s damage", "magic":"the magician flicked his wand dealing %s damage"},
     ["melee"], ["ranged", "magic"], ["magic"],
     [[weapons["Wand"], 3], [heals["Apple"], 10]], 2)

opponent = enemys(130, (10, 35, 0), (0.9, 1, 1.2), 2)
fight("jack mackay", {"melee":"jack stabbed you with his bayonet dealing %s damage", "ranged":"jack shoots you dealing %s damage", "magic":"jack confuses you with his idiocy dealing %s damage"},
     ["melee"], ["melee","ranged"], ["ranged"],
     [[weapons["Jack's Rifle"], 3], [heals["Apple"], 10]], 2)

opponent = enemys(145, (14, 40, 0), (1.1, 0.7, 1), 2)
fight("a gifted archer", {"melee":"the archer stabbed your neck with his arrow dealing %s damage", "ranged":"the archer shoots you with his bow dealing %s damage", "magic":"the archer deals %s damage"},
     ["melee"], ["melee","ranged"], ["ranged"],
     [[weapons["Antique Bow"], 3], [heals["Apple"], 10]], 2)

opponent = enemys(150, (20, 45, 0), (1, 1, 1.4), 2)
fight("rio", {"melee":"rio caved in your skull with his high heel dealing %s damage", "ranged":"rio threw his high heel at you dealing %s damage", "magic":"rio confuses you with his dislesia dealing %s damage"},
     ["melee"], ["melee","ranged"], ["ranged"],
     [[weapons["Rio's Heel"], 5], [heals["Apple"], 10]], 2)

opponent = enemys(170, (5, 12, 45), (1.2, 1, 0.7), 1)
fight("rishabh", {"melee":"rishabh caved in your skull with his pencil dealing %s damage", "ranged":"rishabh threw his orb at you dealing %s damage", "magic":"rishabh attacks you with the orbs mystical powers dealing %s damage"},
     ["melee","magic"], ["melee","ranged","magic"], ["magic"],
     [[weapons["The Orb"], 1], [heals["Apple"], 9]], 2)

print("thanks for playing")
print("made with help from Elliott and Ben")