import time
from colorama import Fore, init, Style
init(autoreset=True)

bounty_list = {
    "A": {
        "name": "Guard Drone CPU Retrieval",
        "target_item": "Drone CPU",
        "required": 8,
        "prize": 560,
        "description": 'A Drone found surveying in the Data Grave. It is believed to have been placed by the corrupt'
                       ' Citadel Watch government...'
    },
    "B": {
        "name": "Wasteland Ghoul Hunting",
        "target_item": "Ghoul Fingers",
        "required": 5,
        "prize": 400,
        "description": 'A mysterious Ghoul found wandering around The Hardpoint, just near the border of The Data Grave.'
                       'They are dangerous, mythical and powerful.'

    }

}

def view_bounty_board(player):
    """ SHOW AVAILABLE BOUNTIES """
    print(f"                             -- [ {Fore.RED + Style.BRIGHT}WATCH POST BOUNTY LIST{Style.RESET_ALL} ] --")
    player.show_status()
    print("\nCommander Thorne: 'Well well, choose your work, fresh meat. Don't waste my time.'\n")
    time.sleep(1.4)
    print(f"\n{player.name}: 'Bounties... let's see...'")
    time.sleep(1.3)

    print("======================== BOUNTY LIST ========================")
    for i, bounty in bounty_list.items():
        print(f"""\n[{i}]: {bounty['name']} - Collect {bounty['required']}x '{bounty['target_item']}' for {bounty['prize']} SMK.  
[{Fore.RED + Style.BRIGHT}INFO{Style.RESET_ALL}]: {bounty['description']}""")
    print("\n[X] - Exit Menu")
    print("=============================================================")

    bounty_choice = input("\n>> ").upper().strip()

    if bounty_choice in bounty_list:
        chosen_bounty = bounty_list[bounty_choice]

        if player.active_bounty is None:
            player.active_bounty = chosen_bounty

            print(f"\nCommander Thorne: 'Now, your job is **{chosen_bounty['name']}**.")
            time.sleep(1.2)
            print(f"**Bounty Accepted!** You must collect {chosen_bounty['required']}x {chosen_bounty['target_item']}.")
            time.sleep(1.4)
        else:
            print(f"\nCommander Thorne: 'You still have a bounty, {player.name}. Finish it first!'")
            time.sleep(1.5)

    elif bounty_choice == "x":
        print("\nCommander Thorne: 'Fine, get outta here.'")
        time.sleep(1.2)
    else:
        print("\nCommander Thorne: 'That is not a valid ID!'")
        time.sleep(1.2)

    return True


def collect_bounty(player):
    """ CHECKS INVENTORY AND GIVES THE REWARDS """
    print("\nCommander Thorne: 'Hand me the proof, I don't care about your stories.'")
    time.sleep(1.2)

    bounty_id = input("Which bounty ID (A, B, C...) do you want to submit? >> ").strip().upper()

    if bounty_id not in bounty_list:
        print("\nCommander Thorne: 'That Bounty ID isn't on the board, get serious!'")
        time.sleep(1.3)
        return True

    bounty = bounty_list[bounty_id]
    target_item = bounty['target_item']
    required_amount = bounty['required']

    """ CHECKS THE AMOUNT OF THE REQUIRED ITEMS IN PLAYER'S INVENTORY"""
    current_amount = player.inventory.get(target_item, 0)

    if current_amount >= required_amount:
        player.remove_item(target_item, required_amount)
        player.stormmarks += bounty['prize']

        print(f"\nCommander Thorne: 'Bounty {bounty_id} cleared. Good job kid. +{bounty['prize']} SMK.'")
        time.sleep(1.3)
        print(f"\nItems cleared from your inventory: {required_amount}x {target_item}")
        time.sleep(1.3)
        player.active_bounty = None

    else:
        print(f"\nCommander Thorne: 'Argh, I said don't waste my time! You only have {current_amount} {target_item}s. Go back and finish the job!'")
        time.sleep(1.3)
    return True

""" SIGNALS TO THE LOCATION CLASS TO EXIT THE LOOP """
def leave_watch_post(player):
    if player.bounty_completed >= 1:
        print(f"{player.name}: 'That was rough, but worth it...'")
        time.sleep(1.3)
    else:
        print(f"{player.name}: 'Well, that was something-'")
        time.sleep(1.3)

    return False

