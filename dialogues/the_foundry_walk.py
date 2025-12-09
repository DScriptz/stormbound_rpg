import random


forward_lines = [
    "A jet of superheated steam erupts to your left; you pivot sharply, the heat searing your skin.",
    "The ground vibrates violently as a distant hydraulic press impacts. You stumble but keep moving.",
    "You dodge a hanging cable snapping loose, the thick insulation whipping past your ear.",
    "The stench of burnt lithium and iron is overwhelming; you taste metal with every ragged breath.",
    "You kick a discarded Sentinel casing that rolls away with a hollow, echoing clang.",
    "Ahead, the dense smog momentarily thins, revealing a massive, skeletal crane frozen overhead.",
    "The oppressive, rhythmic *thrum* of the factory machinery presses on your chest.",
    "You scramble over a low pile of sparking metal debris, gaining a quick burst of speed.",
    "A warning siren blares briefly from the floor below, instantly cut short by a grinding silence.",
    "The air is so thick with soot it feels like running through heavy silt.",
    "You slip on a slick patch of cooled slag, catching yourself before a nasty fall.",
    "The low-grade emergency lights flicker rapidly, casting erratic shadows that twist your vision.",
    "You hear the distinct, heavy footfall of a patrolling drone, forcing you to hug the nearest shadow.",
    "Your boots crunch on something glass-like—the shattered remnants of an old monitor.",
    "The air momentarily turns ice-cold as you pass a massive, leaking coolant pipe.",
    "You nearly run straight into a wall of rusting scaffolding, veering off just in time.",
    "A small piece of molten slag drips from above, hitting the ground with a quick *sizzle*.",
    "You pass beneath a sign warning of an **UNCHECKED AUTOMATION ZONE**, the paint peeling from the heat.",
    "The running helps momentarily clear the static from your thoughts, but the environment quickly rushes back in.",
    "You spot a brief flash of red light—a security eye—and duck behind a stack of damaged coils."
]

def show_forward_dialogue():
    print(random.choice(forward_lines))
    return

walk_right_lines = [
    "You carefully hug the massive support beams, keeping to the shadows and listening for drones.",
    "A thick, grimy layer of oil coats the floor here. You step with slow, deliberate caution.",
    "You find yourself weaving through tight gaps between giant pressure valves, careful not to snag your gear.",
    "The air is noticeably hotter near this wall. You quickly check for steam leaks.",
    "You spot a discarded, rusted crowbar wedged in a pipe junction. It offers no immediate help.",
    "A dull, blue pilot light flickers nearby, providing the only static reference point in the fog.",
    "You pause briefly to scan the structural integrity of the ceiling; everything looks dangerously weak.",
    "The sound of your own footsteps is muffled by the ambient hum, making you feel isolated.",
    "You notice faint scratch marks—likely from another Scrapper—leading into a dark alleyway.",
    "You pass a sealed maintenance door; the emergency override terminal glows a sickly amber.",
    "A rat, half-metal and scurrying fast, darts past your boots and vanishes into the gloom.",
    "You use a piece of broken rebar to test the footing before stepping onto a metal grate.",
    "The dense smog makes judging distances almost impossible. You rely on feel and sound.",
    "A large, silent ventilation fan slowly spins overhead, covered in decades of black dust.",
    "You take note of a small container of useful-looking chemicals, but it’s too risky to grab now.",
    "The low-frequency hum of the factory causes a slight, dull ache behind your eyes.",
    "You step over a pile of fused electronics, taking care not to trip the exposed wiring.",
    "A cascade of cold condensation drips onto your shoulder, a welcome, momentary relief from the heat.",
    "You find an old warning label peeling off the wall, but the text is too corroded to read.",
    "You shift your weight to move around a massive, unmoving industrial gear, its teeth razor-sharp."
]

def show_right_dialogue():
    print(random.choice(walk_right_lines))
    return

walk_left_lines = [
    "You stick close to the massive cooling vents, the forced air momentarily chilling the sweat on your neck.",
    "A vast, darkened section of the factory floor stretches out to your left, obscured by smoke and shadow.",
    "You carefully skirt the edge of an access hole in the floor, dropping off into complete darkness below.",
    "You hear a faint, metallic scraping sound that stops abruptly when you cease moving.",
    "The heavy smell of rust and old iron is strongest here; this area hasn't been used in years.",
    "You spot a piece of what looks like civilian clothing caught on a conveyor belt. Best not to look closer.",
    "A dull orange glow pulses from inside a locked control booth, suggesting a hidden terminal is still active.",
    "You step around a puddle of stagnant, viscous fluid, unsure if it's oil or something more toxic.",
    "Your boots scuff against fine metal filings left over from grinding operations.",
    "You take shelter momentarily behind a stack of oversized, forgotten gear assemblies.",
    "A faint, electrical hum seems to follow you as you walk, suggesting proximity to a power line.",
    "You use your arm to push aside a heavy curtain of plastic sheeting, revealing a dead-end corridor.",
    "The floor is covered in discarded tools; you pick up a wrench and toss it, checking for traps.",
    "You notice a warning light—flashing a rapid red—but it has long since been disconnected from power.",
    "A sudden burst of wind from an unknown source tugs at your gear, unsettling your balance.",
    "You pass beneath a network of thick, interlocking pipes that look ready to burst from internal pressure.",
    "You peer over a low barricade and see nothing but a slow river of polluted water running beneath the factory.",
    "The dense, particulate air makes your eyes sting; you blink rapidly to clear your vision.",
    "You check your weapon's status; the low light makes every precaution feel necessary.",
    "You move around a partially melted piece of machinery, the plastic shell still soft and tacky to the touch."
]

def show_left_dialogue():
    print(random.choice(walk_left_lines))
    return
