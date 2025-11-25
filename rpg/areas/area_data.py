import time
from rpg.models.location_data import Location

""" THESE HANDLES THE FUNCTIONS FOR EACH LOCATION """
def go_to_data_grave(player):

    print("You walked forward, to the Data Grave...")
    data_grave.enter(player)

    return True

def go_to_the_hardpoint(player):
    print("You walked forward into this somewhat abandoned place...")
    time.sleep(1.5)
    the_hardpoint.enter(player)

the_hardpoint = Location(
    "The Hardpoint",
    """\nThe Hardpoint, covered by the 'Signal Towers'. Not a single place, but a chaotic zone. Roads are buried under dead machinery, "
    "and desperate life clings to skeletal skyscrapers. It's a loud, sprawling city of the desperate, "
    "defined by the distant rumble of the Dead Zone. The best loot is here, and so is the worst danger.""",
    {
        "1": ('Explore the Data Grave', go_to_data_grave),
    },
    True
)

data_grave = Location(
    "The Data Grave",
    "\nThe Data Grave. A massive, sprawling landfill where every scrap has been scavenged a hundred times."
    " The main danger is competition. Rival Scrapper crews patrol the perimeter and have rigged rudimentary,"
    " physical traps to protect their claims. The air echoes with the desperate clang of metal.",
    {
        "1": 'Move Forward'
    },
    False
)



