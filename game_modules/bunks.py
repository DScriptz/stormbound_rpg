import time
from colorama import Fore, init, Style

def rent_room(player):
    cost = 30

    print(f"\n{Fore.CYAN}Bunk's Attendant:{Style.RESET_ALL} 'A coil bunk costs {cost} SMK's for the night.'")
    print("Do you want to rent the bunk? (Y/N)")

    choice = input("\n>> ").strip().lower()

    if choice == "y":
        if player.stormmarks >= cost:
            player.stormmarks -= cost
            player.health = player.max_health
            print(f"You bought a bunk for {cost} SMK!")
            time.sleep(1.2)
            print(f"{player.name}: 'Ahh, finally a good night's rest...'")
            time.sleep(1.1)
            print(f"You slept gracefully, restoring youre health back to full health! {player.max_health}")
            time.sleep(1.2)
            player.show_status()
        else:
            print(f"\n{Fore.RED}Bunk's Attendant: 'Tsk, that SMK ain't enough stranger. You need {cost} SMK's'")
            time.sleep(1.2)

    return True

def leave_bunk(player):
    print(f"{player.name}: 'It was nice here.'")
    time.sleep(1.2)

    return False



