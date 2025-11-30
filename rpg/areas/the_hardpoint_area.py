import time
from rpg.tools.audio_manager import play_music
from rpg.models.location_data import Location
from rpg.areas.data_grave_area import go_to_data_grave
from rpg.world_movement.ironwind_outpost import go_to_ironwind_outpost





def go_to_the_hardpoint(player):
    play_music("the hardpoint", volume=0.7, loop=True)
    print("You walked into this somewhat abandoned, spacious open area...")
    time.sleep(1.5)
    the_hardpoint.enter(player)


the_hardpoint = Location(
    "The Hardpoint",
    """\nThe Hardpoint, covered by the 'Signal Towers'. Not a single place, but a chaotic zone. Roads are buried under dead machinery,
    and desperate life clings to skeletal skyscrapers. It's a loud, sprawling city of the desperate, 
    defined by the distant rumble of the Dead Zone. The best loot is here, and so is the worst danger.

    Area Signal Tower Coverage: [HIGH - No Danger] \n""",
    {
        "1": ('Explore the Data Grave', go_to_data_grave),
        "2": ('Radio Ironwinders and go back to Ironwind Outpost', go_to_ironwind_outpost)
    },
    True
)