# --- Temporary test code ---
from rpg.shops_stocks import rusted_rifle_stock
from rpg.tools import Shop
from rpg.models.items import Item
from rpg.shops_stocks.healing_shop import ironwind_apothecary
from rpg.shops_stocks.weapon_shop import rusted_rifle_stock
from rpg.models.player import Player

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
weapons_shop = Shop("The Rusted Rifle", rusted_rifle_stock)
# Print player stats BEFORE
print(f"Before buying: HP {player.health}/{player.max_health}, SMK {player.stormmarks}, ATK {player.attack}")
print(f"Inventory: {player.inventory}")

# Run shop (manually type “1”, “2”, “x”, etc when prompted)
weapons_shop.open_shop(player)
# healing_shop.open_shop(player)

# Print player stats AFTER buying
print(f"\nAfter buying: HP {player.health}/{player.max_health}, SMK {player.stormmarks}, ATK {player.attack}")



