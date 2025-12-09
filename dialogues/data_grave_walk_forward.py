import random

DATA_GRAVE_FORWARD_DIALOGUES = [
    "Another segment of the Iron Road cleared. Just more scrap ahead.",
    "The air here smells like ozone and failed memory banks.",
    "Keep moving. Still too many shadows that aren't shadows.",
    "My thermal display keeps showing phantom heat signatures. Stay sharp.",
    "A thousand discarded processors litter the path. Every piece has a story I don't want to hear.",
    "This quiet is worse than the static. Something's listening.",
    "I should be past the boundary now. The terrain is getting rougher.",
    "Just another few klicks. Focus on the objective, nothing else.",
    "The data stream is thicker here—like wading through code.",
    "Found an old power cell. It's dead, like everything else here.",
    "My boots crunch on shattered glass and circuit boards. Sounds like home.",
    "Checking my chronometer. Time moves differently in the Grave.",
    "The wind whistles through the broken antennae. Sounds like whispering.",
    "I remember the blueprints for this section... they lied.",
    "Can't shake the feeling of being watched. Just nerves, I hope.",
    "Another step. Another battle I can't afford to lose.",
    "The ground here is slick with crystallized data corruption.",
    "Gotta find better cover soon. I'm exposed out here.",
    "This Lineage doesn't quit. Keep pushing forward.",
    "Scanning the horizon. Nothing but rust and the ghosts of forgotten networks.",
]

def show_random_movement_line():
    """ Prints out a random line from the list above """
    dialogue = random.choice(DATA_GRAVE_FORWARD_DIALOGUES)
    print(dialogue)