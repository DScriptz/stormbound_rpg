import random

from colorama import Fore, Style

npc_name = f"{Fore.YELLOW}Rhys 'Rivet' Vance:{Style.RESET_ALL} "

rhys_dialogue = [
    f"{npc_name}'I don't sell scrap, I sell solutions. You break it, you bought it. Next.'",
    f"{npc_name}'Every piece here is tested. Tested on things that bite back.'",
    f"{npc_name}'Looking for bigger numbers? Gotta pay the bigger price. That's the way the Grid works.'",
    f"{npc_name}'Got some scavenged rounds on the back shelf. Discreet, and twice the punch. Interested?'",
    f"{npc_name}'That piece you got? Barely holds together. Trade it in, before it jams on you.'",
    f"{npc_name}'The tariff goes up every day. My prices are firm, and my patience is thin.'",
    f"{npc_name}'Don't wave that thing around. This isn't the Scrimmage Yard, it's a business.'",
    f"{npc_name}'What's your class? Don't buy a pipe-gun if you should be carrying a blade.'"
]

def show_rhys_dialogue():
    print(random.choice(rhys_dialogue))