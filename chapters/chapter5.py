
import time

from tools.audio_manager import play_music


def handle_choice(player):
    print("[1] - Crawl and sneak out of the battle (-20 Faction Respect, +10 Max Health)")
    print("[2] - Sneakily grab the fallen gun on the ground and shoot the re")


def chapter5(player):
    play_music("manhunt", volume=0.7, loop=True)
    print("---------------------- Chapter 5: Make... or break ----------------------")

    print("\nYou signaled the Ironwinders' Guards to come pick you up,")
    time.sleep(1.2)
    print("Guards: 'Get in, we have to be careful. The base is on full alert.'")
    time.sleep(1.4)
    print("30 minutes later, you and the guards are nearing the base, when suddenly- *CRASH*")
    time.sleep(1.8)
    print("You open your eyes, all dizzy, seeing the guards shoot at the vehicle that just rammed you over...")
    time.sleep(1.7)
    print("The 2 guards were struggling to get a hold of the assailants... One of them got shot.")
    time.sleep(1.5)
    print("\nWhat do you do?")