""" IMPORTS """
from colorama import Fore, Style, init
init(autoreset=True)

import random
import time

""" THIS HANDLES THE GAME'S BATTLE MECHANIC """


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def player_attack(self):
        damage = random.randint(self.player.attack - 5, self.player.attack + 2)
        print(f"\nYou attack {self.enemy.name} for {damage} damage! ")
        time.sleep(1.2)
        self.enemy.take_damage(damage)

    def enemy_attack(self):
        damage = random.randint(self.enemy.attack - 3, self.enemy.attack + 2)
        print(f"\nThe {self.enemy.name} attacks {self.player.name} for {damage} damage!")
        time.sleep(1.1)
        self.player.take_damage(damage)

    def fight(self):
        while True:
            self.player.health = self.player.max_health
            self.enemy.health = self.enemy.max_health
            while self.player.health > 0 and self.enemy.is_alive():

                print(f"\n-[Your Health: {self.player.health}/{self.player.max_health} | {self.enemy.name}'s Health: {self.enemy.health}/{self.enemy.max_health}]-")
                print("==============-BATTLE CHOICES-==============")
                print(f"\n[A] - {Fore.RED + Style.DIM}Attack{Style.RESET_ALL} | [D] - {Fore.BLUE + Style.BRIGHT}Defend{Style.RESET_ALL}")
                print(f"[S] - {Fore.LIGHTGREEN_EX + Style.BRIGHT}Special Ability{Style.RESET_ALL}: '{self.player.special_ability}'")
                action = input("\n>> ").lower().strip()

                """ THIS HANDLES HOW THE BATTLES GOES """

                if action == "a":
                    self.player.player_attack(self.enemy)
                    time.sleep(1.3)

                elif action == "d":
                    damage = random.randint(self.enemy.attack - 3, self.enemy.attack + 3) // 2
                    print(f"{self.enemy.name} attacks you for {damage} damage!")
                    time.sleep(1.5)
                    self.player.take_damage(damage)
                    continue

                elif action == "s":


                else:
                    print("\nYou stumbled and lost your turn!")
                    time.sleep(1)

                """ ENEMY'S TURN """

                if self.enemy.is_alive():
                    self.enemy.enemy_attack(self.player)
                    time.sleep(1.3)

            """ PLAYER GETS DEFEATED BUT HAS A CHOICE TO RESTART """
            if self.player.health <= 0:
                print("\nYou have been defeated...")
                choice = input("Try again?: ").lower().strip()

                if choice =="y" or choice == "yes":
                    continue
                else:
                    return
            else:
                print(f"\nYou defeated the {self.enemy.name}!")
                time.sleep(1.1)
                return



