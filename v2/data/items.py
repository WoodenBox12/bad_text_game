
class Item:
    Name: str
    Type: bytes

    SingleUse: bool

class Weapon:
    Name: str
    Type: bytes #  Me: 0b10000000, Ra: 0b01000000, Ma: 0b00100000, Heal: 0b00010000
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

class Heal:# mabye change single use to uses
    Name: str
    Type: bytes

    Amount: int
    SingleUse: bool

    def __init__(self, Name, Type, Amount, SingleUse) -> None:
        self.Name = Name
        self.Type = Type
        self.Amount = Amount
        self.SingleUse = SingleUse

"""class AntiqueBow(Weapon):
    Name = "Antique Bow"
    Type = 0b01000000
    Damage = 45
    CritChance = 10
    CritDamage = 2.5

    SingleUse = False

    RaMsg = ["you fire an arrow at {enemyName} dealing {damage} damage", ]"""

class Items:

    AntiqueBow = Weapon(
        "Antique Bow", 0b01000000, 45, 10, 2.5, False, 
        None, 
        ["you fire an arrow at {enemyName} dealing {damage} damage", ], 
        None
    )

    Wand = Weapon(
        "Wand", 0b00100000, 55, 10, 3, False, 
        None, 
        None, 
        ["you wave your wand at {enemyName} dealing {damage} damage", ]
    )

    DogSpit = Weapon(
        "Dog Spit", 0b01000000, 40, 10, 2, False, 
        None, 
        ["you spit at {enemyName} dealing {damage} damage", ], 
        None
    )

    RollingPin = Weapon(
        "Rolling Pin", 0b10000000, 30, 8, 2, False, 
        [ "you batter {enemyName} with your rolling pin dealing {damage} damage", ], 
        None, 
        None
    )

    CavemanClub = Weapon(
        "Caveman Club", 0b10000000, 40, 10, 3, False, 
        [ "you attempt to cave in {enemyName}'s skull dealing {damage} damage", ], 
        None, 
        None
    )

    SawnOff = Weapon(
        "Matt's Sawn Off", 0b01000000, 44, 4, 4, False, 
        None, 
        [ "you shoot {enemyName} dealing {damage} damage", ], 
        None
    )

    Rifle = Weapon(
        "Jack's Rifle", 0b11000000, 1000, 55, -2, False, 
        [ "you stabbed {enemyName} with your bayonet dealing {damage} damage", ], 
        [ "you shoot {enemyName} dealing {damage} damage", ], 
        None
    )

    Cube = Weapon(
        "Olly's Cube", 0b10100000, 60, 15, 3, False, 
        [ "you whack {enemyName}'s head dealing {damage} damage", ], 
        None, 
        [ "nobody knows how but somehow {enemyName} took {damage} damage", ]
    )

    FryingPan = Weapon(
        "Liam's Fry", 0b10000000, 40, 5, 3, False, 
        [ "you whack {enemyName}'s head dealing {damage} damage", ], 
        None, 
        None
    )

    Dev10usBlade = Weapon(
        "Dev10us Blade", 0b11100000, 400, 50, 5, False, 
        [ "you slice {enemyName}'s head in half with the Dev-10us Blade dealing {damage} damage", ], 
        [ "you throw the Dev-10us Blade at {enemyName}'s Skull causing it to break like an egg dealing {damage} damage", ], 
        [ "the Dev-10us Blade summoned a mystical creature to attack {enemyName}, they dealt {damage} damage", ]
    )


    Apple = Heal(
        "Apple", 0b00010000, 40, True
    )

    StaleCookie = Heal(
        "Stale Cookie", 0b00010000, 50, True
    )



    weapons: list = [AntiqueBow, Wand, DogSpit, RollingPin, CavemanClub, SawnOff, Rifle, Cube, FryingPan, Dev10usBlade]