
import random

""" LIST OF ENEMIES """
enemies = {
    "Windling Scout": {"health": 70, "max_health": 70, "attack": 12, "ability": "Quick Strike"},
    "Ash Goblin": {"health": 60, "max_health": 60, "attack": 10, "ability": "Scavenge"},
    "Ravager Wolf": {"health": 55, "max_health": 55, "attack": 8, "ability": "Bite"},
    "Haven Marauder": {"health": 85, "max_health": 85, "attack": 13, "ability": "Slam"},
    "Ironclad Beetle": {"health": 90, "max_health": 90, "attack": 15, "ability": "Shell Block"},
    "Thief": {"health": 60, "max_health": 60, "attack": 12, "ability": None}
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
        self.health -= damage
        print(f"\nThe {self.name} takes {damage} damage!")

    def is_alive(self):
        return self.health > 0

    def enemy_attack(self, target):
        if target.dodging:
            print(f"\n{self.name} dodged {target.name}'s attack")
            target.dodging = False
            damage = 0
        else:
            damage = random.randint(self.attack - 3, self.attack + 2)
            print(f"\n{self.name} attacks {target.name} for {damage} damage!")

        target.take_damage(damage)
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