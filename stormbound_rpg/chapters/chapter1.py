from player import Player
from classes import *
import time

""" GAME INTRO, BASICALLY JUST A PARAGRAPH EXPLAINING THE GAME'S LORE """

def game_intro():
    print("[----------------------------------------------------------]")
    print("                   -{ STORMBOUND HAVEN }-                      ")
    print("[----------------------------------------------------------]")
    time.sleep(1)
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

""" HANDLES THE CHAPTER 1 OF THE GAME """

def chapter1(player=None):
    game_intro()
    if player is None:
        print("\n---------------------- Chapter 1: Awakening ----------------------")
        print("\nSo you there... Introduce yourself as you venture in this world: ")
        name = input("\n>>  ")

        print("\nPick your class (Type the name of the class): ")
        class_info()
        class_choice = input("\n>> ").strip().lower()

        stats = class_stats.get(class_choice, {"health": 50, "attack": 30, "ability": None})

        player = Player(name, class_choice, stats['health'], stats['attack'])
        player.special_ability = stats['ability']

        player.introduce()
    return player






