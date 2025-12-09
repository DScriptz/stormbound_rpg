import time
from colorama import Fore, Style, init
from game_modules.bounty_board import view_bounty_board, collect_bounty, leave_watch_post
from game_modules.map import show_map
from dialogues.game_tips import show_tips



class Location:
    def __init__(self, name, description, options, is_safe=True):
        self.name = name
        self.description = description
        self.options = options
        self.is_safe = is_safe

    def enter(self, player):
        """ DISPLAYS LOCATION AND STARTS THE INTERACTION WITH WHATEVER LOCATION THE PLAYER GOES"""
        print(f"\n                                                            --- {self.name.upper()} ---")
        print(self.description)
        time.sleep(0.8)

        while True:
            print(f"\n====== [{self.name}] ======")
            show_tips()

            for key, (label, func) in self.options.items():
                print(f"{Fore.LIGHTYELLOW_EX}[{key}]{Style.RESET_ALL} - {label}")

            print("\n====== OPTIONS ======")
            print(f"{Fore.GREEN}[S]{Style.RESET_ALL} - Show Stats | "
                  f"{Fore.GREEN}[I]{Style.RESET_ALL} - Show Inventory")
            print(f"{Fore.GREEN}[U]{Style.RESET_ALL} - Use an Item from Inventory")

            choice = input("\n>> ").strip().lower()

            match choice:

                case 's':
                    player.show_status()
                    continue

                case'i':
                    player.show_inventory()
                    continue

                case "x":
                    break

                case "u":
                    player.use_item()

                case "m":
                    show_map()
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
        "X": ('Exit the Ironwind Watch Post', leave_watch_post)
    }
)

