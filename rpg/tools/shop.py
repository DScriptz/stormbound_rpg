
import time

class Shop:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def open_shop(self, player):
        while True:
            print("   ==========================================================================================================================================================")
            print(f"\n                                                                         -- Welcome to the {self.name} -- ")
            player.show_status()
            print()
            for key, item in self.stock.items():
                print(f"    [{key}] {item.name} - Price: {item.price} SMK | Heal: {item.heal} | Damage: {item.damage} | {item.description}")
            print("    [X] - Exit menu")
            print("   ==========================================================================================================================================================")

            print(f"\n{player.name}: 'Hmm what should I buy...'")
            time.sleep(1)

            choice = input("\n >>  ").lower().strip()

            if choice in self.stock:
                item = self.stock[choice]

                if player.stormmarks >= item.price:
                    player.stormmarks -= item.price
                    player.inventory[item.name] = player.inventory.get(item.name, 0) + 1
                    print(f"\nYou bought {item.name} for {item.price} SMK!")
                    time.sleep(0.6)
                    player.show_inventory()

                else:
                    print(f"\n{player.name}: 'Ehh, I don't have enough SMK's *sighs*' ")
                    time.sleep(1)

            elif choice == "x":
                print(f"\nYou walked away from the shop")
                time.sleep(0.7)
                player.show_status()
                input("Press [Enter] To Continue >> ")
                break
            else:
                print(f"\n{player.name}: 'Am I gonna buy something...? Or did I just forgot?'")
                time.sleep(1.2)


