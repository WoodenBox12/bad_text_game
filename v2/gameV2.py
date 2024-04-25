from data.appearance.unicode import Inventory, Setup, battle
from data.appearance.console import Console
from random import choice,randint
from files import *
from os import path

# add distance changing item that is defended from attack
# make damage from weapons be different depending on distance precise falloff in weapon stats weapon stats
# remake items.json with new format and more weapon data


# Weapons:
#  Id
#  in game name
#  melee/ranged/magic
#  damage, crit%, crit multiplier
#  damage multipliers for different distances
#  single use boolean
#
#  more different use messages
#
#
#  use effect
#
# Misc:
#
#
#
#
#

Console.Clear()
print(Console.Colour("hello", "1;31;40"))


itemsPath = path.abspath("./v2/data/items.json")

weapons = readjs(itemsPath)[0]
heals = readjs(itemsPath)[1]

class Game:

    Player = None

    class Character:

        Inventory = [[],[],[]]#[[weapons],[heals],[other]]
        MainWeapon = None
        Level = 1
        DamageMultiplier = 1
        Magical = False
        Type = None
        MaxHealth = None
        CurrentHealth = None

        xp = 0
        xpReq = [200,240,390,345,400,450,500,550,600,650,700]

        def AddInventory(self, items: list):
            print(items)
            for i in range(len(items)):
                if ("melee" in items[i][1]) | ("magic" in items[i][1]) | ("ranged" in items[i][1]):
                    self.Inventory[0].append(items[i])
                elif items[i][1] == "heal":
                    self.Inventory[1].append(items[i])
                else:
                    self.Inventory[2].append(items[i])

        def DisplayInventory(self):
            while True:
                Console.Clear()
                
                print(Inventory.WeaponHeader)
                print(Inventory.Divider)
                for i in range(len(self.Inventory[0])):                
                    print(Inventory.DataEntry.format(
                        self.Inventory[0][i][0],
                        self.Inventory[0][i][1],
                        self.Inventory[0][i][2],
                        self.Inventory[0][i][3],
                        self.Inventory[0][i][4]))
                print(Inventory.Tail)
                choice = input(">>").lower().strip()
                command = ""
                for i in range(len(choice)):
                    if choice[i] == " ":
                        break
                    command += choice[i]
                
                match command:
                    case "mw":
                        weapon = choice[2:].translate(str.maketrans("", "", "!@#$' "))
                        print(weapon)

                        continue
                    case "use":
                        weapon = choice[3:].translate(str.maketrans("", "", "!@#$' "))
                        print(weapon)
                        continue
                    case "drop":
                        weapon = choice[4:].translate(str.maketrans("", "", "!@#$' "))
                        print(weapon)
                        continue
                    case _:
                        break

        def __init__(self, type: str, health: int, startingItems: list) -> None:
            print(startingItems)
            self.AddInventory(startingItems)

            self.Type = type

            self.MainWeapon = self.Inventory[0]

            #self.Defence = {"melee":defence[0], "ranged":defence[1], "magic":defence[2]} rethink storage

            self.CurrentHealth = self.MaxHealth = health
           
    class Enemy:

        maxHealth = None
        currentHealth = None

        def __init__(self) -> None:
            pass





    def Battle(self):# simulate battle? mabye use a class   but initialising a class when player and oppenent already exist seems like a waste (mabye just pass into function)
        distance = 0
        print(battle.format("X"*(distance==0), "X"*(distance==1), "X"*(distance==2)))
        self.Player.DisplayInventory()
        pass


    class battle:

        def __init__(self) -> None:
            pass

    
    def SelectDifficulty(self):
        dificulty = input("select dificulty between 1 and 5 or random: ")

        try:
            if (type(int(dificulty)) == int) & (1 <= int(dificulty) <= 5):
                dificulty = int(dificulty)
                return
        except:
            pass
        finally:
            dificulty = randint(1,5)
    
    def SelectClass(self):
        while True:
            print(Setup.Classes)
            match input(">>"):
                case "1":
                    weaponlist = []
                    for i in weapons.keys():
                        weaponlist.append(weapons[i])

                    self.Player = self.Character(" knight", 150, weaponlist)
                    break
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case _:
                    pass
            
    def Setup(self):
        self.SelectDifficulty()
        self.SelectClass()

    def __init__(self) -> None:
        pass
    

def Main():
    game = Game()
    game.Setup()
    game.Battle()

if __name__ == "__main__":
    Main()