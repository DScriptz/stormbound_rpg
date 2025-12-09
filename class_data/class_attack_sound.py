import random
from tools.audio_manager import play_sound



def attack_sound(player):
    if player.player_class == "Rivet-Eye":
        play_sound("gunshot", volume=0.6)

    if player.player_class == "Flash Tracer":
        sound_list = ['riftblade', 'sword', 'sword 2']
        sound = random.choice(sound_list)
        play_sound(sound, volume=0.9)

    if player.player_class == "Aethermancer":
        play_sound("aethermancer attack", volume=0.7)

    if player.player_class == "Scrap Brawler":
        play_sound("scrap brawler attack",  volume=0.9)
    else:
        play_sound("attack", volume=0.8)