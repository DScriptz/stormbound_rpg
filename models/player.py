
""" IMPORTS """
import random
import time
from tools import audio_manager
from data.item_database import item_database
from colorama import Fore, Style, init

reset = Style.RESET_ALL

"""
   THIS HANDLES THE PLAYER'S DATA

   This handles the name choosing of the player and the way they introduce themselves

"""

class Player:
    def __init__(self, player_name, player_class, health=50, max_health=50, attack=10, weapon="Barefist", location=None, battles_completed=0, rank="Scrap Initiate", faction_standing=0):
        self.name = player_name
        self.player_class = player_class
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.weapon = weapon
        self.cooldown = 0
        self.rank = rank
        self.inventory = {
            "Quick-Seal Strip": 3
        }
        self.stormmarks = 0
        self.special_ability = None
        self.dodging = False
        self.stunned = False
        self.active_bounty = None
        self.current_chapter = 1
        self.bounty_completed = 0
        self.faction = None
        self.location = location
        self.location_steps = 0
        self.battles_completed = battles_completed
        self.faction_standing = faction_standing

    """ 
        PLAYER'S STATS BEING SHOWN
    
        Example:
                Dwayne | Health: 100 | Attack: 50
                Gold: 20 | Level 5 | Faction: None
                Inventory: {}
                
    """
    def introduce(self):
        print("\n=========[ PLAYER DATA ]=========")
        print(f"\n{self.name}, the {self.player_class.title()} | Weapon: {self.weapon} | Health: {self.health}/{self.max_health} | Attack: {self.attack}")
        print(f"\nStormmarks (SMK): {self.stormmarks} | Rank: {self.rank} | Faction: '{self.faction}'")
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
            extra_damage = random.randint(6, 10)
            print(f"You unleash {self.special_ability}, striking the enemy with arcane energy!")
            time.sleep(1.5)
            enemy.take_damage(self.attack + extra_damage)

            self.cooldown = 3
            return

        elif self.player_class == "Storm Warden":
            stun_chance = 40
            chance = random.randint(1, 100)

            audio_manager.play_sound("stormwarden", volume=0.9)
            damage = random.randint(11, 15)
            print(f"{self.name} unleashed Thunder Strike!! Dealing {damage} damage!")
            time.sleep(1.5)
            enemy.take_damage(damage)

            if chance <= stun_chance:
                enemy.stunned = True
                print("The enemy got stunned by the impact!! ")
                time.sleep(1.3)

            self.cooldown = 4
            return

        elif self.player_class == "Flash Tracer":
            audio_manager.play_sound("unsheathe sword", volume=0.9)
            print(f"You swing your blade 3 times, dealing multiple damage to the enemy!")
            time.sleep(1.5)

            if self.battles_completed >= 11:
                for attack in range(3):
                    enemy.take_damage(random.randint(10,13))
                    sound_list = ['slash 1', 'slash 2', 'slash 3']
                    audio_manager.play_sound(sound_list[attack - 1],  volume=0.7)

            elif self.battles_completed >= 0:
                for attack in range (3):
                    enemy.take_damage(random.randint(5,8))
                    sound_list = ['slash 1', 'slash 2', 'slash 3']
                    audio_manager.play_sound(sound_list[attack - 1], volume=0.7)

            print("\nYou sheathe your sword back...")
            time.sleep(0.5)

            if self.battles_completed >= 11:
                self.cooldown = 5
            elif self.battles_completed >= 0:
                self.cooldown = 3

            return

        elif self.player_class == "Haven Scout":
            audio_manager.play_sound("haven scout", volume=0.9)
            print(f"\nYou analyzed your enemy {enemy.name} carefully... predicting his next move...")
            time.sleep(1.5)
            self.dodging = True

            self.cooldown = 5

            return

        elif self.player_class == "Ironbound Sentinel":
            heal = int(self.max_health * 0.15)
            self.health += heal
            if self.health > self.max_health:
                self.health = self.max_health

            print(f"{self.name} fortifies their defense! Restoring {heal} health!")
            time.sleep(1.5)

            self.cooldown = 4
            return

        elif self.player_class == "Zero-Pulser":
            debuff_value = 0.40
            audio_manager.play_sound("zero pulser 2", volume=1)
            print(f"You placed a {self.special_ability}! The {self.special_ability} deals minor damage, "
                  f"stealing power from {enemy.name}'s attacks!")
            time.sleep(1.5)

            damage = self.attack + random.randint(3, 4)
            enemy.take_damage(damage)

            enemy.is_weakened = True
            enemy.weakness_factor = debuff_value
            print(f"{enemy.name} is Weakened by the Static Field and will deal 40% less damage next turn.")
            time.sleep(1.3)

            self.cooldown = 6

        elif self.player_class == "Rivet-Eye":
            crit_damage = self.attack * 1.8

            print(f"\nYou aimed sharply at the enemy, loading your gun with the deadliest micro-bullet known to man...")
            audio_manager.play_sound("slinger gun", volume=1)
            time.sleep(1.6)
            input(f"\n[Enter] - {Fore.LIGHTYELLOW_EX}Shoot{Style.RESET_ALL} \n >> ")
            audio_manager.play_sound("slinger", volume=1)
            print(f"\n{Fore.RED + Style.BRIGHT}BANG! A CRITICAL SHOT!!{Style.RESET_ALL}")
            time.sleep(0.5)

            damage = int(crit_damage)

            enemy.take_damage(damage)

            self.cooldown = 4
            return

        elif self.player_class == "Data Cultist":
            sacrifice_amount = 20

            if self.stormmarks < sacrifice_amount:
                print(f"You lack the {sacrifice_amount} Stormmarks required for a {self.special_ability}!")
                time.sleep(1.5)
                return

            self.stormmarks -= sacrifice_amount

            bonus_damage = int(sacrifice_amount * 1.6)
            print(f"You sacrifice {sacrifice_amount} Stormmarks to unleash {self.special_ability}!")
            audio_manager.play_sound("data cultist", volume=0.8)
            time.sleep(1.5)

            enemy.take_damage(self.attack + bonus_damage)
            print(f"Dealt {bonus_damage} bonus damage!")

            self.cooldown = 3
            return

        elif self.player_class == "Echo Runner":
            audio_choice = ['teleport', 'teleport 2']
            audio = random.choice(audio_choice)
            audio_manager.play_sound(audio, volume=0.7)
            print(f"You unleashed {self.special_ability}, allowing you for a quick double tap!")
            audio_manager.play_sound(audio, volume=0.7)

            input("[Enter] - Attack  ")
            audio_manager.play_sound("attack", volume=0.8)
            damage1 =  self.attack + random.randint(1,3)
            enemy.take_damage(damage1)

            audio_manager.play_sound(audio, volume=0.7)
            input("[Enter] - Attack  ")
            audio_manager.play_sound("attack", volume=0.8)
            damage2 = self.attack + random.randint(1, 3)
            enemy.take_damage(damage2)

            print(f"Dealt {damage1 + damage2} damage in two quick strikes.")


            self.cooldown = 4
            return

        elif self.player_class == "Scrap Brawler":
            bleed_turns = 3
            bleed_damage_per_turn = 0

            if self.battles_completed >= 21:
                bleed_damage_per_turn = int(self.attack * 0.7)
                audio_manager.play_sound("scrap brawler", volume=0.8)
                print(f"{self.name} unleashes {self.special_ability}, leaving sharp scrap wounds on {enemy.name}!")
                time.sleep(1.5)


            elif self.battles_completed >= 11:
                bleed_damage_per_turn = int(self.attack * 0.5)
                audio_manager.play_sound("scrap brawler", volume=0.8)
                print(f"{self.name} unleashes {self.special_ability}, leaving sharp scrap wounds on {enemy.name}!")
                time.sleep(1.5)

            elif self.battles_completed >= 0:
                bleed_damage_per_turn = int(self.attack * 0.3)
                audio_manager.play_sound("scrap brawler", volume=0.8)
                print(f"{self.name} unleashes {self.special_ability}, leaving sharp scrap wounds on {enemy.name}!")
                time.sleep(1.5)

            if bleed_damage_per_turn > 0:
                if random.random() < 0.40:
                    enemy.is_bleeding = True
                    enemy.bleed_damage = bleed_damage_per_turn
                    enemy.bleed_turns = bleed_turns

                    audio_manager.play_sound("bleeding", volume=0.8)
                    print(f"\n{enemy.name} is Bleeding, taking {bleed_damage_per_turn} damage for {bleed_turns} turns.")
                    time.sleep(1.3)
                else:
                    print(f"\nThe scraps failed to puncture {enemy.name}!!")
                    time.sleep(1.3)

            enemy.take_damage(self.attack)

            self.cooldown = 5
            return

        elif self.player_class == "dev":
            audio_manager.play_sound("megumi_domain", volume=0.6)
            damage = self.attack + 837
            print(f"{enemy.name} got trapped in your Domain Expansion.")
            time.sleep(9.5)
            audio_manager.play_sound("fahh", volume=1)
            enemy.take_damage(damage)

            self.cooldown = 0
            return

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
        print(f"\n{Fore.YELLOW}{Style.BRIGHT} {self.name}{Style.RESET_ALL} - "
              f"> {Fore.LIGHTWHITE_EX + Style.DIM}{Style.BRIGHT}{self.player_class}{Style.RESET_ALL} <")

        print(f"{Fore.WHITE}{Style.DIM}------------------------------{Style.RESET_ALL}")

        print(f"{Fore.CYAN} Rank:{Style.RESET_ALL} {self.rank}")
        print(f"{Fore.GREEN} SMK:{Style.RESET_ALL} {Fore.GREEN}{self.stormmarks}{Style.RESET_ALL}")

        print(f"{Fore.RED} Health:{Style.RESET_ALL} "
              f"{Fore.RED}{Style.BRIGHT}{self.health}{Style.RESET_ALL} / "
              f"{Fore.RED}{Style.BRIGHT}{self.max_health}{Style.RESET_ALL}")

        print(f"{Fore.MAGENTA} Attack:{Style.RESET_ALL} {self.attack}")

        print(f"{Fore.BLUE} Weapon:{Style.RESET_ALL} {Fore.BLUE}'{self.weapon}'{Style.RESET_ALL}")

        print(f"{Fore.YELLOW} Faction:{Style.RESET_ALL} {Style.BRIGHT}{self.faction}{reset}")

        print(f"{Fore.CYAN} Current Chapter:{Style.RESET_ALL} {self.current_chapter}")
        print(f"{Fore.MAGENTA} Battles:{Style.RESET_ALL} {self.battles_completed}")
        print(f"{Fore.BLACK + Style.BRIGHT} Location:{Style.RESET_ALL} {Fore.LIGHTBLACK_EX+Style.BRIGHT}{self.location}{Style.RESET_ALL}")

        print(f"{Fore.WHITE}{Style.DIM}------------------------------{Style.RESET_ALL}\n")

        return

    def use_item(self):

        if not self.inventory:
            print("Your Cache is empty!")
            time.sleep(1.1)
            return

        print(f"=== [{Fore.CYAN}INVENTORY: SECURE CACHE{Style.RESET_ALL} ===")

        item_menu = {}
        menu_index = 1

        for name, count in self.inventory.items():
            item_object = item_database.get(name)

            if not item_object:
                continue

            if item_object.heal > 0 or item_object.damage > 0 or item_object.armor > 0:
                key = str(menu_index)
                item_menu[key] = name

                display_text = ""
                if item_object.heal > 0:
                    display_text += f"Heals {item_object.heal} HP"

                if item_object.damage > 0:
                    if display_text:
                        display_text += " | "
                    display_text += f"Buffs +{item_object.damage} Total Attack"

                if item_object.armor > 0:
                    if display_text:
                        display_text += " | "
                    display_text += f"Increases Max HP +{item_object.armor} Total HP"

                print(f"--> {Fore.YELLOW}[{key}]{Style.RESET_ALL}: {name} ({display_text}) | x{count}")
                menu_index += 1

        print("\n--> [X] - Exit Menu")

        if not item_menu:
            print("You have no usable items in your inventory.")
            time.sleep(1)
            return

        while True:
            choice = input(f"\n{self.name}: 'Hmm which item should I use?' >> ")

            if choice == "x":
                return

            if choice in item_menu:
                item_name = item_menu[choice]
                item_object = item_database[item_name]

                if item_object.use(self):
                    self.remove_item(item_name, 1)

                break
            else:
                print("Invalid selection")
                time.sleep(0.5)