import random

from colorama import Fore, Style

tip = f"{Fore.GREEN + Style.BRIGHT}Tip:{Style.RESET_ALL}"
reset = Style.RESET_ALL

tips = [
    f"{tip} Buying in the shops found around your Faction\'s Base/Headquarters increases your Faction Respect!",
    f"{tip} Use your {Fore.RED}Healing{reset} Items in battle wisely! Especially when you're low HP, it's a matter of high risk OR high reward.",
    f"{tip} Make sure to read the Overviews at the beginning of the game, to get a grasp of the story of Stormbound...",
    f"{tip} Low on SMK? Earn some in thrilling battles or mini-games on some locations!",
    f"{tip} The other Classes are fun too! Replay the game to try them out!",
    f"{tip} Don't know where to go in a Location you went? Check out the {Style.BRIGHT}Current Location GPS{reset}",
    f"{tip} Check out the Stormbound Overview in your pause menu for the Ranks Info!",
    f"{tip} Found a bug? Make sure to put up an Issue request on the 'stormbound_rpg' Github Repository!"

]


def show_tips():
    print(random.choice(tips))