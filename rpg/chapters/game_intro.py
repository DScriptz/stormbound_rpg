import time
import sys
from colorama import Fore, Style
from rpg.tools.save_load_manager import select_load_slot
from rpg.tools import audio_manager
from rpg.dialogues.stormbound_lore import show_stormbound_lore
from rpg.dialogues.factions import show_faction_overview
from rpg.dialogues.class_overview import show_class_overview
from rpg.dialogues.ranks_info import show_rank_info

reset = Style.RESET_ALL

def show_credits():
    print("                   ---- CREDITS ----")
    print("\nWriting and Story: [Github] - DScriptz / Dwayne Japor\n")
    print("Sounds: [Pixabay] - https://pixabay.com,"
          " [Myinstants]- https://www.myinstants.com/en/index/us,"
          " [Tabletop Audio] - https://tabletopaudio.com\n")
    print("Code: [Github] - DScriptz / Dwayne Japor\n")
    time.sleep(1.5)
    return

def show_overview():
    while True:
        print("\n--- STORMBOUND OVERVIEW --- ")
        print("[1] - Stormbound Lore  |  [2] Factions Overview")
        print("[3] - Classes Overview |  [4] Player Ranks (Level) Info")
        print("[X] - Exit Menu")
        print("------------------------------")
        choice = input("\n>> ").strip().lower()

        match choice:

            case "1":
                show_stormbound_lore()
                continue

            case "2":
                show_faction_overview()
                continue

            case  "3":
                show_class_overview()
                continue

            case "4":
                show_rank_info()
                continue

            case "x":
                print("Returning to menu...")
                break

            case _:
                print("Invalid choice, please pick a choice from the menu!")
                time.sleep(0.8)

    return


def game_intro():
    audio_manager.play_music("stormbound menu", volume=0.6, loop=True)
    while True:
        print("\n[----------------------------------------------------------]")
        print("                    -{ STORMBOUND HAVEN }-                      ")
        print("[----------------------------------------------------------]\n")

        print(f"{Fore.LIGHTGREEN_EX+ Style.BRIGHT}Tip: Consider reading the Overviews [2] first before playing"
              f" for more enjoyable experience!{reset}\n")

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
                show_overview()

            case "3":
                loaded_player = select_load_slot()

                if loaded_player is not None:
                    current_player = loaded_player
                    break

                continue

            case "4":
                show_credits()


            case "5":
                print(f"{Fore.BLUE + Style.BRIGHT}Thank you for playing my game! Hope you try it again!{reset}")
                time.sleep(1.3)
                sys.exit()

    return current_player





