""" IMPORTS """

from chapters import (chapter1, chapter2, chapter3, chapter4,
                      game_intro,
                      open_world)
from rpg.areas.data_grave_area import go_to_data_grave
from rpg.areas.salvage_cache_area import go_to_salvage_cache

def main():
    loaded_player = game_intro()

    if loaded_player is not None:

        player = loaded_player

    else:
        print("\nStarting a new game...\n")
        player = chapter1()

    chapter_flow(player)

def chapter_flow(player):

    if player.current_chapter <= 2:
        chapter2(player)

    if player.current_chapter <= 3:
        chapter3(player)

    if player.current_chapter <= 4:
        chapter4(player)

    if player.current_chapter >= 5:
        if player.location == "The Data Grave":
            go_to_data_grave(player)

        elif player.location == "Salvage Cache":
            go_to_salvage_cache(player)

        else:
            open_world(player)



if __name__ == "__main__":
    main()