import time
import sys
from rpg.tools import audio_manager


def game_intro():
    audio_manager.play_music("stormbound menu", volume=0.6, loop=True)
    print("\n[----------------------------------------------------------]")
    print("                   -{ STORMBOUND HAVEN }-                      ")
    print("[----------------------------------------------------------]\n")
    while True:

        print("             ============ [MENU] ============")
        print("            [1] - Start Game | [2] - Game info / Story")
        print("            [3] - Credits | [4] - Quit\n")

        choice = input("-->  ")

        match choice:

            case "1":
                print("\nStarting game...")
                time.sleep(1.4)
                audio_manager.music_fadeout(duration=2000)
                print("Loading game...")
                time.sleep(2)

                break

            case "2":
                print("                    ---------- STORMBOUND LORE ----------")
                print('''\nStormbound Haven is a Dystopian text-based RPG, set in 2035 after a self-aware AI Virus the people
 called the "Storm" invaded the world. To this day, people still don't even know who spread it... Factions around the world
 consisting of different people have bonded together and it has caused many faction wars and destruction.
 Will you be able find out who's the mastermind behind all the chaos?\n''')
                input("-> Press [Enter] to continue: ")

            case "3":
                print("                   ---- CREDITS ----")
                print("\nWriting and Story: [Github] - DScriptz | Dwayne Japor\n")
                print("Sounds: [Pixabay] - https://pixabay.com,"
                      " [Myinstants]- https://www.myinstants.com/en/index/us,"
                      " [Tabletop Audio] - https://tabletopaudio.com\n")
                print("Code: [Github] - DScriptz | Dwayne Japor\n")
                input("-> Press [Enter] to continue: ")
            case "4":
                print("Thanks for playing my game! Hope you try it again! ")
                time.sleep(1.3)
                sys.exit()



