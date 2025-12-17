
from models.items import Item

item_database = {
    "Quick-Seal Strip": Item(
        name="Quick-Seal Strip",
        price=10,
        heal=12,
        damage=0,
        armor=0,
        description="A flexible adhesive infused with clotting gel. Slap it on, hope it sticks, keep running."
    ),

    "Fieldcare Pack MK-II": Item(
        name="Fieldcare Pack MK-II",
        price=20,
        heal=22,
        damage=0,
        armor=0,
        description="A compact paramedic pouch with pressurized antiseptic spray, fiber stitches, and a mild pain suppressant."
    ),

    "RegenStim Injector": Item(
        name="RegenStim Injector",
        price=35,
        heal=37,
        damage=0,
        armor=0,
        description="A single-use auto-injector containing synthetic growth factors. Burns like fire, works like magic."
    ),
    "Drone CPU": Item(
        name="Drone CPU",
        price=30,
        heal=0,
        damage=0,
        armor=0,
        description="A high-tech CPU that can only be found in Drones roaming in areas outside low Signal Tower coverage."
    ),
    "Salvaged Pipe-gun": Item(
        name="Salvaged Pipe-gun",
        price=40,
        heal=0,
        damage=3,
        armor=0,
        description="A crudely assembled, single-shot firearm; cheap and common."
    ),
    "Reinforced Baton": Item(
        name="Reinforced Baton",
        price=52,
        heal=0,
        damage=5,
        armor=0,
        description="A heavy, weighted police baton wrapped in scavenged metal."
    ),
    "Jury-Rigged Laser Baton": Item(
        "Jury-Rigged Laser Baton",
        75,
        0,
        7,
        0,
        "An unstable weapon using repurposed energy cells; risky but powerful."
    ),
    "Makeshift Combat Knife": Item(
        "Makeshift Combat Knife",
        93,
        0,
        10,
        0,
        "Sharp, reliable, and easily concealed—standard fare for ground-level skirmishes."
    ),
    "The 'Silent-Six' Revolver": Item(
        "The 'Silent-Six' Revolver",
        105,
        0,
        12,
        0,
        "A classic firearm known for its stopping power and surprisingly low noise signature."

    ),
    "D-Grade Weld Patch": Item(
        "D-Grade Weld Patch",
        60,
        0,
        0,
        10,
        "A small, hastily applied reinforcement patch of scrap metal. Increases base durability slightly.",
    ),
    "Titanium-Mesh Weave": Item(
        "Titanium-Mesh Weave",
        450,
        0,
        0,
        25,
        "A flexible, light weave installed beneath the exterior plating. Offers mild protection against shrapnel and prevents stress fractures."
    ),
    "Kinetic Blast Deflector": Item(
        "Kinetic Blast Deflector",
        650,
        0,
        0,
        30,
        "A specialized, angled plate designed to dissipate explosive forces and slow down high-velocity kinetic rounds."
    ),
    "Recalibrated Suspension Frame": Item(
        "Recalibrated Suspension Frame",
        745,
        0,
        0,
        45,
        "An internal structural upgrade that increases the overall load-bearing capacity of the armor, allowing for thicker external plating."
    ),
    "Hardened Ferro-Plate Core": Item(
        "Hardened Ferro-Plate Core",
        1000,
        0,
        0,
        160,
        "The highest-grade armor available. A layered core of processed steel and ceramics, guaranteed by Gauge to withstand sustained punishment."
    )
}