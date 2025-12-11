import time
from colorama import Style, Fore
from models import Location
from world_movement.molten_spill_movement import handle_jump_over, handle_wait
from game_modules.pause_menu import show_menu

reset = Style.RESET_ALL

def go_to_molten_spill(player):
    player.location = "The Molten Spill"
    print("\nAs you venture, you see a big, wide, fallen pipe spitting out very hot molten!")
    time.sleep(1)
    print(f"{player.name}: 'This is blocking my way... What should I do?'")

    return the_molten_spill.enter(player)

the_molten_spill = Location(
    "The Molten Spill",
    f"""\nThe Molten Spill, Your path is severed. 
    Before you flows a glowing river of molten metal, slow and luminous, poured fresh from a fractured overhead pipe.
    The crushing heat is immediate, and the thick, coppery scent of superheated ore chokes the air.
    You are forced to halt, the distant metal *CLANGING* of the Foundry echoing your frustration.
                 
    Area Signal Tower Coverage: [{Fore.RED + Style.BRIGHT}II - HIGH Danger{reset}]   
    """,
    {
        "1": ('Wait -> Step back and wait for the metal to cool (Slower but safer + 1 step)', handle_wait),
        "2": ('Jump Over -> Attempt to jump over the Hot Molten (Risky but faster + 5 steps if success)', handle_jump_over),
        "0": ('Pause Game', show_menu)
    }
)