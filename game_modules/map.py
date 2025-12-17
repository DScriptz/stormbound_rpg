import time
from colorama import Style

bright = Style.BRIGHT
reset = Style.RESET_ALL


map_info = {
    "The Data Grave": {
        "description": "The skeletal remains of a massive tech corporation. \nHigh risk of automated sentinels. The air is thick with ionized static.",
        "direction": f"\n{bright}Accessible via: [The Hardpoint] > [The Data Grave]{reset}",
        "lore": "Many people have died here, their data ghosts trapped in the ruins. "
                "Some said that if you walk/run 20 steps in all"
                "directions, you'll see a hidden power vault."
    },
    "The Hardpoint": {
        "description": "The central hub of the resistance. Always safe.",
        "direction": f"\n{bright}Accessible via: [Ironwind Outpost] > [The Hardpoint] OR [Open World/Other Locations] > [The Hardpoint]{reset}",
        "lore": "In this central area of Stormbound, many places can be explored. \nIt is said to be the 'center'"
                "of the Signal Tower that encrypts the corrupted data that are being used by the 'Storm'. \nMaking this place"
                " somewhat very safe and undetected by the Drones."
    },
    "The Foundry": {
        "description": "The place used to be a factory for creating metallic machineries. \nNow after The 'Storm' happened, "
                       "It got abandoned and the remains inside were left to decay...",
        "direction": f"\n{bright}Accessible via: [The Hardpoint] > [The Foundry]{reset}",
        "lore": "It was a newly built factory 1-2 years before 'The Storm' invasion (2022-2023). "
                "\nThe operations in this was just getting started but then halted by the invasion."
                "\n15 steps in all directions may lead you to a new area..."
    },
    "Ironwind Outpost": {
        "description": "A hidden, spacious, and somewhat populated outpost 3 miles East of The Hardpoint. ",
        "direction": f"\n{bright}Accessible via: [The Hardpoint] > [Ironwind Outpost] OR [The Open World] > [Ironwind Outpost]{reset}",
        "lore": "A group of rogue Ex-Militants has bonded together after 'The Storm' and gathered scraps and sheets of "
                "metals to create a base, and soon after found more Ex-Militants to recruit, creating the Faction 'The Ironwinders'."
    },

}


def show_map():
    print("\n     --- [WORLD MAP] ---")
    print("    [DIGITAL MAP INITIALIZING...]\n")
    time.sleep(0.7)
    print(f"\nKnown locations around Stormbound:")
    for location_name, data in map_info.items():
        print(f'\n-> {location_name}: {data["description"]}\n {data["direction"]}')
    print("-" * 20)
    input("\nPress [Enter] to continue: ")
    return


def show_location_details(player):

    data = map_info.get(player.location)

    if not data:
        print(f"\n{player.location} doesn't exist.")
        return

    print(f"\n=== [ Location Data: {player.location} ] ====")

    print("Zone Description:")
    print(data["description"])

    print("\nLocal Lore/Rumor:")
    print(data["lore"])
    print("=" * 30)
    input("\nPress [Enter] to continue: ")
    return
