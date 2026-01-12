
import time
import random

from areas.ironwind_outpost_ambushed import enter_ambushed_outpost
from tools.audio_manager import play_music, play_sound
from colorama import Fore, Style

reset = Style.RESET_ALL


def handle_choice(player):
    while True:
        print("[1] - Crawl and sneak out of the battle (-20 Faction Respect, +10 Max Health)")
        print("[2] - Sneakily grab the fallen gun on the ground and try to shoot the "
              "remaining enemies (50% Chance to fail, high risk, high reward)")

        choice = input("\n>> ").strip()

        if choice == "1":
            print("You crawled under the car, then quickly ran away without being noticed. ")
            time.sleep(1.5)
            player.max_health += 10
            player.faction_standing -= 20
            print(f"Your max HP increased to {player.max_health} and Faction Respect is now: {player.faction_standing}")

        elif choice == "2":
            if random.random() <= 0.50:
                print("You crawled towards the Pistol and grabbed it...")
                time.sleep(1.2)
                play_sound("slinger gun", volume=1)
                input(f"\n[Enter] - Shoot Gun")
                play_sound("gunshot", volume=0.9)
                print(f"BANG! {Fore.RED}Headshot{reset}! ")
                time.sleep(1.2)
                print("\nYou aim at the next enemy shooting towards the guards' direction...")
                time.sleep(1.5)
                play_sound("slinger gun", volume=1)
                input(f"\n[Enter] - Shoot Gun")
                play_sound("gunshot", volume=0.9)
                print(f"BANG! Another {Fore.RED}headshot{reset}")
                time.sleep(2)
                print("The assailants fell to the ground and the guards went to you to help...")
            else:
                print("You tried to crawl towards the gun but you got shot in the leg...")
                time.sleep(1.3)
                print("Just as then, the guards successfully shot the assailants")
                time.sleep(1.3)
                print("The guards then went to you and helped you stand up...")

                if player.health <= 0:
                    player.health = 0
                else:
                    player.health -= 30

                loot = 300
                player.stormmarks += 300

                print(f"You lost 30 HP... but gained {loot} SMK for helping!")
                time.sleep(1.8)

            return player


def show_dialogue(player):
    print("\nYou and the guards now stole the car of the assailants, and drove away...")
    time.sleep(1.3)
    print(f"30 minutes later: *Radio beeps* '{player.name}, Guards you alright? I saw on the GPS that the vehicle is out of signal.'")
    time.sleep(1.7)
    print(f"You picked up the radio, Kael Rowan: {player.name}: 'We... are fine, we were ambushed. Probably D-Corp men...'")
    time.sleep(1.7)
    print(f"*Explosion over the radio*, Kael Rowan: 'GET OVER HERE ASAP, WE ARE BEING AMBUSHED I REPEAT WE ARE BEING AMBUSHED- *cuts off*'")
    time.sleep(1.7)
    print("You and the guards were alerted and stepped on the gas and hurried to the Ironwind Outpost...")
    time.sleep(1.7)
    return player


def chapter5(player):
    play_music("chapter5", volume=0.7, loop=True)
    print("\n---------------------- Chapter 5: Make... or break ----------------------")

    print("\nYou signaled the Ironwinders' Guards to come pick you up,")
    time.sleep(1.2)
    print("Guards: 'Get in, we have to be careful. The base is on full alert.'")
    time.sleep(1.4)
    print("\n45 minutes later, you and the guards are nearing the base, when suddenly-")
    time.sleep(1.8)
    print("*CRASH*")
    time.sleep(1.2)
    print("You open your eyes, all dizzy, seeing the guards shoot at the vehicle that just rammed you over...")
    time.sleep(1.7)
    print("The 2 guards were struggling to get a hold of the assailants... One of them got shot-")
    time.sleep(1.5)
    print("\nWhat would you do?")
    player = handle_choice(player)
    player = show_dialogue(player)

    player = enter_ambushed_outpost(player)
    return player
