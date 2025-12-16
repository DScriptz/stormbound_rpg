import time

from colorama import Fore, Style

from tools import audio_manager
from tools.rank_up import get_rank


def check_rank(player):
    new_rank = get_rank(player)

    if new_rank != player.rank:

        player.rank = new_rank

        print(f'\nYou {Fore.GREEN}RANKED UP{Style.RESET_ALL}! New Player Rank: "{player.rank}"')
        audio_manager.play_sound("level up", volume=0.9)
        time.sleep(1)

    return player