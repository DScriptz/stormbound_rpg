import random
import time
from tools.audio_manager import play_music, music_stop, music_fadeout
from game_modules.battle import Battle
from models.enemy import spawn_enemy
from colorama import Fore, Style

reset = Style.RESET_ALL

def show_dialogue(player):
    play_music("manhunt", volume=0.7, loop=True)
    if player.faction == "Ironwinders":
        print("\nYou catch your breath after that grueling battle...")
        time.sleep(1.5)
        print("After a while, Your Encrypted Cellphone rings and it's Kael, you answered.")
        time.sleep(1.2)
        print(f"Kael Rowan: '{player.name}, Commander Thorne has advised us that the D-Corp has issued a manhunt,'")
        time.sleep(1.2)
        print("Kael Rowan: Where are you right now?")
        time.sleep(0.8)
        print(f"{player.name}: 'I'm at *looks around* uhh, my GPS told me this is at the Foundry, "
              f"I just killed a guy named C.T Kane-'")
        time.sleep(1.8)
        print("Kael Rowan: 'KANE?! You better get out of there now!! That 'Guy' you killed was one of the higher-ups "
              "at D-Corp!!'")
        time.sleep(1.7)
        print("Kael Rowan: *alarm blares off* 'Go back to the base ASAP!!'")
        time.sleep(1.1)
        print("After you heard this you an as fast as you can back to the hardpoint...")
    else:
        print("You catch your breath after that grueling battle...")
        time.sleep(1.2)
        print("After a while, you sneakily went back to the Hardpoint...")
        time.sleep(1.2)

        music_fadeout(duration=2000)
        music_stop()
    return player

def after_battle(player):
    """Handles the transition from The Molten spill back to the Hardpoint menu."""
    from areas.the_hardpoint_area import go_to_the_hardpoint

    show_dialogue(player)
    player.location = "The Hardpoint"
    player.location_steps = 0

    return go_to_the_hardpoint(player)


def handle_player_boss_fight(player):
    player.health = player.max_health
    play_music("boss music 1", volume=0.7, loop=True)
    print("\nYou trek this open area, it seems to be so quiet... Unnervingly quiet.")
    time.sleep(1)
    print("*THUD*- You hear a loud noise from around the corner...")
    time.sleep(0.8)
    print("You peeked, *BEEP* the tall, slim, and the weird human/robot infused figure looked at you...")
    time.sleep(1.5)
    print("Unknown: 'Hmm? An unidentified asset eh? You must be perfect for a test subject!! "
          "C.T Kane (Cyber Tactical) is what they call me'")
    time.sleep(1.8)
    print("C.T Kane: 'Once I defeat you, you'll be a test subject for D-Corp MUWAHAHAHAH!!'")
    time.sleep(1.4)


    print(f"\n{Fore.RED + Style.BRIGHT}                             === BOSS BATTLE ==={reset}")
    time.sleep(1.7)

    bonus_loot = 500

    enemy = spawn_enemy('C.T Kane')
    battle = Battle(player, enemy)
    battle.fight(player, enemy)

    music_fadeout(2000)
    music_stop()

    print("C.T Kane: 'ARGHHHHHH- You will pay for your- *faints*'")
    time.sleep(1.5)
    player.stormmarks += bonus_loot

    print(f"You defeated a {Fore.RED}Boss{reset}! You got a bonus +{bonus_loot} SMK")
    time.sleep(1.5)
    player.boss_defeated += 1

    after_battle(player)
    return player


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
        handle_player_boss_fight(player)

    else:
        player.location_steps += 5
        print("You jump over safely!")
        time.sleep(0.8)
        print(f"{player.name}: 'Phew, that was close...'")
        time.sleep(1)
        print(f"You reached {player.location_steps} step(s) now.")
        handle_player_boss_fight(player)
    return player


def handle_wait(player):
    player.location_steps += 1
    print("You took a step back and waiting for the Molten Lava to cool down a bit..")
    time.sleep(1.5)
    print(f"{player.name}: 'Whew, okay this might be smart...'")
    time.sleep(0.7)
    print("As the Molten sort of cools down, you got a thick metal sheet and placed it over the molten and walked on "
          "top of it cautiously")
    time.sleep(1.2)
    print(f"You reached {player.location_steps} step(s) now.")

    handle_player_boss_fight(player)

    return player
