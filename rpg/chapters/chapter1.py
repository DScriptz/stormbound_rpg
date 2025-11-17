""" IMPORTS """
from rpg.tools import audio_manager
from rpg.models.player import Player
from rpg.class_data import Class, class_info, class_stats


import time

""" GAME INTRO, BASICALLY JUST A PARAGRAPH EXPLAINING THE GAME'S LORE """

def game_intro():
    audio_manager.play_music("chapter1&2", volume=1.1, loop=True)
    print("\n[----------------------------------------------------------]")
    print("                   -{ STORMBOUND HAVEN }-                      ")
    print("[----------------------------------------------------------]")

    skip_choice = input("Do you want to skip the intro? (Y/N): ").lower().strip()

    match skip_choice:
        case "n":
            print("\nThe winds blow outside and the rain pelted the rooftops...")
            time.sleep(0.6)
            print("You woke up in a cold wooden floor, your head hurting, and smoke still lingers in the air..")
            time.sleep(1.2)
            print("Five years has passed since the factions tore the world apart")
            time.sleep(1.2)
            print("And now you find your self in a haven that is nowhere but safe...")
            time.sleep(0.9)
            print("The troubled world out there, it needs a savior...")
            time.sleep(1.1)
        case _:
            print("You skipped the dialogue!")

""" HANDLES THE CHAPTER 1 OF THE GAME """

def chapter1(player=None):
    game_intro()
    if player is None:
        print("\n---------------------- Chapter 1: Awakening ----------------------")
        print("\nSo you there... Introduce yourself as you venture in this world: ")
        name = input("\n>>  ").strip()

        while name == "":
            print("\nSo you there... Introduce yourself as you venture in this world: ")
            name = input("\n>> ").strip()

        class_info()
        print("\nPick your class: ")

        class_choice = input("\n>> ").strip().lower()

        stats = class_stats.get(class_choice)

        if stats:
            class_name = stats['name']

            player = Player(
                name,
                class_name,
                stats['health'],
                stats['max_health'],
                stats['attack']
            )

            player.special_ability = stats.get('ability', 'None')

            player.introduce()
        else:
            print("\nInvalid class selection. Defaulting to Riftblade (Choice 2)")

            default_stats = class_stats['2']

            player = Player(
                name,
                default_stats['name'],
                default_stats['health'],
                default_stats['max_health'],
                default_stats['attack']
            )

            player.special_ability = default_stats.get('ability', 'None')

            player.introduce()

    return player






