from data.appearance.console import Console

battle = f"""╔═══════════════════════╗ 
║ 0 = player, {Console.Colour("X", "1;31;40")} = enemy ║ your health: 
║                       ║ 
║   ╭───────────────╮   ║ 
║   │   ╭───────╮   │   ║ 
║   │   │   0{Console.Colour("{:^3}", "1;31;40")}│{Console.Colour("{:^3}", "1;31;40")}│{Console.Colour("{:^3}", "1;31;40")}║ 
║   │   ╰───────╯   │   ║ 
║   ╰───────────────╯   ║ 
║                       ║ 
╠═══════════════════════╣ 
║  a/away to move away  ║ 
║t/toward to move toward║ 
║    i for inventory    ║ 
║                       ║ 
║   melee/ranged/magic  ║ 
║       for attack      ║ 
╚═══════════════════════╝"""
class Setup:
    Classes = """select player class
╔═══╦═══════════════════╗ 
║ 1 ║ Knight            ║ 
╠═══╬═══════════════════╣ 
║ 2 ║ Barbarian         ║ 
╠═══╬═══════════════════╣ 
║ 3 ║ Archer            ║ 
╠═══╬═══════════════════╣ 
║ 4 ║ Mage              ║ 
╚═══╩═══════════════════╝"""


experimentalinventory = """
items
main weapon is %s 
║{:<20}║{:<18}║{:<4}║{:<4}║{:<4}║
║Name                ║DMG Type          ║DMG ║CRIT║MULT║
╠════════════════════╬══════════════════╬════╬════╬════╣
║Nate's Battle Axe   ║melee/ranged/magic║69  ║100%║2X  ║
║                    ║                  ║    ║    ║    ║ 20 chars, 18 chars, 4 chars, 4 chars, 4 chars
║Apple               ║Heal              ║40  ║    ║    ║ how show this?
║                    ║                  ║    ║    ║    ║
║                    ║                  ║    ║    ║    ║
╠════════════════════╩══════════════════╩════╩════╩════╣
║ to change your main weapon type:      mw weapon═name ║ 
║ to use a heal type:                    use item═name ║ 
╚══════════════════════════════════════════════════════╝
"""
class Inventory:

    WeaponHeader = "║Name                          ║DMG Type          ║DMG ║CRIT║MULT║"
    Divider = "╠══════════════════════════════╬══════════════════╬════╬════╬════╣"
    DataEntry = "║{:<30}║{:<18}║{:<4}║{:<4}║{:<4}║"
    Tail = """╠══════════════════════════════╩══════════════════╩════╩════╩════╣ 
║ to change your main weapon type:                mw weapon name ║ 
║ to use a heal type:                              use item name ║ 
║ to drop an item type:                           drop item name ║ 
╚════════════════════════════════════════════════════════════════╝"""# make 30 chars name