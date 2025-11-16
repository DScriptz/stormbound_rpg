
""" IMPORTS """
import random
import time
import os
import pygame

""" SOUND HELPERS WHEN PLAYING SOUNDS OR MUSIC """

def play_sound(sound_name, volume=0.6 ):
    try:
        sound_path = os.path.join("sounds", f"{sound_name}.ogg")
        sound = pygame.mixer.Sound(sound_path)
        sound.set_volume(volume)
        sound.play()
    except Exception as e:
        print(f"[Sound Error] Couldn't play '{sound_name}': {e}")

# Game long sounds/musics helper code (loop version)

def play_music(music_name, volume=0.5, loop=True ):
    try:
        music_path = os.path.join("sounds", f"{music_name}.ogg")
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1 if loop else 0)
    except Exception as e:
        print(f"[Music Error] Couldn't play '{music_name}': {e}")


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
        self.dodging = False
        self.stunned = False

    """ 
        PLAYER'S STATS BEING SHOWN
    
        Example:
                Dwayne | Health: 100 | Attack: 50
                Gold: 20 | Level 5
                Inventory: {}
                
    """
    def introduce(self):
        print(f"\n{self.name}, the {self.player_class.title()} | Health: {self.health}/{self.max_health}  | Attack: {self.attack}")
        print(f"\nStormmarks (SMK): {self.stormmarks} | Level: {self.level}")
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
            time.sleep(1.5)
            return


        elif self.player_class == "aethermancer":
            extra_damage = random.randint(3, 5)
            print(f"You unleash {self.special_ability}, strucking the enemy with arcane energy!")
            time.sleep(1.5)
            enemy.take_damage(self.attack + extra_damage)

            self.cooldown = 3

        elif self.player_class == "stormwarden":
            damage = random.randint(10, 14)
            print(f"{self.name} unleashed Thunder Strike!! Dealing {damage} damage!")
            time.sleep(1.5)
            enemy.take_damage(damage)

            if random.random() < 0.3:
                enemy.stunned = True
                print("The enemy got stunned by the impact!! ")
                time.sleep(1.3)

            self.cooldown = 4

        elif self.player_class == "riftblade":
            print(f"You swing your blade 3 times, dealing multiple damage to the enemy!")
            time.sleep(1.5)
            for attack in range(3):
                enemy.take_damage(random.randint(2,5))

            self.cooldown = 3

        elif self.player_class == "haven scout":
            print(f"\nYou analyzed your enemy {enemy.name} carefully... predicting his next move...")
            time.sleep(1.5)
            self.dodging = True

            self.cooldown = 5

        elif self.player_class == "ironbound sentinel":
            heal = int(self.max_health * 0.15)
            self.health += heal

            if self.health > self.max_health:
                self.health = self.max_health

            print(f"{self.name} fortifies their defense! Restoring {heal} health!")
            time.sleep(1.5)

            self.cooldown = 4

        else:
            print(f"{self.special_ability} is on cooldown! You lost your turn.")
            time.sleep(1.1)

    def show_inventory(self):
        print("\n== [INVENTORY: SECURE CACHE ==")

        if not self.inventory:
            print("No stored supplies")
            time.sleep(0.6)
            return

        for item, amount in self.inventory.items():
            print(f"> {item} | x{amount}")

    def show_status(self):
        print(f"--[ {self.name} - {self.player_class.title()} | Level: {self.level} | SMK: {self.stormmarks} | Health: {self.health}/{self.max_health} | Attack: {self.attack} ]--")

