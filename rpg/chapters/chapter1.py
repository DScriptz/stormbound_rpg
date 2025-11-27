""" IMPORTS """
import time
import random
from rpg.tools import audio_manager
from rpg.models.player import Player
from rpg.class_data import class_info, class_stats
from colorama import Fore, Style
from rpg.tools.save_load_manager import select_save_slot
from rpg.dialogues.class_overview import show_class_overview

""" GAME INTRO, BASICALLY JUST A PARAGRAPH EXPLAINING THE GAME'S LORE """

def intro():
    audio_manager.play_music("chapter1&2", volume=1.1, loop=True)

    skip_choice = input("Do you want to skip the intro? (Y/N): ").lower().strip()

    match skip_choice:
        case "n":
            print("\nThe winds blow outside and the rain pelted the rooftops...")
            time.sleep(0.6)
            print("You woke up in a cold wooden floor, your head hurting, and smoke still lingers in the air..")
            time.sleep(1.2)
            print(f"Five years has passed since the '{Fore.WHITE + Style.DIM}Storm{Style.RESET_ALL}' tore the world apart")
            time.sleep(1.2)
            print("And now you find your self in a haven that is nowhere but safe...")
            time.sleep(0.9)
            print("The troubled world out there, it needs a savior...")
            time.sleep(1.1)
        case _:
            print("You skipped the dialogue!")

""" HANDLES THE CHAPTER 1 OF THE GAME """

def chapter1():
    intro()
    print("\n---------------------- Chapter 1: Awakening ----------------------")
    print("\nSo you there... Introduce yourself as you venture in this world: ")
    name = input("\n>>  ").strip()

    while name == "":
        print("\nSo you there... Introduce yourself as you venture in this world: ")
        name = input("\n>> ").strip()

    show_class_overview()
    input("[Enter] - Continue:  ")
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

        player.current_chapter = 2

        select_save_slot(player)

        player.introduce()
    else:
        print("\nInvalid class selection. Defaulting to Random Class ")

        random_class = class_stats['1', '2', '3', '4', '5']
        chosen_class = random.choice(random_class)
        default_stats = chosen_class

        player = Player(
            name,
            default_stats['name'],
            default_stats['health'],
            default_stats['max_health'],
            default_stats['attack']
        )

        player.special_ability = default_stats.get('ability', 'None')

        player.current_chapter = 2

        select_save_slot(player)

        player.introduce()



    return player






