
import time

""" THIS HANDLES THE SHOP """

class Shop:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def open_shop(self, player):
        print(f"\n                                                                                        -- Welcome to the {self.name} -- ")
        print()
        for key, item in self.stock.items():
            print(f"[{key}] {item.name} - Price: {item.price} SMK | Heal: {item.heal} | Damage: {item.damage} | {item.description}")
        print("[X] - Exit menu")

        print(f"\n{player.name}: 'Hmm what should I buy...'")
        time.sleep(0.6)

        choice = input("\n >>  ").lower().strip()

        if choice in self.stock:
            item = self.stock[choice]
            if player.stormmarks >= item.price:
                player.stormmarks -= item.price
                player.health = min(player.max_health, player.health + item.heal)
                player.attack += item.damage
                player.inventory[item.name] = player.inventory.get(item.name, 0) + 1
                print(f"\nYou bought {item.name} for {item.price} SmK!")
                time.sleep(0.6)
            else:
                print(f"{player.name}: 'Ehh, I don't have enough SMK's *sighs*' ")
                time.sleep(1)

        elif choice == "x":
            print(f"\nYou walked away from the shop")
            time.sleep(0.7)
            return
        else:
            print("\nInvalid choice!")


