import random
import time

from areas.the_molten_spill_area import go_to_molten_spill
from dialogues.the_foundry_walk import show_forward_dialogue, show_right_dialogue, show_left_dialogue
from game_modules import Battle
from models.enemy import spawn_enemy
from tools.audio_manager import play_music, music_fadeout, music_stop, play_sound


def handle_player_ambushed(player):

    enemies_to_roll = ['Slag-Eel', 'Heat-Tempered Sentinel', "The Foreman's Echo"]
    enemy_name = random.choice(enemies_to_roll)
    enemy = spawn_enemy(enemy_name)


    music_choices = ['battle music 5', 'battle music 6']
    music = random.choice(music_choices)
    play_music(music, volume=0.5, loop=True)

    print(f"As you wander around, the {enemy.name} suddenly ambushes you!!!")
    time.sleep(1.3)

    battle = Battle(player, enemy)
    battle.fight(player, enemy)

    music_fadeout(2000)
    music_stop()

    play_music("the foundry", volume=0.7, loop=True)
    return player


def handle_movement_forward(player):

    if random.random() < 0.60:
        handle_player_ambushed(player)
    else:
        player.location_steps += 2
        play_sound("footstep", volume=0.8)
        show_forward_dialogue()
        print(f"\nYou ran for {player.location_steps} step(s) now.")
        time.sleep(1.3)

        if player.health <= 20:
            return player

        if player.location_steps >= 15 or player.location_steps >= 17:
            return go_to_molten_spill(player)

    return player


def handle_movement_right(player):

    if random.random() < 0.65:
        player.location_steps += 1
        play_sound("footstep", volume=0.8)
        show_right_dialogue()
        print(f"\nYou walked for {player.location_steps} step(s) now.")
        time.sleep(1.3)

        if random.random() < 0.30:
            print(f"Suddenly, an enemy AMBUSHED YOU!!")
            time.sleep(1.3)
            handle_player_ambushed(player)

    else:
        print("The pile of metal sheets on the Right was a dead end. You spent time backtracking.")
        play_sound("footstep", volume=0.8)

        time.sleep(1.3)

        if random.random() < 0.20:
            print("\nAMBUSH!! You attracted unwanted attention while backtracking.")
            handle_player_ambushed(player)

    if player.health <= 0:
        return player

    if player.location_steps >= 15 or player.location_steps >= 17:
        return go_to_molten_spill(player)

    return player


def handle_movement_left(player):

    if random.random() < 0.65:
        player.location_steps += 1
        play_sound("footstep", volume=0.8)
        show_left_dialogue()
        print(f"\nYou walked for {player.location_steps} step(s) now.")
        time.sleep(1.3)

        if random.random() < 0.30:
            print(f"Suddenly, an enemy AMBUSHED YOU!!")
            handle_player_ambushed(player)

    else:
        print("The stack of dead animal bodies on the Left was a dead end. You spent time backtracking.")
        play_sound("footstep", volume=0.8)
        time.sleep(1.3)

        if random.random() < 0.20:
            print("\nAMBUSH!! You attracted unwanted attention while backtracking.")
            handle_player_ambushed(player)

    if player.health <= 0:
        return player

    if player.location_steps >= 15 or player.location_steps >= 17:
        return go_to_molten_spill(player)

    return player