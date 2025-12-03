import time

map_info = {
    "The Data Grave": {
        "description": "The skeletal remains of a massive tech corporation. High risk of automated sentinels. The air is thick with ionized static.",
        "lore": "Many people have died here, their data ghosts trapped in the ruins. "
                "Some believe that if you walk/run 20 steps in all"
                "directions, you'll see a hidden power vault.",
    },
    "The Hardpoint": {
        "description": "The central hub of the resistance. Always safe.",
        "lore": "In this central area of Stormbound, many places can be explored.",
    }
}


def show_map():
    print("\n--- [WORLD MAP] ---")
    print("[DIGITAL MAP INITIALIZING...]\n")
    time.sleep(0.7)
    print(f"\nKnown locations around Stormbound:")
    for location_name, data in map_info.items():
        print(f'-> {location_name}: {data["description"]}')
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
