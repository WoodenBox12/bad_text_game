


class Weapon:
    Id: str
    Name: str
    Type: bytes # mabye use bitmasks for different types
    Damage: int
    CritChance: int
    CritDamage: float

    Distances: list[int]   # [1,0.5,0.25] multipliers for different distances     mabye have one of these for each attack type
    Types: list[int]     #   [1.3, 1, 0.6] multipliers for different attack types
    SingleUse: bool

    MeMsg: list[str]
    RaMsg: list[str]
    MaMsg: list[str]

    def __init__(self, Name, Type, Damage, CritChance, CritDamage, SingleUse, MeMsg, RaMsg, MaMsg) -> None:
        self.Name = Name
        self.Type = Type
        self.Damage = Damage
        self.CritChance = CritChance
        self.CritDamage = CritDamage

        self.SingleUse = SingleUse

        self.MeMsg = MeMsg
        self.RaMsg = RaMsg
        self.MaMsg = MaMsg
        

"""class AntiqueBow(Weapon):
    Name = "Antique Bow"
    Type = 0b01000000
    Damage = 45
    CritChance = 10
    CritDamage = 2.5

    SingleUse = False

    RaMsg = ["you fire an arrow at {enemyName} dealing {damage} damage", ]"""

AntiqueBow = Weapon(
    "Antique Bow", 0b01000000, 45, 10, 2.5, False, 
    None, 
    ["you fire an arrow at {enemyName} dealing {damage} damage", ], 
    None)

Wand = Weapon(
    "Wand", 0b00100000, 55, 10, 3, False, 
    None, 
    None, 
    ["you wave your wand at {enemyName} dealing {damage} damage", ])

DogSpit = Weapon(
    "Dog Spit", 0b01000000, 40, 10, 2, False, 
    None, 
    ["you spit at {enemyName} dealing {damage} damage", ], 
    None)

RollingPin = Weapon(
    "Rolling Pin", 0b10000000, 30, 8, 2, False, 
    [ "you batter {enemyName} with your rolling pin dealing {damage} damage", ], 
    None, 
    None)

Dev10usBlade = Weapon(
    "Dev10us Blade", 0b11100000, 400, 50, 5, False, 
    [ "you slice %s's head in half with the Dev-10us Blade dealing %s damage", ], 
    [ "you throw the Dev-10us Blade at %s's Skull causing it to break like an egg dealing %s damage", ], 
    [ "the Dev-10us Blade summoned a mystical creature to attack %s, they dealt %s damage", ])