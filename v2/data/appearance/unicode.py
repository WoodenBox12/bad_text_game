from data.appearance.console import Console

inventory = f"""main weapon is %s 
╔════════════════════════════════════════════════════╗ 
║ to change your main weapon type:    mw weapon═name ║ 
║ to use a heal type:                  use item═name ║ 
╚════════════════════════════════════════════════════╝"""

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
╚═══════════════════════╝


║   ╭───────────────╮   ║ 
║   │   ╭───────╮   │   ║ 
║   │   │   0 X │ X │ X ║ ▩
║   │   ╰───────╯   │   ║ 
║   ╰───────────────╯   ║ 
"""

classes = """select player class
╔═══╦═══════════════════╗ 
║ 1 ║ Knight            ║ 
╠═══╬═══════════════════╣ 
║ 2 ║ Barbarian         ║ 
╠═══╬═══════════════════╣ 
║ 3 ║ Archer            ║ 
╠═══╬═══════════════════╣ 
║ 4 ║ Mage              ║ 
╚═══╩═══════════════════╝
"""


experimentalinventory = """
items
main weapon is %s 

║Name                ║DMG Type          ║DMG ║CRIT║MULT║
╠════════════════════╬══════════════════╬════╬════╬════╣
║Nate's Battle Axe   ║melee/ranged/magic║69  ║100%║2X  ║
║                    ║                  ║    ║    ║    ║ 20 chars, 18 chars, 4 chars, 4 chars, 4 chars
╠════════════════════╩══════════════════╩════╩════╩════╣
║ to change your main weapon type:      mw weapon═name ║ 
║ to use a heal type:                    use item═name ║ 
╚══════════════════════════════════════════════════════╝
"""