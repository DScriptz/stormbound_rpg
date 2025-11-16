
""" IMPORTS """
from rpg.shop import Shop
from rpg.shops.healing_shop import ironwind_apothecary
import time



""" THIS HANDLES THE DIRECTION THE PLAYER CAN GO """
healing_shop = Shop("Rusty Apothecary", ironwind_apothecary)

def show_shop_choices(player):
        print("You looked around and there's 2 shops waving their offers to you...")
        time.sleep(1.3)
        print(f"{player.name}: 'There's a bunch of shops huh?'")
        time.sleep(1.2)
        while True:
            print("[1] - Rusty Apothecary: Meds & Safety")
            print(f"[2] - The Rusted Rifle, weapon & ammo needs")

            choice = input("\n>> ")

            match choice:
                case "1":
                    healing_shop.open_shop(player)






def show_directions():
    print("\n[1] -  North")
    print("[2] - East")
    print("[3] - West")


""" THIS HANDLES THE CHAPTER 4 LOOP """


def chapter4(player):
    print("\n---------------------- Chapter 4:The Ironwind Outpost ----------------------")
    time.sleep(0.6)

    skip_choice = input("Do you want to skip the dialogue? (Y/N): ").lower().strip()

    match skip_choice:
        case "n":
            print("Dust swirls around the crumbling concrete walls, catching the faint orange glow of the hanging lamps.")
            time.sleep(1.5)
            print("So you walked around the outpost, seeing busy people talking, ")
            time.sleep(1.4)
            print("Excavating from the mines, researching...")
            time.sleep(1.3)
            print("The faint smell of processed food mixes with the scent of disinfectant and rust passes through your nose")
            time.sleep(1.5)
            print("You catch a glimpse of a scavenger kid darting past, holding a bundle of scrap almost bigger than themselves.")
            time.sleep(1.6)


        case _:
            print("You skipped the dialogue!")
            time.sleep(0.3)

    print(f"\n{player.name}: 'This is plenty... where should I go?'")
    player.show_status()
    while True:
        show_directions()

        choice = input("\n>> ")

        match choice:

            case "1":
                print(f"{player.name}: 'Alley of... Remedies? What could be here?'")
                time.sleep(1.2)
                print("You walk north, to the Alley of Remedies...")
                time.sleep(1.1)

            case "2":
                pass

            case "3":
                pass

            case _:
                print(f"{player.name}: 'Hmm, can't decide..'")
                time.sleep(0.5)




