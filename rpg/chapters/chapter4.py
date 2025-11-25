
""" IMPORTS """
import time
from rpg.shops import rusted_rifle_stock
from rpg.tools.shop import Shop
from rpg.shops.healing_shop import ironwind_apothecary
from rpg.dialogues.rusty_apothecary import show_silas_dialogue
from rpg.dialogues.rusted_rifle import show_rhys_dialogue
from rpg.models import Location
from rpg.game_modules.bunks import rent_room, leave_bunk
from rpg.game_modules.mini_games import play_relic_dice
from rpg.models.location_data import watch_post
from rpg.tools import audio_manager
healing_shop = Shop("Rusty Apothecary", ironwind_apothecary)
weapon_shop = Shop("The Rusted Rifle", rusted_rifle_stock)


""" THIS DEFINES THE LOCATION INSTANCE """
coil_bunks = Location(
    "The Coil Bunks",
    "Rows of metallic sleeping pods. The air is stale and quiet. Wexler is running his game in the corner.",
    {
        '1': ("Rent a bunk (30) SMK", rent_room),
        '2': ("Play 'The Relic Dice'", play_relic_dice),
        'x': ("Exit The Coil Bunks", leave_bunk),
    }
)

def leave_ironwind_outpost(player):
    print("\nAs you walk towards the exit, you hear a footstep coming fast at you,")
    time.sleep(1.5)
    print(f"Kael Rowan: '{player.name}! Before you go, I just want to thank you for your help from the thief earlier'")
    time.sleep(1.7)
    print(f"Kael Rowan: 'I've got something for ya, here.'")
    time.sleep(1.5)
    print("Kael shows you a Faction Badge: Ironwinders")
    time.sleep(1.5)
    print("Kael Rowan: 'If you want, you can be one of us.'")
    time.sleep(1.5)

    while True:
        print("\nDo you want to join this faction (Y/N)?")

        choice = input("\n>> ").strip().lower()

        match choice:
            case "y":
                print(f"{player.name}: 'Alright **shakes hands**, we got a deal'")
                time.sleep(1.5)
                player.faction = "Ironwinders"
                print(f"Kael Rowan: 'Welcome to the {player.faction}, {player.name}.'")
                time.sleep(1.5)
                player.show_status()
                input("Press [Enter] to continue: ")
                break
            case "n":
                print(f"{player.name}: 'I think I can handle myself, thanks for the offer tho.'")
                print("Kael Rowan: 'Got it, you can always come back here.'")
                break
            case _:
                print(f"{player.name}: 'Uhh...'")
                continue

    print("Kael Rowan: 'Oh and before you go, I hope you didn't forget to visit the watchpost-'")
    time.sleep(1.7)
    print("Kael Rowan: 'Commander Thorne would appreciate if you could help with the bounties,'")
    time.sleep(1.8)
    print("anyways, come I'll drive you to The Hardpoint.")
    time.sleep(1.5)

""" SHOWS THE PLAYER THE SHOPS THEY CAN GO TO """

def show_shop_choices(player):

    print("You looked around and there's 2 shops waving their offers to you...")
    time.sleep(1.3)
    print(f"{player.name}: 'There's a bunch of shops huh?'")
    time.sleep(1.2)
    while True:

        print("\n[1] - Rusty Apothecary: Meds & Safety")
        print(f"[2] - The Rusted Rifle: Weapon & Ammo Needs")
        print(f"[X] - Go back to the Nexus Point")

        choice = input("\n>> ").strip().lower()

        match choice:

            case "1":
                show_silas_dialogue()
                time.sleep(1.7)
                healing_shop.open_shop(player)

            case "2":
                show_rhys_dialogue()
                time.sleep(1.7)
                weapon_shop.open_shop(player)

            case "x":
                print(f"{player.name}: 'That was nice.'")
                time.sleep(1.2)
                break

            case _:
                print(f"\n{player.name}: 'Gahh, can't decide...'")

""" THIS HANDLES THE DIRECTION THE PLAYER CAN GO """

def show_directions():
    print("\n[1] - North: 'Alley Of Remedies'")
    print("[2] - East: 'The Coil Bunks'")
    print("[3] - West: 'The Watchpost'")
    print("[X] - Exit Ironwind Outpost: Open World")

""" THIS HANDLES THE CHAPTER 4 LOOP """

def chapter4(player):
    audio_manager.play_music("ironwind outpost", volume=0.7, loop=True)
    print("\n---------------------- Chapter 4: The Ironwind Outpost ----------------------")
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
    time.sleep(1.2)
    print("You are now in The Nexus Point (center)")
    time.sleep(1.1)

    while True:
        player.show_status()
        show_directions()

        choice = input("\n>> ").strip().lower()

        match choice:

            case "1":
                print(f"{player.name}: 'Alley of... Remedies? What could be here?'")
                time.sleep(1.2)
                print("You walk north, to the Alley of Remedies...")
                time.sleep(1.1)
                show_shop_choices(player)

            case "2":
                print(f"{player.name}: 'Huh, maybe a place to sleep?'")
                time.sleep(1.2)
                print("You walked towards 'The Coil Bunks'...")
                time.sleep(1.3)
                player = coil_bunks.enter(player)
            case "3":
                print(f"{player.name}: 'I should check the watch post. There might be opportunities there.'")
                time.sleep(1.2)
                print("You walked towards the Ironwind Watch Post")
                time.sleep(1.3)
                player = watch_post.enter(player)


            case "x":
                leave_ironwind_outpost(player)
                audio_manager.music_fadeout(duration=2000)
                audio_manager.music_stop()
                break
            case _:
                print(f"{player.name}: 'Hmm, can't decide..'")
                time.sleep(0.5)




