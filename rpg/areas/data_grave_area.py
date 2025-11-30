import time
from rpg.tools.audio_manager import play_music
from rpg.models.location_data import Location
from rpg.world_movement.data_grave_movement import (
    handle_data_grave_movement_right,
    handle_data_grave_movement_forward, handle_data_grave_movement_left)


def run_back_to_hardpoint_from_grave(player):
    """Handles the transition from Data Grave back to the Hardpoint menu."""
    from .the_hardpoint_area import go_to_the_hardpoint

    print("\nYou scramble out of the wreckage, following the main utility line back to The Hardpoint.")
    player.location_steps = 0
    return go_to_the_hardpoint(player)


def rest(player):
    print("You found a place to rest for a while...")
    time.sleep(1.2)

    if player.health >= player.max_health:
        player.health = player.max_health
    else:
        player.health += 30

    print("You rested well and gained back +30 HP")
    time.sleep(0.6)


data_grave = Location(

    "The Data Grave",
    """\nThe Data Grave. A massive, sprawling landfill where every scrap has been scavenged a hundred times.
     The main danger is competition. Rival Scrapper crews patrol the perimeter and have rigged rudimentary,
     physical traps to protect their claims. The air echoes with the desperate clang of metal.

     You step into this area not knowing what's out there...


    Area Signal Tower Coverage: [LOW - Medium Danger] \n""",
    {
        "1": ('Run Forward (High risk but faster)', handle_data_grave_movement_forward),
        "2": ('Move to the Right (Low risk but slower, may run into dead-ends...)', handle_data_grave_movement_right),
        "3": ('Move to the Left (Low risk but slower, may run into dead-ends...)', handle_data_grave_movement_left),
        "4": ('Run back to the Hardpoint',  run_back_to_hardpoint_from_grave),
        "5": ('Rest +30 Health', rest)
    },
    False
)

def go_to_data_grave(player):
    player.location = "Data Grave"
    play_music("open world", volume=0.7, loop=True)
    print("You walked forward, to the Data Grave...")
    return data_grave.enter(player)