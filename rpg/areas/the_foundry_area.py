import time
from colorama import Style, Fore, init
from rpg.models import Location
from rpg.world_movement.the_foundry_movement import handle_movement_forward, handle_movement_right, handle_movement_left
from rpg.game_modules.map import show_map, show_location_details


init(autoreset=True)

reset = Style.RESET_ALL


def run_back_to_hardpoint_from_foundry(player):
    from .the_hardpoint_area import go_to_the_hardpoint
    print("You ran as fast as you can back to the Hardpoint...")
    time.sleep(1.2)

    player.location_steps = 0

    return go_to_the_hardpoint(player)


def go_to_the_foundry(player):

    if player.battles_completed >= 11:
        print("You walked on the right, towards the bustling noise of clanking metals...")
        time.sleep(1.3)
        print("This place is what the people called, 'The Foundry'...")
        time.sleep(1.1)
        player.location = "The Foundry"

        return the_foundry.enter(player)

    elif player.battles_completed <= 10:
        print(f"{player.name}: 'I'm not experienced enough to wander around this area...'")
        time.sleep(1)
        return None

    return True





the_foundry = Location(
    "The Foundry",
    f"""\nThe Foundry. A colossal, decaying structure of soot-blackened iron, perpetually choked by thick, acid-tinged smog.
    The main danger is extreme heat and obsolete automation. Massive, unchecked production machinery still grinds and pours
    molten slag, treating everything including you as raw material. The air vibrates with the deafening, rhythmic CLANG of dormant
    hammers and steam vents.
    
    Area Signal Tower Coverage: [{Fore.RED + Style.BRIGHT}II - HIGH Danger{reset}]
    """,
    {
        "1": ('Run Forward (High risk but faster)', handle_movement_forward),
        "2": ('Walk to the Right (Low risk but slower, may run into dead-ends...)', handle_movement_right),
        "3": ('Walk to the Left (Low risk but slower, may run into dead-ends...)', handle_movement_left),
        "4": ('Run back to the Hardpoint',  run_back_to_hardpoint_from_foundry),
        "5": ('Show Current Location GPS', show_location_details),
        "M": ('Show Map', show_map)
     }

)