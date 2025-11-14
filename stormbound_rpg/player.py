
""" IMPORTS """
import random
import time


"""
   THIS HANDLES THE PLAYER'S DATA

   This handles the name choosing of the player and the way they introduce themselves

"""

class Player:
    def __init__(self, player_name, player_class, health=50, max_health=50, attack=10):
        self.name = player_name
        self.player_class = player_class
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.cooldown = 0
        self.level = 1
        self.inventory = {}
        self.stormmarks = 0
        self.special_ability = None

    """ 
        PLAYER'S STATS BEING SHOWN
    
        Example:
                Dwayne | Health: 100 | Attack: 50
                Gold: 20 | Level 5
                Inventory: {}
                
    """
    def introduce(self):
        print(f"\n{self.name}, the {self.player_class.title()} | Health: {self.health}/{self.max_health}  | Attack: {self.attack}")
        print(f"\nStormmarks: {self.stormmarks} | Level: {self.level}")
        print(f"\nInventory: {self.inventory}")

    """ PLAYER TAKES DAMAGE """

    def take_damage(self, damage):
        self.health -= damage

        """ ENSURES THE PLAYER'S HEALTH DONT BECOME NEGATIVE """

        if self.health <= 0:
            self.health = 0


        if self.health == 0:
            print("\nYou died... your vision blurs...")
            time.sleep(0.95)

    def player_attack(self, enemy):
        damage = random.randint(self.attack - 5, self.attack + 5)
        print(f"\n{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)

    def use_ability(self, enemy):
        if self.cooldown > 0:
            print(f"{self.special_ability} is on cooldown for {self.cooldown} more turn(s)!")
            return


        if self.player_class == "Aethermancer":
            extra_damage = random.randint(2, 4)
            print(f"You unleash {self.special_ability}, strucking the enemy with arcane energy!")
            enemy.take_damage(self.attack + extra_damage)
        else:
            print(f"{self.special_ability} is on cooldown! You lost your turn.")
            time.sleep(1.1)

