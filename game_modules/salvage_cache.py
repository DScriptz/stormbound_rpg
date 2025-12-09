import time




def handle_cache_loot(player):
    print("\n[ PROCESSING SALVAGE ] Accessing the console...")
    time.sleep(1.3)
    print("The vault's inventory data transfers to your HUD. You collect the key items and SMK.")
    time.sleep(1.2)

    smk_reward = 150
    item_reward = "Fieldcare Pack MK-II"

    player.stormmarks += smk_reward
    player.inventory[item_reward] = player.inventory.get(item_reward, 0) + 2

    print(f"\n[ REWARD RECEIVED ]")
    print(f"  + {smk_reward} Stormmarks (New Total: {player.stormmarks})")
    print(f"  + 2x {item_reward}")

    player.location = "The Hardpoint"
    player.location_steps = 0

    print("\nYou secured the loot and are headed back to The Hardpoint...")
    time.sleep(1.2)
    from areas.the_hardpoint_area import go_to_the_hardpoint

    player.location_steps = 0

    return go_to_the_hardpoint(player)



