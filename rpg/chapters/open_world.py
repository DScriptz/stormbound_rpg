import time

from rpg.areas.area_data import go_to_data_grave, go_to_the_hardpoint


def open_world(player):
    print("\nAfter a few hours, You and Kael reached The Hardpoint...")
    time.sleep(1.5)
    print("Kael Rowan: 'Well, here it is... the place people call 'The Hardpoint'.'")
    time.sleep(1.5)
    print("Be careful around here, it may look safe but there's scavengers and AI S-7 Bots roaming around in here...")
    time.sleep(1.8)
    print(f"{player.name}: 'I'll be careful, thanks for the ride, I'll take it from here'")
    time.sleep(1.5)
    print("Kael nods, then gets on his jeep and drove away...")
    time.sleep(1.5)
    print(f"\n{player.name}: '**sighs** This used to be Manila huh...'")
    time.sleep(1.5)
    go_to_the_hardpoint(player)


