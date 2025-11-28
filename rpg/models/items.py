import time

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

            print(f"\nYou used {self.name} to tend to your wounds!")
            time.sleep(0.5)
            print(f"\n{player.name} healed for {healing_amount} HP! Current health: {player.health}\n")
            time.sleep(0.7)

            return True

        if self.damage > 0:
            player.attack += self.damage
            print(f"\nYou equipped {self.name}! Increasing your total damage to {player.attack}!")
            time.sleep(0.7)

            return True

        return False




