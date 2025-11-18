import time
from colorama import Fore, Style, init
init(autoreset=True)

class Location:
    def __init__(self, name, description, options):
        self.name = name
        self.description = description
        self.options = options

    def enter(self, player):
        """ DISPLAYS LOCATION AND STARTS THE INTERACTION """
        print(f"\n                                          --- {self.name.upper()} ---")
        print(self.description)
        time.sleep(0.8)

        while True:
            print("\nWhere do you want to go?")

            for key, (label, func) in self.options.items():
                print(f"{Fore.LIGHTYELLOW_EX}[{key}]{Style.RESET_ALL} - {label}")
            print("[S] - Show Stats")

            choice = input("\n>> ").strip().lower()

            if choice == 's':
                player.show_status()
                continue

            if choice in self.options:

                destination = self.options[choice][1]

                if destination(player) is False:
                    break
            else:
                print(f"{player.name}: ...")

        return player
