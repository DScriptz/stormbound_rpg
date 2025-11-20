from colorama import Fore, Style, init
init(autoreset=True)

"""
    CLASS CHOICES

    Example:
        - Warrior | Attack 100 | Special Ability: Uproar
        - Gunslinger | Attack 80 | Special Ability: Frenzy
        
"""

class_stats = {
    "1": {"name": "Stormwarden", "health": 75, "max_health": 75, "attack": 11, "ability": f"{Fore.LIGHTBLUE_EX + Style.BRIGHT}Thunder Strike{Style.RESET_ALL}"},
    "2": {"name": "Riftblade", "health": 63, "max_health": 63, "attack": 13, "ability": f"{Fore.YELLOW + Style.BRIGHT}Blade Flurry{Style.RESET_ALL}"},
    "3": {"name": "Aethermancer", "health": 70, "max_health": 70, "attack": 12, "ability": f"{Fore.RED + Style.BRIGHT}Divine Blast{Style.RESET_ALL}"},
    "4": {"name": "Haven Scout", "health": 60, "max_health": 60, "attack": 15, "ability": f"{Fore.LIGHTMAGENTA_EX + Style.BRIGHT}Needle Threader{Style.RESET_ALL}"},
    "5": {"name": "Ironbound Sentinel", "health": 85, "max_health": 85, "attack": 9, "ability": f"{Style.BRIGHT}Iron Guard{Style.RESET_ALL}"}
}

def class_info():
    print("========================================= -CLASSES- =========================================")

    for key, value in class_stats.items():
        print(f"\n[{key}]: {value['name']} |"
              f" Health: {value['health']}/{value['max_health']} |"
              f" Attack: {value['attack']} |"
              f" Special Ability: {value['ability']}")

    print("==============================================================================================")


