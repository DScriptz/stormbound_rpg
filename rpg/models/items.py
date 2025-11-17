
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
            player.health += min(player.max_health, player.health + self.heal)
            print(f"{player.name} healed for {self.heal} HP! Current health: {player.health}")
