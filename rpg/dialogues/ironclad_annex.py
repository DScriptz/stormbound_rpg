import random

npc_dialogue = [
    "Gauge: I deal in millimeters and microns. Your survival depends on tolerances. Don't waste my measurements.",
    "Gauge: Max HP ain't just padding, kid. It's the maximum yield before catastrophic failure. Understand the spec.",
    "Gauge: This Annex only deals in grade-A salvage. If you want junk, go back to the Data Grave.",
    "Gauge: You look fragile. Every Scrapper thinks they're faster than the hit. You're not. Buy the armor.",
    "Gauge: The Foundry's heat warps metal, but it forges strength. My welds don't break.",
    "Gauge: Check your gait. Your armor is unbalanced. I can fix that stress point before it snaps.",
    "Gauge: They call it plating. I call it the acceptable margin of error between you and scrap.",
    "Gauge: I hate soft materials. I hate cheap alloys. If it ain't rated for heavy kinetic, it stays out of the shop.",
    "Gauge: Heard D-Corp sent a new wave of Sentinels toward the Perimeter. Time to upgrade your shoulder specs.",
    "Gauge: Don't worry about the cost. Worry about the crack in your sternum plating that ain't there yet.",
    "Gauge: My prices are fixed. Calculated based on material scarcity and the likelihood of your failure.",
    "Gauge: The best defense is redundancy. You got a primary shield and a secondary layer. Always.",
    "Gauge: That rattling noise? That's not the wind. That's a loose bolt. Fix it or pay the repair fee later.",
    "Gauge: You need armor that moves with you, not against you. Try this ferro-fluid liner.",
    "Gauge: I trust steel more than I trust most faces 'round here. And I only trust steel when I've checked the tensile strength myself."
]


def show_gauge_dialogue():
    print(random.choice(npc_dialogue))
    return