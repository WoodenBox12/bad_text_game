inventory = """
main weapon is %s 
╔════════════════════════════════════════════════════╗ 
║ to change your main weapon type:    mw weapon═name ║ 
║ to use a heal type:                  use item═name ║ 
╚════════════════════════════════════════════════════╝"""

battle = """
╔═══════════════════════╗ 
║ 0 = player, {red('X')} = enemy ║ your health: {player.currentHealth}/{player.maxHealth}    their health: {opponent.currentHealth}/{opponent.maxHealth}
║                       ║ {player.xpReq[player.level - 1]-player.xp} xp away from level {player.level + 1}
║   ╭───────────────╮   ║ 
║   │   ╭───────╮   │   ║ 
║   │   │   0 {opponent.Range(0)} │ {opponent.Range(1)} │ {opponent.Range(2)} ║ 
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