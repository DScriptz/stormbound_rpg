import random


move_left_success = [
    "You slip through a narrow crevice beneath a collapsed wall, finding a shaded, forgotten route.",
    "A broken drainage channel offers a low, crawl-space path. It's muddy, but you gain ground.",
    "You move carefully along the edge of the Data Grave, keeping to the deeper, less disturbed shadows.",
    "You find an access hatch leading to a sub-level corridor, bypassing a high-traffic zone.",
    "The air is still and heavy here; you move quickly, making the most of the quiet passage.",
    "You use a layer of discarded, insulating foam to dampen your footsteps and advance silently.",
    "You successfully navigate a labyrinth of rusted pipes and exposed wires on the ground level.",
    "You find a low-ceilinged area covered by heavy canvas—it's cramped but keeps you hidden.",
    "A slow but necessary passage through ankle-deep water takes you past a major wreckage pile.",
    "You spot footprints belonging to an enemy patrol, but successfully find an alternate parallel path.",
    "You discover a hidden maintenance tunnel, providing surprisingly rapid progress.",
    "The ground shifts beneath your feet, but you quickly find a stable route against the wall.",
    "You avoid a series of crude tripwires and nets laid out by rival scavengers, keeping your pace.",
    "You move beneath the hull of a ruined transport, using the shadow to avoid detection.",
    "A thick bank of discarded server racks acts as a perfect shield while you advance.",
    "You find a small cache of coolant fluid which smooths your path through a sticky metal segment.",
    "You follow a barely visible trail marked by faint scratchings on the bedrock.",
    "You climb down into a deep gully, using the terrain to block line of sight and advance.",
    "The air smells foul here, but the lack of movement suggests this low path is safer.",
    "You successfully bypass a loud steam leak by going underneath the damaged pipeline."
]

def show_dialogue():
    print(random.choice(move_left_success))