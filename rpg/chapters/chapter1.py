
from rpg.player import Player

from rpg.class_data import *

from rpg.player import play_music, pygame

import time

""" GAME INTRO, BASICALLY JUST A PARAGRAPH EXPLAINING THE GAME'S LORE """

def game_intro():
    play_music("chapter1&2", volume=1, loop=True)
    print("[----------------------------------------------------------]")
    print("             -{ STORMBOUND HAVEN }-                      ")
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

        while True:
            print("\nPick your class (Type the name of the class): ")
            class_info()

            class_choice = input("\n>> ").strip().lower()

            if class_choice == "":
                print("\nPick a class from the list.")
                time.sleep(0.4)
                continue

            stats = class_stats.get(class_choice, {"health": 50, "max_health": 50, "attack": 30, "ability": None})

            player = Player(name, class_choice, stats['health'], stats['max_health'], stats['attack'])

            player.special_ability = stats['ability']

            player.introduce()
            pygame.mixer.music.fadeout(2000)
            break

    return player






