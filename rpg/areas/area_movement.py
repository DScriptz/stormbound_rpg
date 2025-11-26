import random
import time
from rpg.models.enemy import spawn_enemy
from rpg.game_modules import Battle

""" DATA_GRAVE LOCATION'S MOVEMENT """

def handle_data_grave_movement(player):
    encounter_chance = 45

    roll = random.randint(1, 100)
    if roll <= encounter_chance:
        print("A SUDDEN AMBUSHH!!!")
        time.sleep(1.3)

        enemies_to_roll = ['Guard Drone', 'Wasteland Ghoul', 'Zero-Day Thief']

        enemy_name = random.choice(enemies_to_roll)

        enemy = spawn_enemy(enemy_name)

        battle = Battle(player, enemy)
        player = battle.fight(player)

    else:
        print("You walk forward to the Data Graves")
    return player

