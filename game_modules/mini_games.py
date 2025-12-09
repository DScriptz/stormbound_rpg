import random
import time
from tools import audio_manager



def play_relic_dice(player):
    roll = random.randint(1, 6)
    while True:
        player.show_status()
        bet = input("\nHow many SMK's do you want to bet? (X to Exit) >>  ").lower().strip()

        if bet == "x":
            print(f"{player.name}: 'Nevermind, betting can wait later. *shrugs*.'")
            time.sleep(0.8)
            return False

        try:
            bet_amount = int(bet)
            if bet_amount <= 0:
                print(f"{player.name}: 'Oh my bad-'")
                time.sleep(1.3)
                continue
            if bet_amount > player.stormmarks:
                print(f"{player.name}: 'Oh, I don't have enough SMKs left...'")
                time.sleep(1.3)
                continue
            break
        except ValueError:
            print("Please type a whole number.")

    """ DEDUCTS THE STORMMARKS TO PREVENT CHEATING """
    player.stormmarks -= bet_amount

    print(f"\nYou bet {bet_amount} SMK and toss the salvaged Relic Dice...")
    audio_manager.play_sound("dice shake", volume=0.8)
    time.sleep(1.3)
    print("\nAnd the Relic Dice settles on...")
    time.sleep(1.7)
    audio_manager.play_sound("dice roll", volume=0.8)
    print(f"\n{roll}")
    time.sleep(1.5)

    if roll <= 3:
        """ THE BET WAS ALREADY DEDUCTED """
        print(f"The Relic Dice short-circuits, you lost the bet! -{bet_amount} SMK.")
        time.sleep(1.5)

    elif roll <= 5:
        win_amount = int(bet_amount * 1.5 + 5)
        player.stormmarks += win_amount
        print(f"The dice flickers a light! You won {win_amount} SMK!!")
        time.sleep(1.5)

    else:

        jackpot = int(bet_amount * 3 + 10)
        player.stormmarks += jackpot
        print(f"JACKPOT! The Dice shines! You win a MASSIVE {jackpot} SMK!")

    player.show_status()
    input("Press [Enter] To Continue >> ")

    return True

