from colorama import Fore, Style, init
init(autoreset=True)

"""
    CLASS CHOICES

    Example:
        - Warrior | Attack 100 | Special Ability: Uproar
        - Gunslinger | Attack 80 | Special Ability: Frenzy
"""

class_stats = {
    "stormwarden": {"health": 75, "attack": 10, "ability": f"{Fore.LIGHTBLUE_EX + Style.BRIGHT}Thunder strike{Style.RESET_ALL}"},
    "riftblade": {"health": 63, "attack": 12, "ability": f"{Fore.YELLOW + Style.BRIGHT}Blade flurry{Style.RESET_ALL}"},
    "aethermancer": {"health": 70, "attack": 15, "ability": f"{Fore.RED + Style.BRIGHT}Lightning bolt{Style.RESET_ALL}"},
    "haven scout": {"health": 60, "attack": 13, "ability": f"{Fore.LIGHTMAGENTA_EX + Style.BRIGHT}Needle threader{Style.RESET_ALL}"},
    "ironbound sentinel": {"health": 85, "attack": 11, f"ability": f"{Style.BRIGHT}Iron guard{Style.RESET_ALL}"}
}

def class_info():
    for key, value in class_stats.items():
        print(f"- [{key}] | Health: {value['health']} | Attack: {value['attack']} | Special Ability: '{value['ability']}'".title())


