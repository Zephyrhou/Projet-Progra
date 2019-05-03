from heroes_namur_gr_06 import *


def cac(positions, character):
    """Check if there is something in melee.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    character: Name of the character that you want to know if he is near an other player

    Returns:
    --------
    If there is a heroe or a creature in melee (bool)
    melee: all the character in melee (list)

    Versions:
    ---------
    specification:
    implementation:
    """

    infighting = []
    for position in positions:
        if position != character:
            if gap_calculator(position, character) < 2:
                infighting.append(character)
    if not infighting:
        return 0, infighting
    else:
        return 1, infighting
