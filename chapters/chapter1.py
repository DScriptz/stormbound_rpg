""" IMPORTS """
import random
import time

from colorama import Fore, Style

from class_data import class_info, class_stats
from dialogues.class_overview import show_class_overview
from models.player import Player
from tools import audio_manager
from tools.save_load_manager import select_save_slot

""" 
    GAME INTRO, BASICALLY JUST A PARAGRAPH EXPLAINING HOW THE PLAYER ENDS UP IN THIS SITUATION 
    
"""

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

""" INTRODUCES THE CHAPTER 1 OF THE GAME """

def chapter1():
    intro()
    print("\n---------------------- Chapter 1: Awakening ----------------------")
    print("\nSo you there... Introduce yourself as you venture in this world: ")
    name = input("\n>>  ").strip()

    while name == "":
        print("\nSo you there... Introduce yourself as you venture in this world: ")
        name = input("\n>> ").strip()
    print("The greatest survivors of this world has specialized in one class...")
    time.sleep(1)
    print("What class do you specialize in...?")
    time.sleep(1.3)

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
            stats['attack'],
            stats['weapon']
        )

        player.special_ability = stats.get('ability', 'None')

        player.current_chapter = 2

        select_save_slot(player)

        player.introduce()
        print("Do you want to read the Classes Info Overview?")

        choice = input("\n>> ").lower().strip()

        if choice == "n":
            return player
        else:
            show_class_overview()
            input("\n[Enter] - Continue: ")
            return player


    else:
        print("\nInvalid class selection. Defaulting to random Class... ")

        random_class = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        chosen_class = random.choice(random_class)
        default_stats = class_stats[chosen_class]

        player = Player(
            name,
            default_stats['name'],
            default_stats['health'],
            default_stats['max_health'],
            default_stats['attack'],
            default_stats['weapon']
        )

        player.special_ability = default_stats.get('ability', 'None')

        player.current_chapter = 2

        print(f"\nYour random class is {default_stats['name']}.")
        time.sleep(0.5)

        select_save_slot(player)

        player.introduce()
        print("Do you want to read the Classes Info Overview(Y/N)?")

        choice = input("\n>> ").lower().strip()

        match choice:

            case  "n":
                print()

            case _:
                show_class_overview()
                print("Loading...")
                time.sleep(1)

    return player