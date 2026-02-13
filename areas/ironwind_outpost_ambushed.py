import time
from colorama import Fore, Style
from tools.audio_manager import play_sound
from game_modules.battle import Battle
from models.enemy import spawn_enemy

reset = Style.RESET_ALL


def enter_ambushed_outpost(player):
    print(f"\n{Fore.RED}=================================================={reset}")
    print(f"{Fore.RED}              [Ironwind Outpost]{reset}")
    print(f"{Fore.RED}=================================================={reset}")
    time.sleep(2)

    print("\nThe vehicle stops at the outpost gates.")
    print("Smoke rises from the market. The smell of ozone and burning metal fills the air.")
    time.sleep(1.5)
    print(f"Guard: 'They're already inside! {player.name}, we need to push them back!'")
    time.sleep(1.5)

    print("\nSuddenly, a squad of D-Corp drones descends from the sky!")
    time.sleep(1.5)


    print(f"\n{Fore.RED}Enemy Encounter!{reset}")
    enemy = spawn_enemy("D-Corp D7 Flying Drone")
    battle = Battle(player, enemy)
    battle.fight(player, enemy)

    if player.health <= 0:
        return player

    print("\nYou scrap the drone, sparking and sputtering on the ground.")
    time.sleep(1.5)
    print(f"Kael Rowan's voice crackles on the radio: '{player.name}! If you can hear me, get to the Command Center!'")
    print("Kael Rowan: 'They are targeting the power grid! But the market is also under heavy fire!'")
    time.sleep(2)

    while True:
        print(f"\n{Fore.YELLOW}What will you do?{reset}")
        print("[1] - Rush to the Command Center to help Kael (Priority: Mission)")
        print("[2] - Head to check the Alley of Remedies to save the shopkeepers (Priority: People)")

        choice = input("\n>> ").strip()

        if choice == "1":
            play_sound("ui", 0.9)
            print("\nYou sprint towards the Command Center, ignoring the chaos in the market...")
            time.sleep(1.5)
            command_center_path(player)
            break
        elif choice == "2":
            play_sound("ui", 0.9)
            print("\nYou hurry towards the market stalls, weapon ready...")
            time.sleep(1.5)
            market_path(player)
            break
        else:
            print("Invalid choice.")

    return player


def command_center_path(player):
    print("You rush through the debris. D-Corp soldiers are setting up a barricade.")
    time.sleep(1.5)

    print(f"\n{Fore.RED}Enemy Encounter!{reset}")
    print("A heavy trooper blocks your path!")

    enemy = spawn_enemy("Ironclad Scavenger")
    enemy.name = "D-Corp Heavy Trooper"
    battle = Battle(player, enemy)
    battle.fight(player, enemy)

    if player.health <= 0:
        return

    print("\nYou breach the Command Center doors.")
    time.sleep(1.5)
    print("Kael is there, wounded, firing at intruders.")
    time.sleep(1.5)
    print(f"Kael Rowan: '{player.name}! Good timing. Help me clear these bastards!'")
    time.sleep(1.5)
    print("Together, you and Kael secure the command room.")
    time.sleep(1.5)
    print("Kael Rowan: 'Gahh, another one of those pricks!'")

    print(f"\n{Fore.RED}Enemy Encounter!{reset}")

    enemy.name = 'D-Corp Brogue Assassin'

    enemy = spawn_enemy("D-Corp Rogue Assassin")
    battle = Battle(player, enemy)
    battle.fight(player, enemy)




def market_path(player):
    print("You arrive at the market. The stalls are burning.")
    print("Rhys is pinned down by a robotic hound.")
    time.sleep(1.5)

    print(f"\n{Fore.RED}Enemy Encounter!{reset}")
    enemy = spawn_enemy("Ravager Wolf")

    """ 
    JUST TEMPORARILY USED THE STATS OF THE RAVAGER WOLF TO MAKE THE CYBER HOUND
    
    """

    enemy.name = "D-Corp Cyber-Hound"
    battle = Battle(player, enemy)
    battle.fight(player, enemy)

    if player.health <= 0:
        return

    print("\nRhys nods at you. 'Thanks, kid. Go help Kael, I'll secure the others!'")
    time.sleep(1.5)
    print("You head towards the Command Center to regroup with Kael.")
    time.sleep(1.5)
    print("You arrive at the Command Center, seeing Kael finishing off an intruder.")

