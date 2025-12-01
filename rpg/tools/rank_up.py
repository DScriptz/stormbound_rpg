


def get_rank(player):
    battles = player.battles_completed

    if battles >= 220:
        return "The Hardpoint Legend"
    elif battles >= 101:
        return "Stormbound Master"
    elif battles >= 81:
        return "Circuit Breaker"
    elif battles >= 65:
        return "Velocity Pilot"
    elif battles >= 50:
        return "Ironclad Runner"
    elif battles >= 43:
        return "Scrap Butcher"
    elif battles >= 35:
        return "Data Cipher"
    elif battles >= 21:
        return "Junk Runner"
    elif battles >= 11:
        return "Drone Hunter"
    elif battles >= 6:
        return "Fringe Rat"
    elif battles >= 3:
        return "Copper Grunt"
    elif battles >= 1:
        return "Green Tag"
    else:
        return "Scrap Initiate"


