""" IMPORTS """
from tools import audio_manager
from chapters import chapter1, chapter2, chapter3, chapter4
audio_manager.initialize_audio()

"""  MAIN STORY  """

def main():
    player = chapter1()
    chapter2(player)
    chapter3(player)
    chapter4(player)



if __name__ == "__main__":
    main()










