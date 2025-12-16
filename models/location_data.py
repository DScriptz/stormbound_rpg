import time

from colorama import Fore, Style
from dialogues.game_tips import show_tips
from game_modules.bounty_board import view_bounty_board, collect_bounty, leave_watch_post
from game_modules.map import show_map
from game_modules.pause_menu import show_menu
from tools.audio_manager import play_sound, initialize_audio

reset = Style.RESET_ALL
initialize_audio()

class Location:
    def __init__(self, name, description, options, is_safe=True):
        self.name = name
        self.description = description
        self.options = options
        self.is_safe = is_safe

    def enter(self, player):
        """ DISPLAYS LOCATION NAME AND STARTS THE INTERACTION WITH WHATEVER LOCATION THE PLAYER GOES"""
        print(f"\n                                                            --- {self.name.upper()} ---")
        print(self.description)
        time.sleep(0.8)

        while True:
            print(f"\n====== [{self.name}] ======")
            show_tips()

            for key, (label, func) in self.options.items():
                print(f"{Fore.LIGHTYELLOW_EX}[{key}]{reset} - {label}")

            print("\n====== OPTIONS ======")
            print(f"{Fore.GREEN}[S]{reset} - [Show Stats] | "
                  f"{Fore.GREEN}[I]{reset} - [Show Inventory]")
            print(f"{Fore.GREEN}[U]{reset} - [Use an Item from Inventory] | {Fore.GREEN}[B]{reset} - [Show Active Bounty]")

            choice = input("\n>> ").strip().lower()

            match choice:

                case 's':
                    play_sound("ui", 0.9)
                    player.show_status()
                    continue

                case'i':
                    play_sound("ui", 0.9)
                    player.show_inventory()
                    continue

                case "x":
                    play_sound("ui", 0.9)
                    break

                case "b":
                    play_sound("ui", 0.9)
                    player.show_active_bounty()
                    continue

                case "u":
                    play_sound("ui", 0.9)
                    player.use_item()

                case "m":
                    play_sound("ui", 0.9)
                    show_map()
                    continue

            if choice in self.options:
                play_sound("ui", 0.9)
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
        "0": ('Pause Game', show_menu),
        "X": ('Exit the Ironwind Watch Post', leave_watch_post)
    }
)

