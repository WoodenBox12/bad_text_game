from os import system, name
from enum import Enum
    
class Console:

    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def Colour(text,code) -> str:

        return f"\33[{code}m{text}\33[0m"
    
    class FgColour(Enum):
        Black=30
        Red=31
        Green=32
        Yellow=33
        Blue=34
        Purple=35
        Cyan=36
        White=37

    class BgColour(Enum):
        Black=40
        Red=41
        Green=42
        Yellow=43
        Blue=44
        Purple=45
        Cyan=46
        White=47