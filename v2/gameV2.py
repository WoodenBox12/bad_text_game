from data.appearance.unicode import Inventory, Setup, battle
from data.appearance.console import Console
from data.items import Items

from random import choice,randint
from files import *
from os import path

# add distance changing item that is defended from attack
# make damage from weapons be different depending on distance precise falloff in weapon stats weapon stats

# make automated easily expandable command system 
# make inventory sortable by different fields

#
#
# use effect for weapons
#
# Misc:
#
# mw currently stores a copy of the item in variable
# mabye change to name but then would have to search all weapons every time which seems inneficent (but so does storing a redundant copy)
# dont know what to do?
#

class Character:

    Inventory: list[list] = [[],[],[]]#[[weapons],[heals],[other]]
    MainWeapon: str
    Level: int
    DamageMultiplier: int
    Magical: bool
    Type: bytes
    MaxHealth: int
    CurrentHealth: int

    xp: int= 0
    xpReq: list[int]= [200,240,390,345,400,450,500,550,600,650,700]

    def AddInventory(self, items: list) -> None:
        for i in range(len(items)):
            if items[i].Type > 0b00011111:# weapon
                self.Inventory[0].append(items[i])
            elif items[i].Type & 0b00010000 == 0b00010000:# heal
                self.Inventory[1].append(items[i])
            else:
                self.Inventory[2].append(items[i])# other

    def BitmaskToString(self, Bitmask: bytes) -> str:
        outStr =""
        names = ["melee", "ranged", "magic", "heal", "other", "", "", ""]
        for i in range(0,8):
            if Bitmask & (128>>i) == (128>>i):
                outStr += names[i] + "/"
        return outStr.strip("/")

    def SwapMainWeapon(self, weapon) -> None:
        for i in range(len(self.Inventory[0])):
            if self.Inventory[0][i].Name.lower().translate(str.maketrans("", "", "!@#$' ")) == weapon:
                self.MainWeapon = self.Inventory[0][i]
                input(f"main weapon is now {self.MainWeapon.Name}\n")
                return
        input(f"unable to change main weapon\n")

    def UseItem(self, item) -> None:
        for i in range(len(self.Inventory[1])):# for heals
            if self.Inventory[1][i].Name.lower().translate(str.maketrans("", "", "!@#$' ")) == item:
                
                self.Heal(self.Inventory[1][i].Amount)

                if self.Inventory[1][i].SingleUse:
                    self.Inventory[1].pop(i)
                
                input(f"now on {self.CurrentHealth}/{self.MaxHealth}\n")
                return
                # decrement UsesLeft if use count is added
            input("no code here my guy\n")

    def DropItem(self, item) -> None:
        for i in range(len(self.Inventory[1])):# for heals
            if self.Inventory[1][i].Name.lower().translate(str.maketrans("", "", "!@#$' ")) == item:# mabye add more code to drop items
                self.Inventory[1].pop(i)
                input(f"item dropped\n")
                return
            
    def Heal(self, amount: int) -> None:
        self.CurrentHealth += amount

        if self.CurrentHealth >= self.MaxHealth:
            self.CurrentHealth = self.MaxHealth

    def DisplayInventory(self):
        while True:
            Console.Clear()
            print(Inventory.WeaponHeader)
            print(Inventory.Divider)
            for i in range(len(self.Inventory[0])):                
                print(Inventory.WeaponEntry.format(
                    self.Inventory[0][i].Name,
                    self.BitmaskToString(self.Inventory[0][i].Type),# make function to convert to string
                    self.Inventory[0][i].Damage,
                    "{}%".format(self.Inventory[0][i].CritChance),
                    self.Inventory[0][i].CritDamage
                ))
            print(Inventory.Divider)
            print(Inventory.HealHeader)
            print(Inventory.Divider)
            for i in range(len(self.Inventory[1])):
                print(Inventory.HealEntry.format(
                    self.Inventory[1][i].Name,
                    self.BitmaskToString(self.Inventory[1][i].Type),
                    self.Inventory[1][i].Amount
                ))
            print(Inventory.Tail.format(mw=self.MainWeapon.Name))
                

            command, item = Console.GetCommand()

            match command:
                case "mw":
                    self.SwapMainWeapon(item)
                case "use":
                    self.UseItem(item)
                case "drop":
                    self.DropItem(item)
                case _:
                    break

    def __init__(self, type: str, health: int, startingItems: list, magical: bool) -> None:
        self.AddInventory(startingItems)

        self.DamageMultiplier = 1
        self.Level = 1

        self.Magical = magical

        self.Type = type

        self.MainWeapon = self.Inventory[0][0]

        self.CurrentHealth = self.MaxHealth = health

class Enemy:

    maxHealth = None
    currentHealth = None

    def __init__(self) -> None:
        pass

class Game:

    Player: Character
    Opponent: Enemy


    def Battle(self):# simulate battle? mabye use a class   but initialising a class when player and oppenent already exist seems like a waste (mabye just pass into function)
        distance = 0
        
        
        while True:
            Console.Clear()
            print(battle.format("X"*(distance==0), "X"*(distance==1), "X"*(distance==2)))
            command, rest = Console.GetCommand()

            match command:
                case "t" | "toward":
                    if distance == 0:
                        input("unable to closer\n")
                        continue
                    distance -= 1
                    input("moved closer\n")

                case "a" | "away":
                    if distance == 2:
                        input("you attempt to run away but a mysterious force is preventing you\n")
                        continue
                    distance += 1
                    input("moved further away\n")

                case "i" | "inventory":
                    self.Player.DisplayInventory()
                
                case "me" | "melee":
                    pass
                
                case "ra" | "ranged":
                    pass
                
                case "ma" | "magic":
                    pass
                
                case "seppuku":
                    
                    pass

                case _:
                    pass


    class battle:

        def __init__(self) -> None:
            pass

    
    def SelectDifficulty(self):
        Console.Clear()
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
            Console.Clear()
            print(Setup.Classes)
            match input(">>"):
                case "1":
                    Loadout =  [Items.AntiqueBow, Items.Apple]

                    self.Player = Character(" knight", 150, Loadout, False)
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