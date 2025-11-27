
from rpg.models.items import Item

item_database = {
    "Quick-Seal Strip": Item(
        name="Quick-Seal Strip",
        price=10,
        heal=10,
        damage=0,
        description="A flexible adhesive infused with clotting gel. Slap it on, hope it sticks, keep running."
    ),

    "Fieldcare Pack MK-II": Item(
        name="Fieldcare Pack MK-II",
        price=20,
        heal=20,
        damage=0,
        description="A compact paramedic pouch with pressurized antiseptic spray, fiber stitches, and a mild pain suppressant."
    ),

    "RegenStim Injector": Item(
        name="RegenStim Injector",
        price=35,
        heal=35,
        damage=0,
        description="A single-use auto-injector containing synthetic growth factors. Burns like fire, works like magic."
    ),
    "Drone CPU": Item(
        name="Drone CPU",
        price=30,
        heal=0,
        damage=0,
        description="A high-tech CPU that can only be found in Drones roaming in areas outside low Signal Tower coverage."
    ),
    "Salvaged Pipe-Gun": Item(
        name="Salvaged Pipe-Gun",
        price=40,
        heal=0,
        damage=3,
        description="A crudely assembled, single-shot firearm; cheap and common."
    ),
    "Reinforced Baton": Item(
        name="Reinforced Baton",
        price=52,
        heal=0,
        damage=5,
        description="A heavy, weighted police baton wrapped in scavenged metal."
    )

    
}

