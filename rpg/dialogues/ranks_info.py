from rpg.tools.keyboard_input_manager import wait_for_key

ranks = """
===================================================================================================
                                --- TITLE PROGRESSION OVERVIEW ---
===================================================================================================
| BATTLES | TITLE (STATUS)       | REPUTATION AND FUNCTION                                        |
---------------------------------------------------------------------------------------------------
| 0       | Scrap Initiate       | The lowest rung. Unregistered and untested, disposable to all.  |
| 1       | Green Tag            | A raw recruit, marked by inexperience and surviving by sheer luck.|
| 3       | Copper Grunt         | Possesses minimal combat knowledge. A low-level asset recognized |
|         |                      | only by the cheapest metallic ID tag.                          |
| 6       | Fringe Rat           | A survivalist who knows the hostile edges of the zone. Elusive |
|         |                      | and opportunistic, skilled at avoiding patrols.                |
| 11      | Drone Hunter         | Focus has sharpened; specializes in dismantling automated threats |
|         |                      | and securing low-risk components.                              |
| 21      | Junk Runner          | A reliable survivor and mover of critical salvage. Understands |
|         |                      | the dangerous routes in the outer wastes.                      |
| 35      | Data Cipher          | Possesses the tactical mind to exploit the programming flaws of  |
|         |                      | enemies. Strikes are precise and leverage vulnerabilities.     |
| 43      | Scrap Butcher        | A brutal close-quarters operative known for high-impact takedowns|
|         |                      | and leaving nothing but silence behind.                        |
| 50      | Ironclad Runner      | Endurance is feared. Able to withstand punishing damage and push |
|         |                      | through environmental toxins.                                  |
| 65      | Velocity Pilot       | A master of movement and combat efficiency. Strikes are optimized|
|         |                      | for speed and timing; a serious tactical threat.               |
| 81      | Circuit Breaker      | Has the skill to dismantle high-tier threats and cause system-wide|
|         |                      | damage. A recognized tactical superior.                        |
| 101     | Stormbound Master    | A figure of legend and fear. Has cleared the most difficult zones|
|         |                      | and possesses unmatched tactical knowledge.                    |
| 220+    | The Hardpoint Legend | The highest designation. A permanent, unpredictable error in the |
|         |                      | system, and the definitive survivor of the Data Grave.         |
---------------------------------------------------------------------------------------------------

[ Your rank is determined by how many Battles you won. That's how you prove you're worthy to survive in this world. ]
[ If you have a high rank, some enemies might respect you, or even invite you to their Faction. ]
[ And also some shops might give you discount on higher ranks. ]

"""

def show_rank_info():
    print(ranks)
    wait_for_key()

