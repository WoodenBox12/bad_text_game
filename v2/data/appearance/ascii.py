from data.appearance.console import Console

inventory = f"""main weapon is %s 
+----------------------------------------------------+ 
| to change your main weapon type:    mw weapon-name | 
| to use a heal type:                  use item-name | 
+----------------------------------------------------+ 
>>"""

battle = """+-----------------------+ 
| 0 = player, {Console.Colour("X", "1;31;40")} = enemy | your health: {player.currentHealth}/{player.maxHealth}    their health: {opponent.currentHealth}/{opponent.maxHealth}
|      ___________      | {player.xpReq[player.level - 1]-player.xp} xp away from level {player.level + 1}
|     /   _____   \     | 
|    /   /     \   \    | 
|   |   |   0{Console.Colour("{:^3}", "1;31;40")}|{Console.Colour("{:^3}", "1;31;40")}|{Console.Colour("{:^3}", "1;31;40")}| 
|    \   \_____/   /    | 
|     \___________/     | 
|                       | 
+-----------------------+ 
|  a/away to move away  | 
|t/toward to move toward| 
|    i for inventory    | 
|                       | 
|   melee/ranged/magic  | 
|       for attack      | 
+-----------------------+ 
>>"""