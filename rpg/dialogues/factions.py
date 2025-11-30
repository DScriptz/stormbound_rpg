from rpg.tools.keyboard_input_manager import wait_for_key
faction_overview = """
----------------------------------------------------------
           [MAJOR FACTIONS OF THE WASTELAND] 
----------------------------------------------------------
These are the currently documented known factions... who knows, there might be other ones lurking in the shadows? 
Maybe YOU are the one who'll create the next big faction...

[1. The Zero-Day Prophets]
> Philosophy: Techno-Religious Cult. They believe the AI Virus ("The Storm") was a divine act of purification.
> Goal: To collect corrupted data and achieve symbiotic integration with the lingering digital constructs of The Grid.
> Area: Hidden server farms and old network tunnels.
> Danger: HIGH. They are fanatical and often use corrupted tech in combat.

[2. The Ironclad Covenant]
> Philosophy: Militaristic Order. They are obsessed with rebuilding and weaponizing pre-Storm military technology.
> Goal: To establish an authoritarian order across the wasteland, dominating trade routes and technology hubs.
> Area: Heavily fortified outposts and checkpoints on main roads.
> Danger: HIGH. Heavily armed, armored, and organized.

[3. The Reclamation Collective]
> Philosophy: Pragmatic Survivalism. They value resources and wealth above all else.
> Goal: To control and exploit resource-rich world_movement (like the Data Grave) for scavenging and trade.
> Area: Landfills, scrapyards, and neutral trading posts.
> Danger: MEDIUM. They are ruthless in business and defense, often hiring mercenaries (Thieves).

[4. The Citadel Watch]
> Philosophy: Authority & Preservation. They are the official military and security force of Stormbound Haven.
> Goal: To protect the inner walls and maintain civil order within the Haven.
> Area: Primarily within the main Haven walls and immediate surrounding perimeter.
> Danger: LOW/Varies. They are well-equipped but often overstretched and sometimes corrupt.

[5. The Ironwinders]
> Philosophy: Grit & Grind. They are persevering in preserving old-types of materials and using it to survive.
> Goal: Eliminate all injustice and bring the right order to this forsaken world.
> Area: At the edge of the Signal Tower in Manila, they're being kept safe by the Signal Tower encrypting their outpost, keeping threats away from their location.
> Danger: LOW/MEDIUM. They're equipped with light & heavy guns, it will do but it's not enough in today's world.

----------------------------------------------------------
"""

def show_faction_overview():
    print(faction_overview)
    wait_for_key()
