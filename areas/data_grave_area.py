import random
import time

from colorama import Fore, Style

from game_modules.map import show_map, show_location_details
from game_modules.pause_menu import show_menu
from models.location_data import Location
from tools.audio_manager import play_music
from world_movement.data_grave_movement import (
    handle_data_grave_movement_right,
    handle_data_grave_movement_forward, handle_data_grave_movement_left, handle_player_ambushed)

reset = Style.RESET_ALL

play_music("open world", volume=0.7, loop=True)

def run_back_to_hardpoint_from_grave(player):
    """Handles the transition from Data Grave back to the Hardpoint menu."""
    from .the_hardpoint_area import go_to_the_hardpoint

    print("\nYou scramble out of the wreckage, following the main utility line back to The Hardpoint.")
    player.location = "The Hardpoint"
    player.location_steps = 0
    return go_to_the_hardpoint(player)


def rest(player):
    rest_heal = 0
    if random.random() < 0.30:
        print("While finding a place to rest, an enemy ambushed you!!")
        handle_player_ambushed(player)

        return player
    else:
        print("You found a place to rest for a while...")
        time.sleep(1.2)

        if player.health >= player.max_health:
            print("You rest well, but you're already at full health!")
            player.health = player.max_health
        else:
            rest_heal = random.randint(30, 35)
            player.health += rest_heal
            if player.health >= player.max_health:
                player.health = player.max_health

        print(f"You rested well and gained back +{rest_heal} HP")
        time.sleep(0.6)

        return player


data_grave = Location(

    "The Data Grave",
    f"""\nThe Data Grave. A massive, sprawling landfill where every scrap has been scavenged a hundred times.
     The main danger is competition. Rival Scrapper crews patrol the perimeter and have rigged rudimentary,
     physical traps to protect their claims. The air echoes with the desperate clang of metal.

     You step into this area not knowing what's out there...


    Area Signal Tower Coverage: [{Fore.LIGHTYELLOW_EX}III - MEDIUM Danger{reset}]
    
{Fore.GREEN}Tip: Always check Current Location Info for guidance on a possible step(s) requirement for exploring.{reset}
""",
    {
        "1": ('Run Forward (High risk but faster)', handle_data_grave_movement_forward),
        "2": ('Move to the Right (Low risk but slower, may run into dead-ends...)', handle_data_grave_movement_right),
        "3": ('Move to the Left (Low risk but slower, may run into dead-ends...)', handle_data_grave_movement_left),
        "4": ('Run back to the Hardpoint',  run_back_to_hardpoint_from_grave),
        "5": ('Show Current Location GPS', show_location_details),
        "6": ('Find a place to rest (Heals HP)', rest),
        "0": ('Pause Game', show_menu),
        "M": ('Use Map', show_map)
    },
    False
)

def go_to_data_grave(player):
    player.location = "The Data Grave"
    play_music("open world", volume=0.7, loop=True)
    print("You walked forward, to the Data Grave...")
    return data_grave.enter(player)