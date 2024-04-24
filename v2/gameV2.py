from data.appearance.unicode import inventory, battle, classes
from data.appearance.console import Console
from random import choice,randint
from files import *
from os import path


Console.Clear()
print(Console.Colour("hello", "1;31;40"))


itemsPath = path.abspath("./items.json")

weapons = readjs(itemsPath)[0]
heals = readjs(itemsPath)[1]

class Game:

    class Character:

        Inventory = []#[[weapons],[heals],[other]]
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
            for i in range(len(items)):
                if ("melee" in items[i][1]) | ("magic" in items[i][1]) | ("ranged" in items[i][1]):
                    self.Inventory[0] += items[i]
                elif items[i][1] == "heal":
                    self.Inventory[1] += items[i]
                else:
                    self.Inventory[2] += items[i]

        def DisplayInventory(self):
            Console.Clear()

            print("items in backpack:\n")

            #for i in range(len(self.Inventory[0])):
                #print(self.Inventory[0][i])

        def __init__(self, type: str, health: int, startingItems: list) -> None:
            self.Inventory = startingItems

            self.Type = type

            self.MainWeapon = self.inventory[0]

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
        finally:
            dificulty = randint(1,5)
        input()
        Console.Clear()
    
    def SelectClass(self):
        while True:
            print(classes)
            match input(">>"):
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
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