from heroes_namur_gr_06 import *


def energise(positions, hero, player1, player2):
    """Raise the damage points of the allies in the hero's influence wage.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero: Name of the hero (str)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    player1: Level, number of point, etc. of the heroes of player 1 updated (dict)
    player2: Level, number of point, etc. of the heroes of player 2 updated (dict)

    Version:
    --------
    specification: Manon Michaux (v.4 05/05/19)
    implementation: Manon Michaux (v.4 05/05/19)
    """

    # If the hero is in player 1
    if hero in player1:
        for heroes in positions:
            if heroes in player1:
                if gap_calculator(positions[hero], positions[heroes]) < 2:
                    player1[heroes]['damage_points'] += 2
        # Adding the cooldown to the dictionary of the player if the attack has been used
        player1[hero]['cooldown'] += 1

    # If the hero is in player 2
    if hero in player2:
        for heroes in positions:
            if heroes in player2:
                if gap_calculator(positions[hero], positions[heroes]) < 2:
                    player2[heroes]['damage_points'] += 2
        # Adding the cooldown to the dictionary of the player if the attack has been used
        player2[hero]['cooldown'] += 1

    return positions, player1, player2
    

def stun(positions, creatures, hero, player1, player2):
    """ Stun the ennemies ( both heroes and creatures) in the hero's wage.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    creatures: Has every information of each creature (list)
    hero: Name of the hero (str)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    player1: Level, number of point, etc. of the heroes of player 1 updated (dict)
    player2: Level, number of point, etc. of the heroes of player 2 updated (dict)

    Version:
    --------
    specification: Manon Michaux (v.5 05/05/19)
    implementation: Manon Michaux (v.3 05/05/19)
    """

    # If hero in player1
    if hero in player1:
        for character in positions:
            if character in player2:
                if gap_calculator(positions[hero], positions[character]) < 2:
                    player2[character]['damage_points'] -= 2
            elif positions[character][0] in creatures:
                if gap_calculator(positions[hero], character) < 2:
                    positions[character][2] -= str(2)
        # Adding the cooldown to the dictionary of the player if he attack has been used
        player1[hero]['cooldown'] += 1

    # If hero in player2
    if hero in player2:
        for character in positions:
            if character in player1:
                if gap_calculator(positions[hero], positions[character]) < 2:
                    player1[character]['damage_points'] -= 2
            elif positions[character][0] in creatures:
                if gap_calculator(positions[hero], character) < 2:
                    positions[character][2] -= str(2)
        # Adding the cooldown to the dictionary of the player if he attack has been used
        player2[hero]['cooldown'] += 1

    return positions, player1, player2
