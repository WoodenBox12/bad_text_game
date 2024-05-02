from data.appearance.unicode import Inventory, Setup, battle
from data.appearance.console import Console
from data.items import Items

from math import isqrt, floor
from random import choice, choices, randint
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
    DamageMultiplier: int
    Magical: bool
    Type: bytes
    MaxHealth: int
    CurrentHealth: int

    Xp: int
    Level: int

    def LevelUp(self) -> None:# https://www.desmos.com/calculator/ak3w2tjndn for equation    not finished yet
        NewLevel = floor((isqrt(self.Xp) / 50) + (self.Xp / 200)) + 1
        if self.Level < NewLevel:
            self.Level = NewLevel
            input(f"Leveled up, now on level {self.Level}\n")

    def AddInventory(self, items: list) -> None:
        for i in range(len(items)):
            if items[i].Type & 0b11100000 >= 0b00100000:# weapon
                self.Inventory[0].append(items[i])
            elif items[i].Type & 0b00010000 == 0b00010000:# heal
                self.Inventory[1].append(items[i])
            else:
                self.Inventory[2].append(items[i])# other

    def BitmaskToString(self, bitmask: bytes) -> str:
        outStr =""
        names = ["melee", "ranged", "magic", "heal", "other", "", "", ""]
        for i in range(0,8):
            if bitmask & (128>>i) == (128>>i):
                outStr += names[i] + "/"
        return outStr.strip("/")

    # mabye add search function with a function partameter

    def SwapMainWeapon(self, weapon: str) -> None:
        for i in range(len(self.Inventory[0])):
            if self.Inventory[0][i].Name.lower().translate(str.maketrans("", "", "!@#$' ")) == weapon:
                self.MainWeapon = self.Inventory[0][i]
                input(f"main weapon is now {self.MainWeapon.Name}\n")
                return
        input(f"unable to change main weapon\n")

    def UseItem(self, item: str) -> None:
        for i in range(len(self.Inventory[1])):# for heals
            if self.Inventory[1][i].Name.lower().translate(str.maketrans("", "", "!@#$' ")) == item:
                
                self.Heal(self.Inventory[1][i].Amount)

                if self.Inventory[1][i].SingleUse:
                    self.Inventory[1].pop(i)
                
                input(f"now on {self.CurrentHealth}/{self.MaxHealth}\n")
                return
                # decrement UsesLeft if use count is added
        input("no code here my guy\n")

    def DropItem(self, item: str) -> None:
        for i in range(len(self.Inventory[1])):# for heals
            if self.Inventory[1][i].Name.lower().translate(str.maketrans("", "", "!@#$' ")) == item:# mabye add more code to drop items
                self.Inventory[1].pop(i)
                input(f"item dropped\n")
                return
        input("no code here my guy\n")           

    def Heal(self, amount: int) -> None:
        self.CurrentHealth += amount

        if self.CurrentHealth >= self.MaxHealth:
            self.CurrentHealth = self.MaxHealth

    def DisplayInventory(self):
        while True:
            Console.Clear()# mabye add pages to change inventory view

            print(Inventory.Title.format("Heals"))
            print(Inventory.HealHeader)
            print(Inventory.Divider)
            for i in range(len(self.Inventory[1])):
                print(Inventory.HealEntry.format(
                    self.Inventory[1][i].Name,
                    self.BitmaskToString(self.Inventory[1][i].Type),
                    self.Inventory[1][i].Amount
                ))
            print(Inventory.EndDivider)
            
            print(Inventory.Title.format("Weapons"))
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

            
            print(Inventory.Tail.format(mw=self.MainWeapon.Name))
                
            command, item = Console.GetCommand(input(">>"))
            item = item.translate(str.maketrans("", "", "!@#$' "))

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
        self.Xp = 0

        self.Magical = magical

        self.Type = type

        self.MainWeapon = self.Inventory[0][0]

        self.CurrentHealth = self.MaxHealth = health

