import os
import pickle
import time
from colorama import Fore, Style

save_folder = "save_data"
slot_count = 10

def check_slot_status(slot_number):
    filename = os.path.join(save_folder, f"stormbound_save_{slot_number}.dat")
    return os.path.exists(filename)

def select_save_slot(player):
    print("\n=== SELECT SAVE SLOT ===")


    for slot in range(1, slot_count + 1):
        status = f"{Fore.LIGHTCYAN_EX}IN USE{Style.DIM + Style.RESET_ALL}" if check_slot_status(slot) else f"{Style.BRIGHT}EMPTY{Style.RESET_ALL}"
        print(f"[{slot}] - {status}")

    print("[X] - Cancel Save")
    time.sleep(1.3)

    while True:
        try:
            print(f"\nWhich save slot (1-{slot_count}) would you like to use? ([0] - Cancel): ")
            choice = input(f"\n>>  ")
            slot_number = int(choice)

            if slot_number == 0:
                print("Save Cancelled")
                time.sleep(1.4)
                return False
            if 1<= slot_number <= slot_count:
                break
            else:
                print(f"Invalid slot number. Please choose between 1-10.")
        except ValueError:
            print("Invalid Input. Please Enter a number.")

        """ PLAYER OVERWRITE CONFIRMATION """
    if check_slot_status(slot_number):
        confirm = input(f"Slot {slot_number} is IN USE. Overwrite? (y/n): ")
        if confirm != "y":
            print("Overwrite cancelled")
            return False

    save_game(player, slot_number)
    return True


def select_load_slot():
    """Handles the menu and input validation for loading the game"""
    print("\n=== SELECT LOAD SLOT ===")

    for slot in range(1, slot_count + 1):
        status = f"{Fore.LIGHTCYAN_EX}IN USE{Style.DIM + Style.RESET_ALL}" if check_slot_status(slot) else f"{Style.BRIGHT}EMPTY{Style.RESET_ALL}"
        print(f"[{slot}] - {status}")

    while True:
        try:
            print(f"\nWhich slot (1-{slot_count}) would you like to Load? ([0] - Cancel): ")
            choice = input(f"\n>>  ")
            slot_number = int(choice)

            if slot_number == 0:
                print("Load Cancelled")
                return None  # Returns None if cancelled
            if 1 <= slot_number <= slot_count:
                # Critical check: Don't let them try to load an empty slot
                if not check_slot_status(slot_number):
                    print(f"\nSlot {slot_number} is EMPTY. Please choose an IN USE slot.")
                    time.sleep(1.3)
                    continue
                break
            else:
                print(f"Invalid slot number. Please choose between 1-{slot_count}.")
        except ValueError:
            print("Invalid Input. Please Enter a number.")

    return load_game(slot_number)


def save_game(player, slot_number):
    """
    Saves the entire player object to a specific save slot using the pickle module.

    Args:
        player (Player): The instance of your Player class to be saved.
        slot_number (int): The number of the save slot (e.g., 1, 2, or 3).
    """

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    filename = os.path.join(save_folder, f"stormbound_save_{slot_number}.dat")

    try:
        with open(filename, "wb") as file:
            pickle.dump(player, file)

        print(f"\nGame saved successfully to Slot {slot_number}\n")
        return True

    except Exception as e:
        print(f"Unexpected error has occurred: {e}")
        return False



def load_game(slot_number):
    """
    Loads and reconstructs the Player object from a specific save slot.

    """

    filename = os.path.join(save_folder, f"stormbound_save_{slot_number}.dat")

    if not os.path.exists(filename):
        print(f"\nError: Slot {slot_number} is empty or the file was not found.")
        return None

    try:
        with open(filename, 'rb') as file:
            loaded_player = pickle.load(file)

        print(f"\nGame successfully loaded from Slot {slot_number}.")
        return loaded_player

    except Exception as e:
        # Catches any file reading or corrupted data errors
        print(f"\nAn unexpected error occurred while loading Slot {slot_number}. Save file may be corrupted: {e}")
        return None



