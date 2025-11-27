from colorama import Fore, Style


CLASS_OVERVIEW_TEXT = f"""
================================================================
                            -[CHOOSE YOUR PATH: SURVIVOR CLASSES]- 
================================================================
NOTE: {Fore.LIGHTGREEN_EX}Pick what you'll enjoy. Attack/Health can be increased by buying certain items from certain shop{Style.RESET_ALL}.

[1] - Stormwarden  (HP: 75 / ATK: 11)
  > Role: Balanced Fighter & Utility. An average survivor adapted to common threats.
  > Ability: {Fore.LIGHTBLUE_EX + Style.BRIGHT}Thunder Strike{Style.RESET_ALL} - (A reliable, mid-damage attack that has a 30% chance of stunning the enemy.)

[2] - Riftblade (HP: 63 / ATK: 13)
  > Role: Agile Damage Dealer. Focuses on speed and quick, precise hits.
  > Ability: {Fore.YELLOW + Style.BRIGHT}Blade Flurry{Style.RESET_ALL} - (High-risk, high-reward burst damage.)

[3] - Aethermancer (HP: 70 / ATK: 12)
  > Role: Skill & Support. Utilizes specialized knowledge for effects or minor healing.
  > Ability: {Fore.RED + Style.BRIGHT}Divine Blast{Style.RESET_ALL} - (A magical damage attack that electrocutes your foe.)

[4] - Haven Scout (HP: 60 / ATK: 15)
  > Role: Glass Cannon. Very high damage output but low survivability.
  > Ability: {Fore.LIGHTMAGENTA_EX + Style.BRIGHT}Needle Threader{Style.RESET_ALL} - (Anticipate your enemy's next move and dodge accordingly.)

[5] - Ironbound Sentinel (HP: 85 / ATK: 9)
  > Role: The Defender. Highest HP and best defense, sacrificing attack power.
  > Ability: {Style.BRIGHT}Iron Guard{Style.RESET_ALL} - (A powerful heal that can shock your enemies.)

--- NEW CLASSES as of v1.02.01 ---

[6] - E-Warden (HP: 78 / ATK: 10)
  > Role: The Controller. Focuses on enemy debuffs and battlefield control.
  > Ability: {Fore.CYAN + Style.BRIGHT}Power Siphon{Style.RESET_ALL} - (Siphons enemy power to reduce their next attack damage by 40%.)

[7] - Slinger (HP: 65 / ATK: 14)
  > Role: The Marksman. Prioritizes precision and devastating single-shot damage.
  > Ability: {Fore.YELLOW + Style.BRIGHT}Deadeye{Style.RESET_ALL} - (Aim precisely at the enemy and shoot them for a guaranteed crit)

[8] - Data Cultist (HP: 68 / ATK: 10)
  > Role: The Economic Broker. Uses high risk to gain high-value rewards.
  > Ability: {Fore.MAGENTA + Style.BRIGHT}Marked Sacrifice{Style.RESET_ALL} - (Corrupt a network Data and sacrifice 20 SMK for a bonus damage.)

[9] - Echo Runner (HP: 62 / ATK: 12)
  > Role: The Swift Striker. Uses speed and agility for rapid engagement.
  > Ability: {Fore.WHITE + Style.BRIGHT}Reposition Strike{Style.RESET_ALL} - (Use your speed to your advantage and attack the enemy in quick succession for 2 times in a turn.  )

[10] - Scrap Brawler (HP: 73 / ATK: 11)
  > Role: Damage Over Time Specialist. Wears down opponents with persistent injuries.
  > Ability: {Fore.RED + Style.BRIGHT}Scrap Shrapnel{Style.RESET_ALL} - (Inflicts Bleeding damage over 3 turns after the initial attack.)

================================================================
"""

def show_class_overview():
    print(CLASS_OVERVIEW_TEXT)