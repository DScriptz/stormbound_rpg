""" IMPORTS """

from chapters import (chapter1, chapter2, chapter3, chapter4,
                      open_world, return_to_ironwind_outpost)
from areas.data_grave_area import go_to_data_grave
from areas.salvage_cache_area import go_to_salvage_cache
from areas.the_foundry_area import go_to_the_foundry
from areas.the_hardpoint_area import go_to_the_hardpoint
from game_modules.game_intro import game_intro


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

        elif player.location == "The Foundry":
            go_to_the_foundry(player)

        elif player.location == "Ironwind Outpost":
            return_to_ironwind_outpost(player)

        elif player.location == "The Hardpoint":
            go_to_the_hardpoint(player)

        else:
            open_world(player)

    return player


def main():
    loaded_player = game_intro()

    if loaded_player is not None:

        player = loaded_player

    else:
        print("\nStarting a new game...\n")
        player = chapter1()

    chapter_flow(player)

    return

if __name__ == "__main__":
    main()