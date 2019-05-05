from heroes_namur_gr_06 import *


def reach(positions, hero, player1, player2, coordinates):
    """Teleports the hero using the attack if he is the first using reach this turn and if the target coordinates aren't occupied.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero: Name of the hero (str)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)
    coordinates: Where the hero wants to use ovibus (tuple)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    player1: Level, number of point, etc. of the heroes of player 1 updated (dict)
    player2: Level, number of point, etc. of the heroes of player 2 updated (dict)

    Version:
    --------
    specification: Manon Michaux (v.3 05/05/19)
    implementation: Manon Michaux (v.4 05/05/19)
    """

    for character in positions:
        if positions[character] == coordinates or character == coordinates:
            print('You cannot use reach there')
        else:
            positions[hero] = coordinates
            # Adding the cooldown to the dictionary of the player if he attack has been used
            if hero in player1:
                player1[hero]['cooldown'] += 1
            elif hero in player2:
                player2[hero]['cooldown'] += 1

    return positions, player1, player2


def burst(positions, hero, player1, player2, creatures):
    """The creatures/enemies in the hero's wage lose a given number of health points.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero: Name of the hero (str)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)
    creatures: Has every information of each creature (list)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    player1: Level, number of point, etc. of the heroes of player 1 updated (dict)
    player2: Level, number of point, etc. of the heroes of player 2 updated (dict)

    Version:
    --------
    specification: Manon Michaux (v.3 05/05/19)
    implementation: Manon Michaux (v.3 05/05/19)
    """

    # If hero in player1
    if hero in player1:
        for character in positions:
            if character in player2:
                if gap_calculator(positions[hero], positions[character]) < 2:
                    player2[character]['life_points'] -= 2
            elif positions[character][0] in creatures:
                if gap_calculator(character, positions(hero)) < 2:
                    positions[character][1] -= 2
        # Adding the cooldown to the dictionary of the player if the attack has been used
        player1[hero]['cooldown'] += 1

    # If hero in player2
    if hero in player2:
        for character in positions:
            if character in player1:
                if gap_calculator(positions[hero], positions[character]) < 2:
                    player1[character]['life_points'] -= 2
            elif positions[character][0] in creatures:
                if gap_calculator(character, positions(hero)) < 2:
                    positions[character][1] -= 2
        # Adding the cooldown to the dictionary of the player if the attack has been used
        player2[hero]['cooldown'] += 1

    return positions, player1, player2
