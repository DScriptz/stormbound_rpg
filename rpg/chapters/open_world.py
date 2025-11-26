import time
from rpg.tools.audio_manager import *
from rpg.world_map.area_data import go_to_the_hardpoint


def open_world(player):
    play_music("the hardpoint", volume=0.7, loop=True)
    go_to_the_hardpoint(player)


