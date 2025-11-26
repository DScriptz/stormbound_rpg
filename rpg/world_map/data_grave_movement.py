import random
import time
from rpg.models.enemy import spawn_enemy
from rpg.game_modules import Battle
from rpg.game_modules.loot_handler import handle_loot


""" DATA_GRAVE LOCATION'S MOVEMENT """
def handle_player_ambushed(player):
    encounter_chance = 50

    roll = random.randint(1, 100)
    if roll <= encounter_chance:
        print("As you walk, An enemy suddenly ambushes you!!!")
        time.sleep(1.3)

        enemies_to_roll = ['Guard Drone', 'Wasteland Ghoul', 'Zero-Day Thief']

        enemy_name = random.choice(enemies_to_roll)

        enemy = spawn_enemy(enemy_name)

        battle = Battle(player, enemy)
        battle.fight(player)

        handle_loot(player, enemy)

        level_up_chance = 47

        roll = random.randint(1, 100)
        if roll <= level_up_chance:
            player.level_up()

    else:
        print("You walk forward seeing nothing but dirt, metals and abandoned buildings...")
        time.sleep(0.4)

    return player


def handle_data_grave_movement_forward(player):
    handle_player_ambushed(player)

    return player

