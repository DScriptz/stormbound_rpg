from colorama import Fore, Style, init
init(autoreset=True)

"""
    CLASS CHOICES

    Example:
        - Warrior | Attack 100 | Special Ability: Uproar
        - Gunslinger | Attack 80 | Special Ability: Frenzy
        
"""

class_stats = {
    "1": {
        "name": "Storm Warden",
        "health": 75, "max_health": 75,
        "attack": 11,
        "ability": f"{Fore.LIGHTBLUE_EX + Style.BRIGHT}Thunder Strike{Style.RESET_ALL}"
    },
    "2": {
        "name": "Flash Tracer",
        "health": 63,
        "max_health": 63,
        "attack": 13,
        "ability": f"{Fore.YELLOW + Style.BRIGHT}Blade Flurry{Style.RESET_ALL}"
    },
    "3": {
        "name": "Aethermancer",
        "health": 70,
        "max_health": 70,
        "attack": 12,
        "ability": f"{Fore.RED + Style.BRIGHT}Divine Blast{Style.RESET_ALL}"
    },
    "4": {
        "name": "Haven Scout",
        "health": 60,
        "max_health": 60,
        "attack": 15,
        "ability": f"{Fore.LIGHTMAGENTA_EX + Style.BRIGHT}Needle Threader{Style.RESET_ALL}"
    },
    "5": {
        "name": "Ironbound Sentinel",
        "health": 85,
        "max_health": 85,
        "attack": 9,
        "ability": f"{Style.BRIGHT}Iron Guard{Style.RESET_ALL}"
    },

    "6": {
        "name": "Zero-Pulser",
        "health": 78,
        "max_health": 78,
        "attack": 10,
        "ability": f"{Fore.CYAN + Style.BRIGHT}Static Field{Style.RESET_ALL}"
    },

    "7": {
        "name": "Rivet-Eye",
        "health": 65,
        "max_health": 65,
        "attack": 14,
        "ability": f"{Fore.YELLOW + Style.BRIGHT}Final Caliber{Style.RESET_ALL}"
    },
    "8": {
        "name": "Data Cultist",
        "health": 68,
        "max_health": 68,
        "attack": 10,
        "ability": f"{Fore.LIGHTGREEN_EX + Style.BRIGHT}Storm's Favor{Style.RESET_ALL}"
    },
    "9": {
        "name": "Echo Runner",
        "health": 58,
        "max_health": 62,
        "attack": 12,
        "ability": f"{Fore.WHITE + Style.BRIGHT}Dead Bolt{Style.RESET_ALL}"
    },
    "10": {
        "name": "Scrap Brawler",
        "health": 73,
        "max_health": 73,
        "attack": 11,

        "ability": f"{Fore.LIGHTRED_EX + Style.DIM}Scrap Shrapnel{Style.RESET_ALL}"
    },
    "dev": {
        "name": "dev",
        "health": 837,
        "max_health": 837,
        "attack": 999,
        "ability": f"{Style.DIM + Fore.RED}Domain Expansion: Barangay Tanod{Style.RESET_ALL}"
    }
}

def class_info():
    print("========================================= -CLASSES- =========================================")
    print(f"{Fore.LIGHTGREEN_EX}Tip: Forgot what a class's special ability does? Make sure to read the class overview!{Style.RESET_ALL}")

    for key, value in class_stats.items():
        print(f"\n[{key}]: {value['name']} |"
              f" Health: {value['health']}/{value['max_health']} |"
              f" Attack: {value['attack']} |"
              f" Special Ability: {value['ability']}")
    print("==============================================================================================")


