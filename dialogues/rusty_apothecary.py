import random

from colorama import Fore, Style

npc_name = f"{Fore.LIGHTGREEN_EX}Silas 'Synth' Vane: {Style.RESET_ALL}"

silas_dialogue = [
    f"{npc_name}Yeah, yeah, what d'ya need? Don't ask where it came from, and don't tell me where it goes.",
    f"{npc_name}The air out there's thick enough to chew. Get your patch, pay your price, and get out.",
    f"{npc_name}I only deal in cash, no credit, no stories. What's the damage?",
    f"{npc_name}You got the marks or just the nerve? Don't waste my time, the Watch is close.",
    f"{npc_name}Everything on this shelf works, mostly. If it doesn't, you bought it, not me.",
    f"{npc_name}You look like you're about to fall apart. Fix that, or bleed somewhere else.",
    f"{npc_name}Don't breathe that heavy in here. I got enough synthetic stink as it is.",
    f"{npc_name}My inventory's low and the tariff's high. Whatever you see, that's the final cost."
]

def show_silas_dialogue():
    print(random.choice(silas_dialogue))