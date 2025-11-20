import time
from colorama import Fore, init, Style
init(autoreset=True)

bounty_list = {
    "A": {
        "name": "Guard Drone CPU Retrieval",
        "target_item": "Drone CPU",
        "required": 5
        ,"prize": 500
    },
    "B": {
        "name": "Wasteland Ghoul Hunting",
        "target_item": "Ghoul Fingers",
        "required": "3",
        "prize": 350
    }

}

def view_bounty_board(player):
    """ SHOW AVAILABLE BOUNTIES """
    print(f"                             -- [ {Fore.RED + Style.BRIGHT}WATCH POST BOUNTY LIST{Style.RESET_ALL} ] --")
    player.show_status()
    print("Commander Thorne: 'Well well, choose your work, fresh meat. Don't waste my time.'")
    time.sleep(1.4)

    print("======================== BOUNTY LIST ========================")
    for i, bounty in bounty_list.items():
        print(f"\n[{i}]: {bounty['name']} - Collect {bounty['required']}x '{bounty['target_item']}' for {bounty['prize']} SMK")
        print("[X] - Exit Menu")
    print("=============================================================")
    time.sleep(1.3)

    print(f"{player.name}: 'Bounties... let's see...'")
    time.sleep(1.3)

    bounty_choice = input("\n>> ").lower().strip()

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

    bounty_id = input("Which bounty ID (A, B, C...) do you want to submit? >> ").strip().lower()

    if bounty_id not in bounty_list:
        print("\nCommander Thorne: 'That Bounty ID isn't on the board, get serious!'")
        time.sleep(1.3)
        return True

    bounty = bounty_list[bounty_id]
    target_item = bounty_list['target_item']
    required_amount = bounty_list['required']

    """ CHECKS THE AMOUNT OF THE REQUIRED ITEMS IN PLAYER'S INVENTORY"""
    current_amount = player.inventory.get(target_item, 0)

    if current_amount >= required_amount:
        player.remove_item(target_item, required_amount)
        player.stormmarks += bounty['prize']

        print(f"Commander Thorne: 'Bounty {bounty_id} cleared. Reward granted: {bounty['prize']} SMK.'")
        print(f"Items cleared from your inventory: {required_amount}x {target_item}")
    else:
        print(f"Commander Thorne: 'Argh, I said don't waste my time! You only have {current_amount} {target_item}s. Go back and finish the job!'")
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

