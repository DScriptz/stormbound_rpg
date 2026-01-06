import random
import time
from tools.audio_manager import play_sound
from colorama import Fore, Style


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
                price_increase = random.randint(5, 10)
                item = self.stock[choice]

                if player.stormmarks >= item.price:
                    total_price = item.price
                    if player.faction_standing >= 5:
                        player.stormmarks -= int(total_price // 1.5)

                    elif player.faction_standing < 0:
                        player.stormmarks -= int(total_price + price_increase)

                    else:
                        player.stormmarks -= total_price
                    player.inventory[item.name] = player.inventory.get(item.name, 0) + 1
                    sounds = ['purchase', 'purchase 2']
                    random_sound = random.choice(sounds)
                    play_sound(random_sound, volume=0.7)
                    print(f"\nYou bought {item.name} for {total_price} SMK!")
                    time.sleep(0.6)
                    add_faction_respect(player)

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


def add_faction_respect(player):
    respect = random.randint(1, 2)

    if not player.faction:
        print("\nYou have no Faction. No faction respected earned")
        time.sleep(1)
        return player

    if random.random() <= 0.60:
        player.faction_standing += respect
        print(f"\nYou earned some respect from your Faction '{player.faction}' +{respect}")
        time.sleep(0.8)
        if player.faction_standing >= 5:
            player.faction_standing = 5
            print(
                f"\nYou reached the maximum Faction Respect of 5! You got the uttermost Respect from your Faction '{player.faction}'.")
            time.sleep(1.2)

        elif player.faction_standing <= -5:
            player.faction_standing = -5
            print(
                f"Better be careful, your Faction doesn't Respect you! Player Faction Respect: {player.faction_standing}.")
            time.sleep(1.2)
        print(f"\nYour Faction Respect is now {player.faction_standing}")
        time.sleep(0.9)




    return player
