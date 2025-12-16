import time
from colorama import Fore, Style
from tools.rank_up import get_rank
from tools import audio_manager

reset = Style.RESET_ALL


def handle_levelup_stats(player):

    while True:
        print("Which one of your stats would you like to upgrade: ")
        print(f"[1] - [{Fore.RED}Attack{reset}] + 5 | [2] - [{Fore.GREEN}Max Health{reset}] + 3")

        choice = input("\n>> ").strip()

        match choice:
            case "1":
                player.attack += 5
                print(f"\nYour total Attack power increased to {player.attack}!")
                time.sleep(1)
                break

            case "2":
                player.max_health += 3
                player.health += 3
                print(f"\nYour total Health increased to {player.max_health}!")
                time.sleep(1)
                break

            case _:
                print(f"{player.name}: 'Which one does benefit me more...'")
                time.sleep(0.5)


def check_rank(player):
    """
    CHECKS IF THE PLAYER HAS LEVELED (RANKED) UP

    """
    new_rank = get_rank(player)

    if new_rank != player.rank:

        player.rank = new_rank

        print(f'\nYou {Fore.GREEN}RANKED UP{reset}! New Player Rank: "{player.rank}"')
        audio_manager.play_sound("level up", volume=0.9)
        time.sleep(1)
        handle_levelup_stats(player)

    return player