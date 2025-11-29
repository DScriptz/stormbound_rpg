import random
from rpg.tools.audio_manager import play_sound



def attack_sound(player):
    if player.player_class == "Rivet-Eye":
        play_sound("gunshot", volume=0.6)

    if player.player_class == "Riftblade":
        sound_list = ['sword', 'sword 2']
        sound = random.choice(sound_list)
        play_sound(sound, volume=0.9)
    else:
        play_sound("attack", volume=0.8)