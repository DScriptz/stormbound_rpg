
""" IMPORTS """
import random
import time
from rpg.tools import audio_manager
from rpg.data.item_database import item_database
from colorama import Fore, Style, init
init(autoreset=True)

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
        self.inventory = {"Quick-Seal Strip": 2}
        self.stormmarks = 0
        self.special_ability = None
        self.dodging = False
        self.stunned = False
        self.active_bounty = None
        self.current_chapter = 0
        self.bounty_completed = 0

    """ 
        PLAYER'S STATS BEING SHOWN
    
        Example:
                Dwayne | Health: 100 | Attack: 50
                Gold: 20 | Level 5
                Inventory: {}
                
    """
    def introduce(self):
        print("=========[ PLAYER DATA ]=========")
        print(f"\n{self.name}, the {self.player_class.title()} | Health: {self.health}/{self.max_health}  | Attack: {self.attack}")
        print(f"\nStormmarks (SMK): {self.stormmarks} | Level: {self.level}")
        print("=================================\n")
        self.show_inventory()

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


        elif self.player_class == "Aethermancer":
            audio_manager.play_sound("aethermancer", volume=0.8)
            extra_damage = random.randint(3, 5)
            print(f"You unleash {self.special_ability}, strucking the enemy with arcane energy!")
            time.sleep(1.5)
            enemy.take_damage(self.attack + extra_damage)

            self.cooldown = 3

        elif self.player_class == "Stormwarden":
            audio_manager.play_sound("stormwarden", volume=0.9)
            damage = random.randint(10, 14)
            print(f"{self.name} unleashed Thunder Strike!! Dealing {damage} damage!")
            time.sleep(1.5)
            enemy.take_damage(damage)

            if random.random() < 0.3:
                enemy.stunned = True
                print("The enemy got stunned by the impact!! ")
                time.sleep(1.3)

            self.cooldown = 4

        elif self.player_class == "Riftblade":
            print(f"You swing your blade 3 times, dealing multiple damage to the enemy!")
            time.sleep(1.5)
            for attack in range(3):
                audio_manager.play_sound("fahh", volume=0.7)
                enemy.take_damage(random.randint(3,7))

            self.cooldown = 3

        elif self.player_class == "Haven Scout":
            print(f"\nYou analyzed your enemy {enemy.name} carefully... predicting his next move...")
            time.sleep(1.5)
            self.dodging = True

            self.cooldown = 5

        elif self.player_class == "Ironbound Sentinel":
            heal = int(self.max_health * 0.15)
            self.health += heal
            if self.health > self.max_health:
                self.health = self.max_health

            print(f"{self.name} fortifies their defense! Restoring {heal} health!")
            time.sleep(1.5)

            self.cooldown = 4

        elif self.player_class == "dev":
            audio_manager.play_sound("megumi_domain", volume=0.6)
            damage = self.attack + 837
            print(f"{enemy.name} got trapped in your Domain Expansion.")
            time.sleep(9.5)
            audio_manager.play_sound("fahh", volume=0.7)
            enemy.take_damage(damage)

            self.cooldown = 0

        else:
            print(f"{self.special_ability} is on cooldown! You lost your turn.")
            time.sleep(1.1)


    def show_inventory(self):
        print("\n== [INVENTORY: SECURE CACHE] ==")

        if not self.inventory:
            print("\nNo stored supplies")
            time.sleep(1)
            return
        for item, amount in self.inventory.items():
            print(f"\n> {item} | x{amount}")
        print("-----------------------------------")

        input("\nPress [Enter] To Close Inventory >> ")


    def remove_item(self, item_name, quantity=1):
        """ DEDUCTS THE  QUANTITY OF AN ITEM FROM INVENTORY IF IT REACHES 0 """

        if item_name not in self.inventory:
            return False

        current_count = self.inventory[item_name]

        if current_count < quantity:
            return False

        self.inventory[item_name] -= quantity

        if self.inventory[item_name] <= 0:
            del self.inventory[item_name]

        return True




    def show_status(self):
        print(f"\n                    --[ {self.name} - {self.player_class.title()} | Level: {self.level} | SMK: {self.stormmarks} | "
              f"Health: {self.health}/{self.max_health} | Attack: {self.attack} ]--")


    def level_up(self):
        self.level += 1
        print(f"\nYou leveled up! Level is now {self.level}")


    def use_item(self):

        if not self.inventory:
            print("Your Cache is empty!")
            time.sleep(1.1)
            return

        print(f"=== [{Fore.CYAN}ITEM USAGE MENU{Style.RESET_ALL} ===")

        item_menu = {}
        menu_index = 1

        for name, count in self.inventory.items():
            item_object = item_database.get(name)
            key = str(menu_index)
            item_menu[key] = name

            print(f"--> {Fore.YELLOW}[{key}]{Style.RESET_ALL}: {name} - Heals {item_object.heal} HP | x{count}")
            print("[X] - Exit Menu")
            menu_index += 1

        while True:
            choice = input(f"\n{self.name}: 'Hmm which item should I use?' >> ")

            if choice == "x": return

            if choice in item_menu:
                item_name = item_menu[choice]
                item_object = item_database[item_name]

                if item_object.use(self):
                    self.remove_item(item_name, 1)

                break

            print("Invalid selection")
            time.sleep(0.5)





