from colorama import Fore, Style


def get_rank(player):
    battles = player.battles_completed

    if battles >= 320:
        return f"{Fore.LIGHTWHITE_EX + Style.DIM}Deranged Conqueror{Style.RESET_ALL}"

    elif battles >= 220:
        return f"{Fore.YELLOW + Style.BRIGHT}The Hardpoint Legend{Style.RESET_ALL}"

    elif battles >= 101:
        return f"{Fore.MAGENTA + Style.BRIGHT}Stormbound Master{Style.RESET_ALL}"

    elif battles >= 81:
        return f"{Fore.CYAN}Circuit Breaker{Style.RESET_ALL}"

    elif battles >= 68:
        return f"{Fore.LIGHTBLUE_EX}Velocity Pilot{Style.RESET_ALL}"

    elif battles >= 53:
        return f"{Fore.LIGHTBLACK_EX + Style.BRIGHT}Ironclad Runner{Style.RESET_ALL}"  # Bright Black/Dark Gray

    elif battles >= 43:
        return f"{Fore.RED}Scrap Butcher{Style.RESET_ALL}"

    elif battles >= 35:
        return f"{Fore.YELLOW}Data Cipher{Style.RESET_ALL}"

    elif battles >= 21:
        return f"{Fore.GREEN}Junk Runner{Style.RESET_ALL}"

    elif battles >= 11:
        return f"{Fore.WHITE}Drone Hunter{Style.RESET_ALL}"

    elif battles >= 6:
        return f"{Fore.LIGHTBLACK_EX}Fringe Rat{Style.RESET_ALL}"

    elif battles >= 3:
        return f"{Fore.LIGHTYELLOW_EX + Style.DIM}Copper Grunt{Style.RESET_ALL}"

    elif battles >= 1:
        return f"{Fore.GREEN + Style.DIM}Green Tag{Style.RESET_ALL}"


    else:
        return f"{Fore.LIGHTBLACK_EX + Style.DIM}Scrap Initiate{Style.RESET_ALL}"


