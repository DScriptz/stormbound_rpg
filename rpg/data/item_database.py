
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
    
}

