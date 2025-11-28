import time
from rpg.models.location_data import Location
from rpg.game_modules.salvage_cache import handle_cache_loot

def go_to_salvage_cache(player):
    player.location = "Salvage Cache"
    print("You saw an open wall on the side of an abandoned building...")
    time.sleep(1)
    print("And walked towards it...")
    time.sleep(1.2)
    salvage_cache.enter(player)

    return player


salvage_cache = Location(

    "Salvage Cache",
    """\nThe Salvage Cache. You are standing inside a reinforced, pressurized vault—a hidden bubble of calm carved 
out of the hostile Data Grave. The thick walls dampen the constant shriek of the wind, leaving only the 
low, rhythmic hum of internal cooling systems.

    Area Signal Tower Coverage: [LOW - Medium Danger] \n""",
    {
        "1": ('Process Salvage and return to the Hardpoint', handle_cache_loot)
    }

)