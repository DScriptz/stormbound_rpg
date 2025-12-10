import time
from colorama import Style, Fore
from tools.audio_manager import play_music
from models.location_data import Location
from areas.data_grave_area import go_to_data_grave
from areas.the_foundry_area import go_to_the_foundry
from world_movement.ironwind_outpost import go_to_ironwind_outpost
from game_modules.map import show_map, show_location_details
from game_modules.pause_menu import show_menu


reset = Style.RESET_ALL


def go_to_the_hardpoint(player):
    player.location = "The Hardpoint"
    play_music("the hardpoint", volume=0.7, loop=True)
    print("You walked into this somewhat abandoned, spacious open area...")
    time.sleep(1.5)
    the_hardpoint.enter(player)


the_hardpoint = Location(
    "The Hardpoint",
    f"""\nThe Hardpoint, covered by the 'Signal Towers'. Not a single place, but a chaotic zone. Roads are buried under dead machinery,
    and desperate life clings to skeletal skyscrapers. It's a loud, sprawling city of the desperate, 
    defined by the distant rumble of the Dead Zone. Many other areas can be accessed through here.

    Area Signal Tower Coverage: [{Fore.GREEN}IIIII - SAFE{reset}] \n""",
    {
        "1": ('Explore The Data Grave (Recommended Rank: "Green Tag [2 Battles] or Higher >>")', go_to_data_grave),
        "2": ('Radio Ironwinders and go back to Ironwind Outpost', go_to_ironwind_outpost),
        "3": ('Explore The Foundry (Recommended Rank: "Fringe Rat [6 Battles] or Higher >>" & equipments upgraded.)', go_to_the_foundry),
        "5": ('Show Current Location GPS', show_location_details),
        "0": ('Pause Game', show_menu),
        "M": ('Use Map', show_map)
    },
    True
)