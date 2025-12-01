import time
import sys
from colorama import Fore, Style
from rpg.tools.save_load_manager import select_load_slot
from rpg.tools import audio_manager
from rpg.dialogues.stormbound_lore import show_stormbound_lore
from rpg.dialogues.factions import show_faction_overview
from rpg.dialogues.class_overview import show_class_overview
from rpg.dialogues.ranks_info import show_rank_info


def game_intro():
    audio_manager.play_music("stormbound menu", volume=0.6, loop=True)
    while True:
        print("\n[----------------------------------------------------------]")
        print("                    -{ STORMBOUND HAVEN }-                      ")
        print("[----------------------------------------------------------]\n")

        print(f"{Fore.LIGHTGREEN_EX+ Style.BRIGHT}Tip: Consider reading the Overviews [2] first before playing"
              f" for more enjoyable experience!{Style.RESET_ALL}\n")

        current_player = None


        print(" ============ [MENU] ============")
        print("[1] - Start Game |  [2] - Stormbound Lore & Factions/Classes Overview")
        print("[3] - Load Game File |  [4] - Credits")
        print("                     [5] - Quit")

        choice = input("-->  ")

        match choice:

            case "1":
                print("\nStarting game...")
                time.sleep(1.4)
                audio_manager.music_fadeout(duration=2000)
                audio_manager.music_stop()
                current_player = None

                break

            case "2":
                while True:
                    print("\n--- STORMBOUND OVERVIEW --- ")
                    print("[1] - Stormbound Lore")
                    print("[2] - Factions Overview")
                    print("[3] - Classes Overview")
                    print("[4] - Stormbound Ranks Overview")
                    print("[X] - Exit Menu")

                    choice = input("\n>> ").strip().lower()

                    if choice == "1":
                        show_stormbound_lore()

                    elif choice == "2":
                        show_faction_overview()

                    elif choice == "3":
                        show_class_overview()

                    elif choice == "4":
                        show_rank_info()

                    elif choice == "x":
                        print("Returning to menu...")
                        break

                    else:
                        print("Invalid choice, please pick a choice from the menu!")
                        time.sleep(1)

            case "3":
                loaded_player = select_load_slot()

                if loaded_player is not None:
                    current_player = loaded_player
                    break

                continue

            case "4":
                print("                   ---- CREDITS ----")
                print("\nWriting and Story: [Github] - DScriptz | Dwayne Japor\n")
                print("Sounds: [Pixabay] - https://pixabay.com,"
                      " [Myinstants]- https://www.myinstants.com/en/index/us,"
                      " [Tabletop Audio] - https://tabletopaudio.com\n")
                print("Code: [Github] - DScriptz | Dwayne Japor\n")
                time.sleep(1.5)

            case "5":
                print("Thanks for playing my game! Hope you try it again!")
                time.sleep(1.3)
                sys.exit()

    return current_player





