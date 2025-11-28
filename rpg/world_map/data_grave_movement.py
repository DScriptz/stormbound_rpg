import random
import time
from rpg.models.enemy import spawn_enemy
from rpg.game_modules import Battle
from rpg.game_modules.loot_handler import handle_loot
from rpg.tools.audio_manager import play_music, music_stop, music_fadeout


""" DATA_GRAVE LOCATION'S MOVEMENT """
def handle_player_ambushed(player):
    play_music("open world", volume=0.7, loop=True)
    encounter_chance = 50

    roll = random.randint(1, 100)
    if roll <= encounter_chance:
        """ 
        
            CHOOSES  A RANDOM ENEMY NAME FROM THE ENEMY LIST THEN IF PICKED, THAT'S THE PLAYER'S ENEMY 
            
        """

        enemies_to_roll = ['Guard Drone', 'Wasteland Ghoul']

        enemy_name = random.choice(enemies_to_roll)

        enemy = spawn_enemy(enemy_name)

        """ PICKS A RANDOM MUSIC FOR BATTLE"""
        music_choices = ['battle music 2', 'battle music 3']
        music = random.choice(music_choices)

        play_music(music, volume=0.6,loop=True)

        print(f"As you walk, the {enemy.name} suddenly ambushes you!!!")
        time.sleep(1.3)

        battle = Battle(player, enemy)
        battle.fight(player)

        handle_loot(player, enemy)

        level_up_chance = 40

        roll = random.randint(1, 100)

        if roll <= level_up_chance:
            player.level_up()
        music_fadeout(2000)
        music_stop()
    else:
        print("You walked forward, seeing nothing but dirt and abandoned buildings,")
        print("And metal scraps flying because of the wind in the distance...")
        time.sleep(1.3)

    return player

def handle_data_grave_movement_forward(player):

    handle_player_ambushed(player)
    return player