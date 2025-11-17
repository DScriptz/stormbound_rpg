import os
import pygame

AUDIO_DIR = "sounds"


""" SOUND HELPERS WHEN PLAYING SOUNDS OR MUSIC """


def initialize_audio():
    """Initializes the Pygame mixer"""
    try:
        pygame.mixer.init(44100, -16, 2, 4096)
        print("Audio mixer initialized.")
    except Exception as e:
        print(f"[Audio Init Error] Failed to initialize mixer: {e}")


def play_sound(sound_name, volume=0.6):
    try:
        sound_path = os.path.join(AUDIO_DIR, f"{sound_name}.ogg")
        sound = pygame.mixer.Sound(sound_path)
        sound.set_volume(volume)
        sound.play()

    except Exception as e:
        print(f"[Sound Error] Couldn't play '{sound_name}'. Check path: {sound_path}. Error: {e}")



def play_music(music_name, volume=0.5, loop=True):
    try:
        music_path = os.path.join(AUDIO_DIR, f"{music_name}.ogg")

        if not os.path.exists(music_path):
            raise FileNotFoundError(f"File not found at: {music_path}")

        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(volume)

        pygame.mixer.music.play(-1 if loop else 0)
    except FileNotFoundError as e:
        print(f"[Music Error] {e}")
    except Exception as e:
        print(f"[Music Error] Couldn't play '{music_name}': {e}")


def music_fadeout(duration=2000):
    """
        This fades out the currently playing background music over a specific duration.

        Args:
            duration(int): The duration of the fade, in milliseconds (ms).
                               Default is 2000 ms (2 seconds).
    """

    try:
        if pygame.mixer.get_busy():
            pygame.mixer.music.fadeout(duration)
            print(f"Music fading out in {duration} secs.")
        else:
            print(f"No music is currently playing")

    except Exception as e:
        print(f"[Audio Error] failed to fade music: {e}")