import random
from colorama import Style, Fore

gauge = f"{Fore.RED + Style.BRIGHT}Gauge{Style.RESET_ALL}"

npc_dialogue = [
    f"{gauge}: I deal in millimeters and microns. Your survival depends on tolerances. Don't waste my measurements.",
    f"{gauge}: Max HP ain't just padding, kid. It's the maximum yield before catastrophic failure. Understand the spec.",
    f"{gauge}: This Annex only deals in grade-A salvage. If you want junk, go back to the Data Grave.",
    f"{gauge}: You look fragile. Every Scrapper thinks they're faster than the hit. You're not. Buy the armor.",
    f"{gauge}: The Foundry's heat warps metal, but it forges strength. My welds don't break.",
    f"{gauge}: Check your gait. Your armor is unbalanced. I can fix that stress point before it snaps.",
    f"{gauge}: They call it plating. I call it the acceptable margin of error between you and scrap.",
    f"{gauge}: I hate soft materials. I hate cheap alloys. If it ain't rated for heavy kinetic, it stays out of the shop.",
    f"{gauge}: Heard D-Corp sent a new wave of Sentinels toward the Perimeter. Time to upgrade your shoulder specs.",
    f"{gauge}: Don't worry about the cost. Worry about the crack in your sternum plating that ain't there yet.",
    f"{gauge}: My prices are fixed. Calculated based on material scarcity and the likelihood of your failure.",
    f"{gauge}: The best defense is redundancy. You got a primary shield and a secondary layer. Always.",
    f"{gauge}: That rattling noise? That's not the wind. That's a loose bolt. Fix it or pay the repair fee later.",
    f"{gauge}: You need armor that moves with you, not against you. Try this ferro-fluid liner.",
    f"{gauge}: I trust steel more than I trust most faces 'round here. And I only trust steel when I've checked the tensile strength myself."
]


def show_gauge_dialogue():
    print(random.choice(npc_dialogue))
    return