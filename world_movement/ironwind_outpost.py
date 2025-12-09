import time
from tools.audio_manager import music_stop, music_fadeout




def go_to_ironwind_outpost(player):
    from chapters.chapter4 import return_to_ironwind_outpost

    print("\nYou ran to the muddy, dirty road and picked up your radio, signaling the Ironwinder Guard for transport...")
    time.sleep(1.4)
    music_fadeout(2000)
    music_stop()
    print("Loading area...")
    time.sleep(1.5)
    return_to_ironwind_outpost(player)