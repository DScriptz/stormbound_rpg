
import random
import time


""" LIST OF ENEMIES """
enemies = {
    "Wasteland Ghoul": {"health": 70, "max_health": 70, "attack": 12, "ability": "Quick Strike"},
    "Ash Goblin": {"health": 60, "max_health": 60, "attack": 10, "ability": "Scavenge"},
    "Ravager Wolf": {"health": 55, "max_health": 55, "attack": 8, "ability": None},
    "Guard Drone": {"health": 75, "max_health": 76, "attack": 12, "ability": "Electrocute"},
    "Ironclad Beetle": {"health": 90, "max_health": 90, "attack": 15, "ability": "Shell Block"},
    "Thief": {"health": 60, "max_health": 60, "attack": 10, "ability": None}
}



class Enemy:
    def __init__(self, name, health, max_health, attack, ability=None):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.ability = ability
        self.stunned = False

    """ THIS HANDLES THE PART WHEN THEY GET HIT OR DAMAGED """

    def take_damage(self, damage):
        defense_chance = 0.2
        damage_reduction = 0.50

        final_damage = damage

        if random.random() < defense_chance:

            reduction_amount = damage_reduction * damage
            final_damage = damage - reduction_amount

            print(f"\n{self.name} defends your attack! Reducing your attack by half!")

        self.health -= final_damage
        print(f"\nThe {self.name} takes {damage} damage!")
        time.sleep(0.4)

    def is_alive(self):
        return self.health > 0

    def enemy_attack(self, player):
        if player.dodging:
            damage = 0
            print(f"\n{player.name} dodged {self.name}'s attack!")
        else:
            damage = random.randint(self.attack - 3, self.attack + 2)
            print(f"\n{self.name} attacks {player.name} for {damage} damage!")

        player.take_damage(damage)


        if player.dodging:
            player.dodging = False

        return

""" 
    THIS HANDLES THE SPAWNING OF THE ENEMY
    
    Example:
            stats = spawn_enemy("Thief") <--  or any enemy you want
            battle = Battle(player, enemy)
            battle.fight() <--  call the fight() function in the battle.py
            
"""

def spawn_enemy(name):
    stats = enemies[name]
    return Enemy(name, stats['health'], stats['max_health'], stats['attack'], stats['ability'])