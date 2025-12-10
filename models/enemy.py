import random
import time
from colorama import Style, Fore

reset = Style.RESET_ALL

""" LIST OF ENEMIES THE PLAYER CAN ENCOUNTER/FIGHT """
enemies = {
    "Wasteland Ghoul": {
        "health": 65,
        "max_health": 65,
        "attack": 12,
        "ability": "Quick Strike",
        "prize": "Ghoul Fingers"
    },

    "Ash Goblin": {
        "health": 60,
        "max_health": 60,
        "attack": 10,
        "ability": "Scavenge",
        "prize": 70
    },

    "Ravager Wolf": {
        "health": 55,
        "max_health": 55,
        "attack": 8,
        "ability": None,
        "prize": 35
    },

    "Guard Drone": {
        "health": 70,
        "max_health": 70,
        "attack": 12,
        "ability": "Electrocute",
        "prize": "Drone CPU"
    },
    "Ironclad Scavenger": {
        "health": 90,
        "max_health": 90,
        "attack": 15,
        "ability": "Shell Block",
        "prize": 80
    },
    "Thief": {
        "health": 60,
        "max_health": 60,
        "attack": 10,
        "ability": None,
        "prize": 80
    },
    "Zero-Day Thief": {
        "health": 72,
        "max_health": 72,
        "attack": 12,
        "ability": None,
        "prize": 65
    },
    "Slag-Eel": {
        "health": 60,
        "max_health": 60,
        "attack": 16,
        "ability": "Swarm",
        "prize": 80
    },
    "Heat-Tempered Sentinel": {
        "health": 95,
        "max_health": 95,
        "attack": 12,
        "ability": "Disuptor",
        "prize": "Lazer-Infused Blade"
    },
    "The Foreman's Echo": {
        "health": 90,
        "max_health": 90,
        "attack": 11,
        "ability": None,
        "prize": "S-7 Intel Chip"
    },
    "C.T Kane": {
        "health": 100,
        "max_health": 100,
        "attack": 15,
        "ability": 'Enrage',
        "prize": 'D-HQ Keys'
    }
}

# enemy Object
class Enemy:
    def __init__(self, name, health, max_health, attack, ability=None, loot=0, is_weakened=False):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.ability = ability
        self.stunned = False
        self.loot = loot
        self.is_weakened = is_weakened
        self.weakness_factor = 0.0
        self.is_bleeding = False
        self.bleed_damage = 0
        self.bleed_turns = 0


    """ THIS HANDLES THE PART WHEN THEY GET HIT OR DAMAGED """

    def take_damage(self, damage):
        defense_chance = 0.3
        damage_reduction = random.uniform(0.2, 0.5)

        final_damage = round(damage, 1)

        if random.random() < defense_chance:

            reduction_amount = damage_reduction * damage

            rounded_reduction_amount = round(reduction_amount, 1)

            final_damage = damage - rounded_reduction_amount

            print(f"\n{self.name} defends against your attack! Reducing your attack!!")
            time.sleep(1.3)

        self.health -= round(final_damage, 1)
        print(f"\nThe {self.name} takes {final_damage} damage!")
        time.sleep(0.4)

    def calculate_damage(self):
        base_damage = self.attack + random.randint(-2, 2)

        if self.name == "C.T Kane" and self.health <= 50:
            print(f"\nC.T Kane is now {Fore.RED}ENRAGED!{reset} His system is overclocked (+5 Total Damage)")
            time.sleep(1.1)
            base_damage += 5

        if self.is_weakened:
            final_damage = int(base_damage * (1.0 - self.weakness_factor))

            self.is_weakened = False
            self.weakness_factor = 0.0

            return final_damage

        return base_damage


    def is_alive(self):
        return self.health > 0


    def enemy_attack(self, player):
        is_dodging = player.dodging

        if is_dodging:
            damage = 0
            print(f"\n{player.name} dodged {self.name}'s attack!")
        else:
            damage = random.randint(self.attack - 3, self.attack + 2)
            print(f"\n{self.name} attacks {player.name} for {damage} damage!")

        player.take_damage(damage)

        if is_dodging:
            player.dodging = False

        return

    def get_loot(self):
        """ CALCULATES AND RETURNS THE STORMMARKS PRIZE FOR DEFEATING THIS ENEMY """
        return self.loot

""" 
    THIS HANDLES THE SPAWNING OF THE ENEMY
    
    Example:
            stats = spawn_enemy("Thief") <--  or any enemy you want
            battle = Battle(player, enemy)
            battle.fight() <--  call the fight() function in the battle.py
            
"""

# creates stats of the enemy then spawns them in for the player to battle
def spawn_enemy(name):
    stats = enemies[name]
    return Enemy(
        name,
        stats['health'],
        stats['max_health'],
        stats['attack'],
        stats['ability'],
        loot = stats['prize']
    )

