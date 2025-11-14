""" IMPORTS """
import time
from stormbound_rpg.enemy import *
from stormbound_rpg.game_modules import Battle
""" HANDLES CHAPTER 3 OF THE GAME """

def chapter3(player):
    print("\n---------------------- Chapter 3: Shadows of the Ironwind. ----------------------")
    time.sleep(0.6)
    print(f"Kael Rowan: 'As you can see, the pathway to our hideout still isn't... safe'")
    time.sleep(1.3)
    print(f"Kael Rowan: 'Keep your eyes u-'")
    time.sleep(1.3)
    print("Suddenly, a thief jumped out from the shadows stabbing Kael!")
    time.sleep(1.3)
    print(f"Kael Rowan: '*grunts* {player.name}, I can't fight it's up to you!'")
    time.sleep(1.5)

    """ RESETS THE PLAYER'S HEALTH """
    player.health = player.max_health

    """ SPAWNS THE ENEMY """
    enemy = spawn_enemy("Thief")
    battle = Battle(player, enemy)
    battle.fight()


