""" IMPORTS """
from tools import audio_manager
from models.player import Player
from class_data import Class, class_info, class_stats


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


        print("\nPick your class (Type the name of the class, if blank or not in list, stats of Riftblade is default): ")
        class_info()

        class_choice = input("\n>> ").strip().lower()


        stats = class_stats.get(class_choice, {"health": 63, "max_health": 63, "attack": 12, "ability": None})

        player = Player(name, class_choice, stats['health'], stats['max_health'], stats['attack'])

        player.special_ability = stats['ability']

        player.introduce()


    return player






