import time
from colorama import Fore, Style
from rpg.class_data import class_weapons

reset = Style.RESET_ALL
choices = class_weapons

def weapon_choices(player):
    player_class = player.player_class

    if player_class == "Storm Warden":
        choices.stormwarden_weapons()

    elif player_class == "Flash Tracer":
        choices.flash_tracer_weapons()

    elif player_class == "Aethermancer":
        choices.aethermancer_weapons()

    elif player_class == "Haven Scout":
        choices.haven_scout_weapons()

    elif player_class == "Ironbound Sentinel":
        choices.ironbound_sentinel_weapons()

    elif player_class == "Zero-Pulser":
        choices.zero_pulser_weapons()

    elif player_class == "Rivet-Eye":
        choices.rivet_eye_weapons()

    elif player_class == "Data Cultist":
        choices.data_cultist_weapons()

    elif player_class == "Echo Runner":
        choices.echo_runner_weapons()

    elif player_class == "Scrap Brawler":
        choices.scrape_brawler_weapons()

    else:
        print(f"{player.name}: 'I don't like any of these, I'll just fight with my {player.weapon}.'")
        time.sleep(0.7)

    return

def choose_weapon(player):
    print("\nThese are ideas of weapons you might want to wield if you can't think of any!")
    time.sleep(0.5)
    weapon_choices(player)

    weapon = input("\n>> ").strip()

    if not weapon:
        print(f"{player.name}: 'I don't like any of these, I'll just fight with my {player.weapon}.'")
        time.sleep(0.7)

    else:
        player.weapon = weapon
        print(f"{player.name}: 'Alright! I'm now wielding a {player.weapon}. This will do me good.'")
        time.sleep(0.6)

    return player

def main(player):
    """ DETERMINES THE PLAYER'S WEAPON WIELD. THIS IS JUST FOR ROLEPLAY PURPOSES """
    print("Before you pack up, you look at this chipped, ragged wooden table.")
    time.sleep(0.7)
    print(f"{player.name}: 'What weapon should I wield?'")
    time.sleep(0.8)
    print(f"{Fore.GREEN + Style.BRIGHT}NOTE: Wielding a weapon does NOT give added attack or buffs, it's just for Roleplaying! Enjoy!{reset}")
    print("\nType any weapon name or choose from the table (Feel free to use your imagination!):  ")
    choose_weapon(player)

    return player

