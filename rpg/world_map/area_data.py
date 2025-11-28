import time
from rpg.models.location_data import Location
from rpg.world_map.data_grave_movement import handle_data_grave_movement_forward
from rpg.tools.audio_manager import music_stop, music_fadeout, play_music
""" THESE HANDLES THE FUNCTIONS FOR EACH LOCATION """

def go_to_data_grave(player):
    player.location = "Data Grave"
    play_music("open world", volume=0.7, loop=True)
    print("You walked forward, to the Data Grave...")
    data_grave.enter(player)
    return True

def go_to_the_hardpoint(player):
    play_music("the hardpoint", volume=0.7, loop=True)
    print("You walked into this somewhat abandoned, spacious open area...")
    time.sleep(1.5)
    the_hardpoint.enter(player)

def go_to_ironwind_outpost(player):
    from rpg.chapters.chapter4 import return_to_ironwind_outpost

    print("\nYou ran to the muddy, dirty road and picked up your radio, signaling the Ironwinder Guard for transport...")
    time.sleep(1.4)
    music_fadeout(2000)
    music_stop()
    print("Loading area...")
    time.sleep(1.5)
    return_to_ironwind_outpost(player)


""" THIS DEFINES THE LOCATIONS FUNCTIONS """

the_hardpoint = Location(
    "The Hardpoint",
    """\nThe Hardpoint, covered by the 'Signal Towers'. Not a single place, but a chaotic zone. Roads are buried under dead machinery, "
    "and desperate life clings to skeletal skyscrapers. It's a loud, sprawling city of the desperate, "
    "defined by the distant rumble of the Dead Zone. The best loot is here, and so is the worst danger.
    
    Area Signal Tower Coverage: [HIGH - No Danger] \n""",
    {
        "1": ('Explore the Data Grave', go_to_data_grave),
        "2": ('Radio Ironwinders and go back to Ironwind Outpost', go_to_ironwind_outpost)
    },
    True
)

data_grave = Location(
    "The Data Grave",
    """\nThe Data Grave. A massive, sprawling landfill where every scrap has been scavenged a hundred times.
     The main danger is competition. Rival Scrapper crews patrol the perimeter and have rigged rudimentary,
     physical traps to protect their claims. The air echoes with the desperate clang of metal.
     
     
    Area Signal Tower Coverage: [LOW - Medium Danger] \n""",
    {
        "1": ('Move Forward', handle_data_grave_movement_forward),
        "4": ('Run back to the Hardpoint', go_to_the_hardpoint)
    },
    False
)



