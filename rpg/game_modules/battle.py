""" IMPORTS """
import random
import time
import sys
from colorama import Fore, Style, init
from rpg.tools import audio_manager

init(autoreset=True)

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

    """ MAIN BATTLE LOOP OF THE GAME """

    def fight(self, player):
        while True:
            """ THIS ENSURES THAT IF THE GAME RESTARTS THE PLAYER AND ENEMY'S HEALTH GOES BACK TO THEIR MAX HEALTH """
            self.player.health = self.player.max_health
            self.enemy.health = self.enemy.max_health
            while self.player.health > 0 and self.enemy.is_alive():
                """ PLAYER'S TURN """
                print(f"\n    --[{self.player.name}'s Health: {Fore.LIGHTRED_EX}"
                      f"{self.player.health}/{self.player.max_health}"
                      f"{Style.RESET_ALL} "
                      f"| {self.enemy.name}'s Health: {Fore.LIGHTRED_EX}"
                      f"{self.enemy.health}/{self.enemy.max_health}"
                      f"{Style.RESET_ALL}]-")

                print("    [==============-BATTLE CHOICES-==============]")
                print(f"\n   [A] - {Fore.RED + Style.DIM}Attack{Style.RESET_ALL} |  [D] - {Fore.BLUE + Style.BRIGHT}Defend{Style.RESET_ALL}")
                print(f"   [U] - {Fore.GREEN + Style.BRIGHT}Use an Item{Style.RESET_ALL} |  [R] - {Style.BRIGHT + Fore.LIGHTBLACK_EX}Run{Style.RESET_ALL} (-20 Stormmarks)")

                """
                    THIS HANDLES THE COOLDOWN OF THE PLAYER'S ABILITY, IF IT'S IN COOLDOWN, DONT SHOW THE OPTION: 
                        '[S] - Special Ability'  
                """

                if self.player.cooldown == 0:
                    print(f"   [S] - {Fore.YELLOW + Style.BRIGHT}Special Ability{Style.RESET_ALL}: '{self.player.special_ability}' |  [I] - Inventory")

                else:
                    print(f"   [S] - (Cooldown : {self.player.cooldown}) |  [I] - Inventory")

                if player.stunned:
                    print(f"{player.name} got stunned and can't move!!!")
                    time.sleep(1.2)
                    player.stunned = False
                    continue

                action = input("\n>> ").lower().strip()

                """ 
                    THIS HANDLES THE PLAYER'S CHOICES WITHIN THE GAME
                    
                    Example:
                                     -[Your Health: 75/75 | Ravager Wolf's Health: 55/55]-
                                ==============-BATTLE CHOICES-==============

                                [A] - Attack | [D] - Defend
                                [S] - Special Ability: 'Thunder strike'
                                            
                                >> a
                                            
                                You attacked the enemy for 10 damage!
                                
                """

                if action == "a":
                    audio_manager.play_sound("attack", volume=0.8)
                    self.player.player_attack(self.enemy)
                    time.sleep(1.3)

                elif action == "d":
                    print(f"{self.player.name} defends themselves! Reducing {self.enemy.name}'s attack!")
                    damage = random.randint(self.enemy.attack - 3, self.enemy.attack + 3) // 2
                    print(f"{self.enemy.name} attacks you for {damage} damage!")
                    time.sleep(1.5)
                    self.player.take_damage(damage)

                    if self.player.cooldown > 0:
                        self.player.cooldown -= 1
                    continue

                elif action == "u":
                    player.use_item()

                elif action == "r":
                    audio_manager.play_sound("run", volume=0.9)
                    print("You ran away like a coward! Dropping some of your SMK along the way...")
                    time.sleep(1.3)
                    if player.stormmarks <= 0:
                        player.stormmarks = 0
                    else:
                        player.stormmarks -= 20
                    break
                elif action == "i":
                    player.show_inventory()
                    continue

                elif action == "s":
                    self.player.use_ability(self.enemy)
                else:
                    print("\nYou stumbled and lost your turn!")
                    time.sleep(1)

                """ ENEMY'S TURN """

                if self.enemy.is_alive():
                    if self.enemy.is_bleeding:
                        print(f"{self.enemy.name} bleeds from {self.player.special_ability} for {self.enemy.bleed_damage} damage!")
                        self.enemy.take_damage(self.enemy.bleed_damage)

                        self.enemy.bleed_turns -= 1

                        if self.enemy.bleed_turns <= 0:
                            self.enemy.is_bleeding = False
                            self.enemy.bleed_damage = 0
                            print(f"The bleeding on {self.enemy.name} has stopped.")
                        time.sleep(1.0)

                    if not self.enemy.is_alive():
                        return None

                    if self.enemy.stunned:
                        print(f"The enemy is stunned and cannot move! {self.enemy.name}'s turn is lost!")
                        self.enemy.stunned = False


                    else:

                        raw_damage = self.enemy.calculate_damage()

                        if self.enemy.is_weakened:
                            final_damage = int(raw_damage * (1.0 - self.enemy.weakness_factor))

                            print(f"[{self.enemy.name}]'s attack is weakened! Deals {final_damage} damage!")

                            self.enemy.is_weakened = False
                            self.enemy.weakness_factor = 0.0

                        else:
                            final_damage = raw_damage
                            print(f"\n{self.enemy.name} attacks you for {final_damage} damage!")

                        self.player.take_damage(final_damage)
                        time.sleep(1.3)


                """ 
                    IF PLAYER USES THIER ABILITY, 
                    
                    THIS MAKES IT SO THAT THE TIMER OF THEIR ABILITY COOLDOWN E.G: 3 TURNS, GETS DEDUCTED
                    
                 """

                if self.player.cooldown > 0:
                    self.player.cooldown -= 1

            """ PLAYER GETS DEFEATED BUT HAS A CHOICE TO RESTART """
            if self.player.health <= 0:
                print("\nYou have been defeated...")
                choice = input("Try again? (Y/N): ").lower().strip()

                if choice =="y" or choice == "yes":
                    continue
                else:
                    print("Your fate leads to death...")
                    sys.exit()


            else:
                print(f"\nYou defeated the {self.enemy.name}!")
                audio_manager.play_sound("victory", volume=1.3)
                time.sleep(1.1)
                self.player.cooldown = 0
                self.player.battles_completed += 1
                return player



