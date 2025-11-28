import random

move_right_success = [
    "You skirt the perimeter of a crater, using the twisted foundation as cover.",
    "The wind howls through shattered concrete ribs, but you find a brief respite in the lee of a collapsed tower.",
    "A massive, fallen ventilation duct provides a temporary tunnel to bypass a heavily obstructed area.",
    "You successfully thread the gap between two leaning, colossal ferrocrete slabs.",
    "You utilize the shadow of a half-standing skyscraper, keeping your movement hidden as you proceed.",
    "A loud metallic shriek echoes nearby, but you recognize the sound of twisting rebar, not an enemy.",
    "You find a surprisingly stable path across old network conduit, gaining valuable steps.",
    "You spot a worn service access route—slow going, but a clear advance.",
    "A broken hydraulic line provides just enough grip to scale a tricky pile of debris.",
    "You successfully hack a defunct environmental door to create a new, temporary shortcut.",
    "You use a dense cluster of rebar as a makeshift ladder, pushing ahead.",
    "Fine rust-dust fills the air, but you quickly find an avenue shielded from the worst of the fallout.",
    "You expertly bypass a visible pressure plate trap, maintaining your pace.",
    "A section of unbroken pavement provides smooth ground, allowing you to quickly cover distance.",
    "The metallic clang of shifting wreckage settles, granting you quiet passage for a few critical steps.",
    "You spot valuable discarded shielding material and use it to steady your footing.",
    "You gain valuable ground by carefully following the edge of an old, vertical service shaft.",
    "You find a trail left by an old automated scavenger bot and follow its efficient, winding route.",
    "A careful leap over a gaping fissure takes you past a major obstacle.",
    "The blinking light of a malfunctioning security camera confirms you are undetected, allowing you to slip past."
]
def show_dialogue():
    print(random.choice(move_right_success))