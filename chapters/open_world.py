# import time
from areas.the_hardpoint_area import go_to_the_hardpoint
from tools.audio_manager import play_music


def open_world(player):
    play_music("the hardpoint", volume=0.7, loop=True)
    go_to_the_hardpoint(player)


