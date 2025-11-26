import time
from colorama import Fore, Style, init
from rpg.game_modules.bounty_board import view_bounty_board, collect_bounty, leave_watch_post
from rpg.tools.save_load_manager import select_save_slot
init(autoreset=True)


class Location:
    def __init__(self, name, description, options, is_safe=True):
        self.name = name
        self.description = description
        self.options = options
        self.is_safe = is_safe

    def enter(self, player):
        """ DISPLAYS LOCATION AND STARTS THE INTERACTION WITH WHATEVER LOCATION THE PLAYER GOES"""
        print(f"\n                                          --- {self.name.upper()} ---")
        print(self.description)
        time.sleep(0.8)

        while True:
            print(f"\n====== [{self.name}] ======")

            for key, (label, func) in self.options.items():
                print(f"{Fore.LIGHTYELLOW_EX}[{key}]{Style.RESET_ALL} - {label}")
            print(f"{Fore.LIGHTYELLOW_EX}[S] - Show Stats")
            print(f"{Fore.LIGHTYELLOW_EX}[I]{Style.RESET_ALL} - Show Inventory")
            print(f"{Fore.LIGHTYELLOW_EX}[C]{Style.RESET_ALL} - Save Game")
            choice = input("\n>> ").strip().lower()

            if choice == 's':
                player.show_status()
                continue
            if choice == 'i':
                player.show_inventory()
                continue
            if choice == "c":
                select_save_slot(player)
                continue

            if choice in self.options:
                destination = self.options[choice][1]

                if destination(player) is False:
                    break
            else:
                print(f"{player.name}: 'Where do I go...'")

        return player

""" DEFINES THE WATCH POST IN CHAPTER 4'S LOCATION """

watch_post = Location(
    "Ironwind Watch Post",
    "\nA reinforced, guarded bunker near the west perimeter. Commander Thorne is watching you from behind a thick pane of security glass.",
    {
        "1": ('View the Bounty Board', view_bounty_board),
        "2": ('Collect Bounty', collect_bounty),
        "3": ('Exit the Ironwind Watch Post', leave_watch_post)
    }
)

