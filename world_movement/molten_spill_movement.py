import random
import time
from tools.audio_manager import play_music, music_stop, music_fadeout
from game_modules import Battle
from colorama import Fore, Style

reset = Style.RESET_ALL

def handle_player_boss_fight(player):
    print("You trek this open area, it seems to be so quiet... Unnervingly quiet.")
    time.sleep(1)
    print("*THUD*- You hear a loud noise from around the corner...")
    time.sleep(0.8)
    print("You peeked, *BEEP* the tall, slim, and the weird human/robot infused figure looked at you...")
    time.sleep(1.1)
    print("Unknown: 'Hmm? An unidentified asset eh? You must be perfect for a test subject!! I'm C.T Kane as they call me'")
    time.sleep(1.2)
    print("C.T Kane: 'Once I defeat you, you'll be a test subject for D-Corp MUWAHAHAHAH!!'")
    time.sleep(1.1)


    print(f"\n{Fore.RED + Style.BRIGHT}=== BOSS BATTLE ==={reset}")
    time.sleep(1.3)




def handle_jump_over(player):

    if random.random() <= 0.50:
        molten_damage = random.randint(10, 20)

        if player.health > 0:
            player.health -= molten_damage
        else:
            player.health = 0

        print("\nYou jump over but your feet touched the Molten Lava!!")
        time.sleep(0.8)
        print(f"{player.name}: 'Ow! That burns, aghhh'")
        time.sleep(1)
        print(f"\nYou got burned for: {molten_damage}! Health is now: {player.health}/{player.max_health}")
        player.location_steps += 1
        print(f"You reached {player.location_steps} step(s) now.")

    else:
        player.location_steps += 5
        print("You jump over safely!")
        time.sleep(0.8)
        print(f"{player.name}: 'Phew, that was close...'")
        time.sleep(1)
        print(f"You reached {player.location_steps} step(s) now.")

    return player

def handle_wait(player):
    player.location_steps += 1
    print("You took a step back and waiting for the Molten Lava to cool down a bit..")
    time.sleep(1.1)
    print(f"{player.name}: 'Whew, okay this might be smart...'")
    time.sleep(0.7)
    print("As the Molten sort of cools down, you got a thick metal sheet and placed it over the molten and walked on "
          "top of it cautiously")
    time.sleep(1.2)
    print(f"You reached {player.location_steps} step(s) now.")

    return player
