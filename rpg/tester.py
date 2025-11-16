# --- Temporary test code ---
from shop import Shop
from rpg.items import Item
from rpg.shops.healing_shop import ironwind_apothecary
from player import Player

# Create a fake player for testing
class FakePlayer:
    def __init__(self):
        self.name = "Tester"
        self.stormmarks = 100  # so you can buy things
        self.health = 50
        self.max_health = 100
        self.attack = 10
        self.inventory = {}
        self.dodging = False

player = FakePlayer()

# Create some test items

# Create the shop
healing_shop = Shop("Ironwind Medic Bay", ironwind_apothecary)

# Print player stats BEFORE
print(f"Before buying: HP {player.health}/{player.max_health}, SMK {player.stormmarks}, ATK {player.attack}")
print(f"Inventory: {player.inventory}")

# Run shop (manually type “1”, “2”, “x”, etc when prompted)
healing_shop.open_shop(player)

# Print player stats AFTER buying
print(f"\nAfter buying: HP {player.health}/{player.max_health}, SMK {player.stormmarks}, ATK {player.attack}")



