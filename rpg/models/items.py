
""" HANDLES THE FUNCTIONALITY OF THE ITEMS PLAYERS MAY USE """

class Item:
    def __init__(self, name, price, heal=0, damage=0, description=""):
        self.name = name
        self.price = price
        self.heal = heal
        self.damage = damage
        self.description = description
    
    def use(self, player):
        if self.heal > 0:

            if player.health >= player.max_health:
                print(f"You are already at full health. Item not used")
                return False

            healing_amount = min(self.heal, player.max_health - player.health)
            player.health = min(player.max_health, player.health + self.heal)

            print(f"{player.name} healed for {healing_amount} HP! Current health: {player.health}")

            return True

        return False




