""" IMPORTS """
import random
import time
import sys
from rpg.game_modules.loot_handler import handle_loot
from colorama import Fore, Style, init
from rpg.tools import audio_manager
from rpg.game_modules.player_ranks_up import check_rank

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

    def process_enemy_attack(self):
        """
        Calculates enemy damage, applies dodge/weakness factors,
        applies damage to the player, and resets the player's dodge state.
        """

        # 1. Check for Dodge State (must be the first check)
        if self.player.dodging:
            damage = 0
            print(f"\n{self.enemy.name} attacks, but {self.player.name} swiftly {Fore.GREEN}DODGES{Style.RESET_ALL}!")

        else:
            # 2. Calculate Damage with Weakness
            raw_damage = self.enemy.calculate_damage()

            if self.enemy.is_weakened:
                final_damage = int(raw_damage * (1.0 - self.enemy.weakness_factor))
                print(f"[{self.enemy.name}]'s attack is weakened! Deals {final_damage} damage!")
                self.enemy.is_weakened = False
                self.enemy.weakness_factor = 0.0
            else:
                final_damage = raw_damage
                audio_manager.play_sound("player hit", volume=0.8)
                print(f"\n{self.enemy.name} attacks you for {final_damage} damage!")

            damage = final_damage

        # 3. Apply Damage and Reset Dodge State
        self.player.take_damage(damage)
        time.sleep(1.3)

        # 4. Reset dodge state *only* after the attack is processed
        if self.player.dodging:
            self.player.dodging = False

        return

    """ MAIN BATTLE LOOP OF THE GAME """


    def fight(self, player, enemy):
        player_run = False

        self.enemy.health = enemy.max_health

        while True:
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
                    from rpg.class_data.class_attack_sound import attack_sound
                    attack_sound(player)
                    self.player.player_attack(self.enemy)
                    time.sleep(1.3)

                elif action == "d":
                    audio_manager.play_sound("block attack", volume=0.9)
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
                    player_run = True
                    audio_manager.play_sound("run", volume=0.9)
                    print("You ran away like a coward! Dropping some of your SMK along the way...")
                    time.sleep(1.3)

                    if player.stormmarks <= 0:
                        player.stormmarks = 0

                    elif player.location_steps <= 0:
                        player.location_steps = 0

                    else:
                        player.stormmarks -= 20
                        player.location_steps -= 1
                    break
                elif action == "i":
                    player.show_inventory()
                    continue

                elif action == "s":
                    player.use_ability(enemy)
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
                        self.process_enemy_attack()

                """ 
                    IF PLAYER USES THIER ABILITY, 
                    
                    THIS MAKES IT SO THAT THE TIMER OF THEIR ABILITY COOLDOWN E.G: 3 TURNS, GETS DEDUCTED
                    
                 """

                if self.player.cooldown > 0:
                    self.player.cooldown -= 1

            """ PLAYER GETS DEFEATED BUT HAS A CHOICE TO RESTART """
            if self.player.health <= 0:
                print("\nYou have been defeated...")

                choice = input("\nTry again? (Y/N): ").lower().strip()

                if choice =="y" or choice == "yes":
                    """ THIS ENSURES THAT IF THE GAME RESTARTS THE PLAYER AND ENEMY'S HEALTH GOES BACK TO THEIR MAX HEALTH """
                    self.player.health = self.player.max_health
                    self.enemy.health = self.enemy.max_health
                    continue
                else:
                    print("Your fate leads to death...")
                    sys.exit()
            else:
                if not player_run:
                    print(f"\nYou defeated the {self.enemy.name}!")
                    audio_manager.play_sound("victory", volume=1.3)
                    time.sleep(1.1)
                    handle_loot(player, enemy)

                    self.player.cooldown = 0
                    self.player.battles_completed += 1
                    check_rank(player)
                    return player
                else:
                    print("\nYou earned nothing for running away from a battle!")
                    time.sleep(1.1)
                    self.player.cooldown = 0
                    return player





