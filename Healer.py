from heroes_namur_gr_06 import *


def invigorate(positions, hero, player1, player2):
    """Raise the health points of the allies in the hero's wage.

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
    specification: Manon Michaux (v.3 05/05/19)
    implementation: Manon Michaux (v.4 05/05/19)
    """

    # If hero in player1
    if hero in player1:
        for heroes in positions:
            if heroes in player1:
                if gap_calculator(positions[hero], positions[heroes]) < 2:
                    player1[heroes]['life_points'] += 2
        # Adding the cooldown to the dictionary of the player if he attack has been used
        player1[hero]['cooldown'] += 1

    # If hero in player2
    if hero in player2:
        for heroes in positions:
            if heroes in player2:
                if gap_calculator(positions[hero], positions[heroes]) < 2:
                    player2[heroes]['life_points'] += 2
        # Adding the cooldown to the dictionary of the player if he attack has been used
        player2[hero]['cooldown'] += 1

    return positions, player1, player2


def immunise(positions, hero, player1, player2, coordinates):
    """Whenever a hero is immunised he's can't be attacked during this turn

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero: Name of the hero (str)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)
    coordinates: Where the special capacity 'immunise' is being used (tuple)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    player1: Level, number of point, etc. of the heroes of player 1 updated (dict)
    player2: Level, number of point, etc. of the heroes of player 2 updated (dict)

    Version:
    --------
    specification: Aude Lekeux (v.1 05/05/2019)
    implementation: Aude Lekeux (v.1 05/05/2019)
    """

    # If hero in player1
    if hero in player1:
        for heroes in positions:
            if positions[heroes] == coordinates:
                if heroes in player1:
                    print()
        # Adding the cooldown to the dictionary of the player if he attack has been used
        player1[hero]['cooldown'] += 1

    # If hero in player2
    if hero in player2:
        for heroes in positions:
            if positions[heroes] == coordinates:
                if heroes in player2:
                    print()
        # Adding the cooldown to the dictionary of the player if he attack has been used
        player2[hero]['cooldown'] += 1

    return positions, player1, player2
