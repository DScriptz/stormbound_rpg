import time
import random
from tools.audio_manager import play_sound, music_stop
from colorama import Fore, Style

reset = Style.RESET_ALL


def handle_cache_loot(player):
    music_stop()
    play_sound("data processing", 1.5)
    print(f"\n{Fore.LIGHTGREEN_EX}[ PROCESSING SALVAGE ]{reset} Accessing the console...")
    time.sleep(2.5)
    print("\nThe vault's inventory data transfers to your Cache. You collect the key items and SMK.")
    time.sleep(1.2)

    smk_reward = random.randint(130, 150)
    item_reward = "Fieldcare Pack MK-II"

    player.stormmarks += smk_reward
    player.inventory[item_reward] = player.inventory.get(item_reward, 0) + 2

    print(f"\n[ REWARD RECEIVED ]")
    print(f"  + {smk_reward} Stormmarks (New SMK total: {player.stormmarks})")
    print(f"  + 2x {item_reward}")

    player.location = "The Hardpoint"
    player.location_steps = 0

    print("\nYou secured the loot and are headed back to The Hardpoint...")
    time.sleep(1.2)

    from areas.the_hardpoint_area import go_to_the_hardpoint

    player.location_steps = 0

    return go_to_the_hardpoint(player)



