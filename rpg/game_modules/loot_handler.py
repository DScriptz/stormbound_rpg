import time

def handle_loot(player, enemy):

    loot = enemy.get_loot()

    if isinstance(loot, int):
        player.stormmarks += loot
        print(f"\n[Loot]: You earned {loot} SMKs! Total SMK: {player.stormmarks}")

    elif isinstance(loot, str):
        item_name = loot

        player.inventory[item_name] = player.inventory.get(item_name, 0) + 1

        print(f"[Loot]: You found {item_name}! Quantity: {player.inventory[item_name]}")

    else:
        print(f"{player.name}: 'Aww man, no loot.'")
        time.sleep(1.5)

    return player