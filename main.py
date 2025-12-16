""" IMPORTS """
from areas.data_grave_area import go_to_data_grave
from areas.salvage_cache_area import go_to_salvage_cache
from areas.the_foundry_area import go_to_the_foundry
from areas.the_hardpoint_area import go_to_the_hardpoint
from areas.the_molten_spill_area import go_to_molten_spill
from chapters import (chapter1, chapter2, chapter3, chapter4, chapter5,
                      open_world, return_to_ironwind_outpost)
from game_modules.game_intro import game_intro
from tools.audio_manager import initialize_audio

initialize_audio()


def chapter_flow(player):
    if player.current_chapter <= 2:
        chapter2(player)

    if player.current_chapter <= 3:
        chapter3(player)

    if player.current_chapter <= 4:
        chapter4(player)

    if player.current_chapter >= 5:
        chapter5(player)

    if player.location:
        if player.location == "The Data Grave":
            go_to_data_grave(player)

        elif player.location == "Salvage Cache":
            go_to_salvage_cache(player)

        elif player.location == "The Foundry":
            go_to_the_foundry(player)

        elif player.location == "The Molten Spill":
            go_to_molten_spill(player)

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

# SemVer self reminders: Use 'Major, Minor, Patch' (E.G "v0[Major].1[Minor].0[Patch]) when naming versions.
