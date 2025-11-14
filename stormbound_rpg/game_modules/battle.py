
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
        damage = random.randint(self.enemy.attack - 3, self.enemy.attack + 3)
        print(f"\nThe {self.enemy.name} attacks {self.player.name} for {damage} damage!")
        time.sleep(1.1)
        self.player.take_damage(damage)

    def fight(self):

        while self.player.health > 0 and self.enemy.is_alive():

            print(f"\n-[Your Health: {self.player.health} | {self.enemy.name}'s Health: {self.enemy.health}]-")
            print("==============-BATTLE CHOICES-==============")
            print("\n[A] - Attack | [D] - Defend")
            print(f"[S] - Special Ability: '{self.player.special_ability}'")
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

            elif action == "s":
                if self.player.special_ability:
                    extra_damage = random.randint(8, 13)
                    print(f"You used {self.player.special_ability} for {extra_damage} damage!")
                    self.enemy.take_damage(self.player.attack + extra_damage)
                else:
                    print("You dont have a special ability! Turn lost.")

            else:
                print("\nYou stumbled and lost your turn!")
                time.sleep(1)

            """ ENEMY'S TURN """

            if self.enemy.is_alive():
                self.enemy.enemy_attack(self.player)
                time.sleep(1.3)


        if self.player.health <= 0:
            print("\nYou have been defeated...")
            choice = input("Try again?: ").lower().strip()

            if choice == "y" or "yes":


        else:
            print(f"\nYou defeated {self.enemy.name}!")



