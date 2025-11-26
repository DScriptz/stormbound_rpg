""" IMPORTS """
import time
# import random
from rpg.tools import audio_manager
from rpg.models.enemy import spawn_enemy
from rpg.game_modules import Battle
from rpg.tools.save_load_manager import select_save_slot
from rpg.game_modules.loot_handler import handle_loot

""" HANDLES CHAPTER 3 OF THE GAME """

def chapter3(player):
    if player.current_chapter > 3:
        return player

    if player.current_chapter < 3:
        player.current_chapter = 3

    print("\n---------------------- Chapter 3: Shadows of the Ironwind. ----------------------")
    time.sleep(0.6)
    print(f"Kael Rowan: 'As you can see, the pathway to our hideout still isn't... safe'")
    time.sleep(1.3)
    print(f"Kael Rowan: 'Keep your eyes u-'")
    time.sleep(1.3)
    print("Suddenly, a thief jumped out from the shadows stabbing Kael!")
    time.sleep(1.3)
    print(f"Kael Rowan: '*grunts* {player.name}, I can't fight it's up to you!'")
    audio_manager.music_fadeout(duration=1500)
    audio_manager.music_stop()
    print("\nLoading...")
    time.sleep(1.5)
    audio_manager.play_music("thief_fight", volume=0.4)




    """ RESETS THE PLAYER'S HEALTH """
    player.health = player.max_health

    """ SPAWNS THE ENEMY """
    enemy = spawn_enemy("Thief")
    battle = Battle(player, enemy)
    battle.fight(player)

    handle_loot(player, enemy)

    player.show_status()
    print("\nLoading dialogues...")
    audio_manager.music_fadeout(duration=2000)
    time.sleep(2)
    audio_manager.music_stop()

    input("\nPress [Enter] to continue >> ")


    """ IF PLAYER WINS, THE CHAPTER CONTINUES """

    skip_choice = input("Do you want to skip the dialogue? (Y/N): ").lower().strip()

    match skip_choice:
        case "n":

            print("\nKael Rowan: 'Gahh, come help me-'")
            time.sleep(1.2)
            print("\nYou walked towards Kael, put his arms over your shoulders and helped him")
            time.sleep(1.3)
            print("So both of you walked through this hidden tunnel, 1 mile away from where you were ambushed...")
            time.sleep(1.4)
            print("As both of you exited the tunnel, you saw a big, busy, hidden underground base!")
            time.sleep(1.4)
            print(f"Kael Rowan: '*coughs*, {player.name}, Welcome to the Ironwind Outpost.'")
            time.sleep(1.5)
            print(f"As you were looking around, the bodyguards cautiously went near both of you but Kael told them you're friendly")
            time.sleep(2)
            print(f"Kael Rowan: 'I need to get my wounds checked, feel free to walk around, {player.name} you're one of us now'")
            time.sleep(2)

        case _:
            print("You skipped the dialogue!")

    print(f"{player.name}: 'Appreciate it, I'll be sure to leave when needed. *nods*'")
    player.level_up()

    player.current_chapter = 4
    select_save_slot(player)

    return player



