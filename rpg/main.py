""" IMPORTS """
from chapters import chapter1, chapter2, chapter3, chapter4, game_intro, open_world


def main():
    game_intro()
    player = chapter1()
    chapter2(player)
    chapter3(player)
    chapter4(player)
    open_world(player)


if __name__ == "__main__":
    main()