import time
import sys
from colorama import Fore, Style, init
from rpg.tools.save_load_manager import select_save_slot
from rpg.dialogues.ranks_info import show_rank_info
from rpg.game_modules.game_intro import show_overview
from rpg.dialogues.game_tips import show_tips


init(autoreset=True)
reset = Style.RESET_ALL


def handle_game_exit():
    while True:
        print(f"{Fore.LIGHTRED_EX}NOTE: Remember to save your game before exiting!{reset}")
        print("\nAre you sure you want to exit the game (Y/N)?")

        choice = input("\n>> ").strip().lower()

        match choice:
            case "y":
                print("Thanks for playing!")
                sys.exit()
            case "n":
                break

            case _:
                print("\nInvalid Choice!")
    return


def show_progression_guide(player):
    """
    Shows the sub-menu for Progression (Titles, Chapters).
    """
    while True:
        print(f"\n{Fore.CYAN + Style.BRIGHT}--- SURVIVAL GUIDE: PROGRESSION ---{reset}")
        print(f"Current Chapter: {player.current_chapter}")
        print("\n[V] - View Title Progression (Status/Battles)")
        print("[X] - Back to Pause Menu")

        choice = input("\n>> ").lower().strip()

        if choice == 'v':
            show_rank_info()
            continue

        elif choice == 'x':
            break
        else:
            print(f"{Fore.RED}Invalid selection.{reset}")

    return


def show_roleplaying_guide(player):
    """

    Shows the sub-menu for Roleplaying Systems (Respect Meter, Weapon Weilding, etc.).

    """
    while True:
        print(f"\n{Fore.CYAN + Style.BRIGHT}--- SURVIVAL GUIDE: ROLEPLAYING SYSTEMS ---{reset}")
        print(f"\nYour Faction: {player.faction}")
        print(f"{Fore.YELLOW}{player.name}'s Faction Standing:{reset} {player.faction_standing} Respect")
        print("\nThis system tracks your reputation with local groups.")
        print("Positive respect (0 is neutral, but respected) opens up better deals and safer dialogue options.")
        print("Negative respect may result in hostile interactions or higher prices.")
        print("\n--- SURVIVAL GUIDE: WEAPON WIELDING ---")
        print("\nThis system for now is just for Roleplay Purposes and immersion.")
        print("At the start of the game, you have the choice to type your weapon choice,"
              " \nyou can even use your imagination and wield a weapon that's of your own creation!")
        print("This roleplaying system may also serve a purpose in interaction with NPCs or general shop dialogues.")

        print("\n[X] - Back to Pause Menu")

        choice = input("\n>> ").upper().strip()

        if choice == 'X':
            break
        else:
            print(f"{Fore.RED}Invalid selection.{reset}")

    return


def show_survival_guide(player):
    """

    The main hub for the Survival Guide.

    """
    while True:
        print(f"\n{Fore.MAGENTA + Style.BRIGHT}--- SURVIVAL GUIDE ARCHIVE ---{reset}")
        print("Select a feature to review the mechanics.")
        print("====================================")
        show_tips()
        print("\n[1] - Titles and Progression")
        print("[2] - Roleplaying Systems (Reputation, Doctrine)")
        print("[3] - Combat Reference (Status Effects, Mechanics)")
        print("\n[X] - Back to Pause Menu")

        choice = input("\n>> ").lower().strip()

        if choice == '1':
            show_progression_guide(player)
            continue

        elif choice == '2':
            show_roleplaying_guide(player)
            continue

        elif choice == '3':
            print(f"{Fore.YELLOW}Coming SOON:{reset} Combat Reference not yet available.")
            time.sleep(1)

        elif choice == 'x':
            break

        else:
            print(f"{Fore.RED}Invalid selection.{reset}")

    return


def show_menu(player):
    while True:
        show_tips()
        print("\n           --- >GAME PAUSED< ---")
        print("[1] - Resume Game  |  [2] - Survival Guide (Game Guide)")
        print("[3] - Save Game  |  [4] - Stormbound RPG Overview")
        print("                         [X] - Quit Game")

        choice = input("\n>> ").lower().strip()

        match choice:

            case "1":
                break

            case "2":
                show_survival_guide(player)

            case "3":
                select_save_slot(player)

            case "4":
                show_overview()

            case "x":

                handle_game_exit()

            case _:
                print(f"{Fore.RED + Style.BRIGHT}Invalid Choice!{reset}")

    return
