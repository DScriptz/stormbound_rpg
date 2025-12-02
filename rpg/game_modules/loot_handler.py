import time
import random

def handle_loot(player, enemy):

    loot = enemy.get_loot()

    if isinstance(loot, int):
        player.stormmarks += random.randint(loot, loot + 10)
        print(f"\n[Loot]: You earned {loot} SMKs! Total SMK: {player.stormmarks}")
        time.sleep(1.1)

    elif isinstance(loot, str):
        item_name = loot
        loot_amount = random.randint(1, 2)
        player.inventory[item_name] = player.inventory.get(item_name, 0) + loot_amount

        random_prize_amount = random.randint(35, 50)
        smk = random_prize_amount
        player.stormmarks += smk

        print(f"[Loot]: You found {item_name}! Quantity: {player.inventory[item_name]}. And got +{smk} SMK's!")
        time.sleep(1.1)
    else:
        print(f"{player.name}: 'Aww man, no loot.'")
        time.sleep(1.5)

    return player