class Enemy:
     
    MaxHealth: int     
    CurrentHealth: int     
     
    Distance: int     
    Attacks: list[list[str]]     
    Damages: list[int]     

    def CalculateScore(self):# some score making function for player xp gain
        score = self.MaxHealth

        return score

    def ItemDrop(self, items: list, weights: list[int], dropCount: int) -> list[str]:
        return choices(items, weights, k=dropCount)

    def Attack(self,):# return int of damage dealt     must attack within certain constraints
        match self.Distance:#  how to include player resistances?
            case 0:
                attack = choice(self.Attacks[0])
            case 1:
                attack = choice(self.Attacks[1])
            case 2:
                attack = choice(self.Attacks[2])

    def __init__(self, distance: int, health: int, attacks: list[list[str]], damages: list[int]) -> None:
        self.Distance = distance

        self.CurrentHealth = self.MaxHealth = health

        self.Attacks = attacks
        self.Damages = damages
        
class FieldEditor:
    def ChangeField(object: object, field: str, strType: str, value: str):
        match strType:
            case "str":
                castValue = value
            case "bool":
                castValue = (value == "True")
            case "int":
                castValue = int(value)
            case "float":
                castValue = float(value)

        if hasattr(object, field):
            setattr(object, field, castValue)
            input("{}.{} is now set to {} (type:{})\n".format(type(object).__name__, field, castValue, type(castValue).__name__))
            return
        input("{}.{} is not a recognised field\n".format(type(object).__name__, field))

    def __init__(self) -> None:
        pass

class Game:

    Player: Character
    Opponent: Enemy
    Cheats: bool= False

    def Battle(self):# simulate battle? mabye use a class   but initialising a class when player and oppenent already exist seems like a waste (mabye just pass into function)
        self.Opponent = Enemy(0, 100, [["melee"],["melee", "ranged"],["ranged"]], [30, 25, 20])

        while True:
            Console.Clear()
            print(battle.format(self.Player.CurrentHealth, self.Player.MaxHealth, self.Opponent.CurrentHealth, self.Opponent.MaxHealth,
                "X"*(self.Opponent.Distance==0), "X"*(self.Opponent.Distance==1), "X"*(self.Opponent.Distance==2)))
            command, rest = Console.GetCommand(input(">>"))

            match command:
                case "t" | "toward":
                    if self.Opponent.Distance == 0:
                        input("unable to move closer\n")
                        continue
                    self.Opponent.Distance -= 1
                    input("moved closer\n")

                case "a" | "away":
                    if self.Opponent.Distance == 2:
                        input("you attempt to run away but a mysterious force is preventing you\n")
                        continue
                    self.Opponent.Distance += 1
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

                case "edit":
                    if not self.Cheats:
                        input("cheats not enabled\n")
                        continue
                    temp = rest.split()
                    obj, field, strType, value = temp[0], temp[1], temp[2], temp[3]

                    if (obj.lower() == "player") | (obj.lower() == "character"):
                        FieldEditor.ChangeField(self.Player,field, strType, value)
                        continue
                    FieldEditor.ChangeField(self.Opponent,field, strType, value)

                case _:
                    pass

    def SelectDifficulty(self) -> None:
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

    def SelectClass(self) -> None:
        while True:
            Console.Clear()
            print(Setup.Classes)
            match input(">>"):
                case "1":
                    knightLoadout = [Items.Sword, Items.Apple]

                    self.Player = Character(" knight", 150, knightLoadout, False)
                    break
                case "2":
                    barbarianLoadout = [Items.BattleAxe, Items.Apple]

                    self.Player = Character(" barbarian", 120, barbarianLoadout, False)
                    break
                case "3":
                    archerLoadout = [Items.Bow, Items.Apple]

                    self.Player = Character("n archer", 80, archerLoadout, False)
                    break
                case "4":
                    mageLoadout = [Items.FireBolt, Items.Apple]

                    self.Player = Character(" mage", 80, mageLoadout, True)
                    break
                case "dev":
                    devLoadout = [Items.Dev10usBlade, Items.DevApple]

                    self.Player = Character(" dev", 500, devLoadout, True)
                    break
                case _:
                    pass

    def Setup(self) -> None:
        self.SelectDifficulty()
        self.SelectClass()

    def __init__(self, cheats) -> None:
        self.Cheats = cheats

def Main():
    game = Game(True)
    game.Setup()
    game.Battle()

if __name__ == "__main__":
    Main()