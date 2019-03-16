def defeated(player, creature):
    """Whenever a hero or a creature is defeated.

    Parameters:
    -----------
    player: Information on the player's defeated hero who will respawn (dict)
    creature: Information on the creature that dies (dict)

    Returns:
    --------
    player: Information on the player's defeated hero who will respawn (dict)
    position: Contains all the coordinates of the board (dict)

    Notes:
    ------
    A hero or a creature is defeated whenever their health points are at O or less.
    When a hero is defeated he respawns.
    When a creature is defeated it dies and it's victory points are distributed to the heroes around.

    Version:
    --------
    specification: Aude Lekeux (v.5 04/03/2019)
    implementation: Aude Lekeux (v.2 15/03/19)
    """