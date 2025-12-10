import random
import time

from areas.salvage_cache_area import go_to_salvage_cache
from dialogues import data_grave_walk_right, data_grave_walk_left
from game_modules import Battle
from models.enemy import spawn_enemy
from tools.audio_manager import play_music, music_stop, music_fadeout, play_sound

""" DATA_GRAVE LOCATION'S MOVEMENT """


def handle_player_ambushed(player):

    enemies_to_roll = ['Guard Drone', 'Wasteland Ghoul', 'Zero-Day Thief']
    enemy_name = random.choice(enemies_to_roll)
    enemy = spawn_enemy(enemy_name)


    music_choices = ['battle music 2', 'battle music 3']
    music = random.choice(music_choices)
    play_music(music, volume=0.6, loop=True)

    print(f"As you walk, the {enemy.name} suddenly ambushes you!!!")
    time.sleep(1.3)


    battle = Battle(player, enemy)
    battle.fight(player, enemy)

    music_fadeout(2000)
    music_stop()

    play_music("open world", volume=0.7, loop=True)
    return player

def handle_data_grave_movement_forward(player):
    if random.random() < 0.50:
        handle_player_ambushed(player)
    else:
        from dialogues.data_grave_walk_forward import show_random_movement_line

        player.location_steps += 2
        play_sound("footstep", volume=0.8)
        show_random_movement_line()
        print(f"\nYou ran for {player.location_steps} step(s) now.")
        time.sleep(1.3)

        if player.health <= 20:
            return player

        if player.location_steps >= 20:
            return go_to_salvage_cache(player)

    return player

def handle_data_grave_movement_right(player):

    if random.random() < 0.65:
        player.location_steps += 1
        play_sound("footstep", volume=0.8)
        data_grave_walk_right.show_dialogue()
        print(f"\nYou walked for {player.location_steps} step(s) now.")
        time.sleep(1.3)

        if random.random() < 0.30:
            print(f"Suddenly, an enemy AMBUSHED YOU!!")
            time.sleep(1.3)
            handle_player_ambushed(player)

    else:
        print("The wreckage on the Right was a dead end. You spent time backtracking.")
        play_sound("footstep", volume=0.8)

        time.sleep(1.3)

        if random.random() < 0.20:
            print("\nAMBUSH!! You attracted unwanted attention while backtracking.")
            handle_player_ambushed(player)

    if player.health <= 0:
        return player

    if player.location_steps >= 20:
        return go_to_salvage_cache(player)

    return player


def handle_data_grave_movement_left(player):

    if random.random() < 0.65:
        player.location_steps += 1
        play_sound("footstep", volume=0.8)
        data_grave_walk_left.show_dialogue()
        print(f"\nYou walked for {player.location_steps} step(s) now.")
        time.sleep(1.3)

        if random.random() < 0.30:
            print(f"Suddenly, an enemy AMBUSHED YOU!!")
            handle_player_ambushed(player)

    else:
        print("The wreckage on the Left was a dead end. You spent time backtracking.")
        play_sound("footstep", volume=0.8)
        time.sleep(1.3)

        if random.random() < 0.20:
            print("\nAMBUSH!! You attracted unwanted attention while backtracking.")
            handle_player_ambushed(player)

    if player.health <= 0:
        return player

    if player.location_steps >= 20:
        return go_to_salvage_cache(player)

    return player
