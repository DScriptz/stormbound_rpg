import random
import time

from colorama import Fore, Style

from tools.audio_manager import play_sound


class Shop:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def open_shop(self, player):
        while True:
            print("   ==========================================================================================================================================================")
            print(f"\n                                                                         -- Welcome to the {self.name} -- ")
            print(f"\n{Fore.GREEN + Style.BRIGHT}[Shopkeeper's Note: 'If you bought an item that can increase your stat, you need to equip/use that item via the option '[U] - Use an Item from Inventory' to get its effect!]'{Style.RESET_ALL}")
            player.show_status()
            print()
            for key, item in self.stock.items():
                print(f"    [{key}] {item.name} - Price: {item.price} SMK | Heal: {item.heal} | Damage: +{item.damage} | HP Increase (Armor): +{item.armor} | {item.description}")
            print("    [X] - Exit menu")
            print("   ==========================================================================================================================================================")

            print(f"\n{player.name}: 'Hmm what should I buy...'")


            choice = input("\n >>  ").lower().strip()

            if choice in self.stock:
                item = self.stock[choice]

                if player.stormmarks >= item.price:
                    player.stormmarks -= item.price
                    player.inventory[item.name] = player.inventory.get(item.name, 0) + 1
                    sounds = ['purchase', 'purchase 2']
                    random_sound = random.choice(sounds)
                    play_sound(random_sound, volume=0.7)
                    print(f"\nYou bought {item.name} for {item.price} SMK!")
                    time.sleep(0.6)

                else:
                    print(f"\n{player.name}: 'Ehh, I don't have enough SMK's *sighs*' ")
                    time.sleep(1)

            elif choice == "x":
                print(f"\nYou walked away from the shop")
                time.sleep(0.7)
                player.show_status()
                break
            else:
                print(f"\n{player.name}: 'Am I gonna buy something...? Or did I just forgot?'")
                time.sleep(1)


