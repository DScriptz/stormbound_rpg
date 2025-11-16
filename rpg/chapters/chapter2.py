import time
from rpg.enemy import *
from rpg.game_modules import Battle

""" HANDLES CHAPTER 2 OF THE GAME """
def intro(player):
    skip_choice = input("\nDo you want to skip the dialogue? (Y/N): ").lower().strip()
    match skip_choice:
        case "n":
            print("---------------------- Chapter 2: The Encounter... ----------------------")
            time.sleep(0.8)
            print(f"\n{player.name}: *prepares their bag* 'Hmm, this should be good.'")
            time.sleep(1.5)
            print("You walked out, the door creaks as you open, and you step out into this seemingly vast, broken world...")
            time.sleep(1.56)
            print("After hours of cautious travel, you saw a hidden encampment along the ruins...")
            time.sleep(1.7)
            print("A man suddenly steps forward from the shadows, pointing a gun at you...")
            time.sleep(1.2)
            print("\nStranger: 'And who might you be...?'")
            time.sleep(1.5)
            print("\nYou put your hands up and told him, ")
            time.sleep(0.7)
            print(f"\n{player.name}: 'My name is {player.name}, I wish to just seek supplies for survival...'")
            time.sleep(1.6)
        case _:
            print("\nYou skipped the dialogue!")

    return player

def chapter2(player):
    intro(player)
    print("Stranger: 'Hmm, alright. I am Kael Rowan. The leader of the Ironwind Outpost.'")
    time.sleep(1.3)
    print(f"Kael Rowan: 'So then {player.name}, I will lend you supplies if you prove you're trustworthy.'")
    time.sleep(1.4)
    print(f"Kael Rowan: 'I want you to kill a Ravager Wolf for me'")
    time.sleep(1.4)
    print("Kael Rowan: 'Go over in that wrecked car, and find the wolf, tough luck.'")
    time.sleep(1.5)
    print("So you walked towards the wrecked car...")
    time.sleep(1.3)
    print("Suddenly a Wolf jumps out from the car, growling at you!")
    time.sleep(1.3)
    """ CREATES THE UPDATED ENEMY OBJECT FROM ENEMY DICTIONARY """

    enemy = spawn_enemy("Ravager Wolf")
    battle = Battle(player, enemy)
    battle.fight()

    """ WHEN PLAYER KILLS WOLF """
    print("\nAs you defeat the wolf, Kael Rowan claps his hand and walks slowly towards you..")
    time.sleep(1.5)
    print("\nKael Rowan: 'Well well, you got some guts huh?'")
    time.sleep(1.3)
    print("Kael Rowan: 'As promised, come with me *signals for you to follow him to the hideout*'")
    time.sleep(1.5)

    player.stormmarks += 20

    print(f"Congratulations! Stormmarks + 20. Your SMK now: {player.stormmarks}")

    player.level += 1

    print(f"\nYou leveled up! Level is now: {player.level}")
    time.sleep(0.3)
    input("\nPress [Enter] to continue >> ")


