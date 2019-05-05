def fulgura(positions, hero, player1, player2, creatures, coordinates):
    """ The creature/enemy on the target coordinates loses a given number of health points.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero: Name of the hero (str)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)
    creatures: Has every information of each creature (list)
    coordinates: Where the special capacity 'immunise' is being used (tuple)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    player1: Level, number of point, etc. of the heroes of player 1 updated (dict)
    player2: Level, number of point, etc. of the heroes of player 2 updated (dict)

    Version:
    --------
    specification: Manon Michaux (v.3 05/05/19)
    implementation: Manon Michaux (v.2 05/05/19)
    """

    # If hero in player1
    if hero in player1:
        for character in positions:
            if character in player2:
                if positions[character] == coordinates:
                    player2[character]['life_points'] -= 2
            elif positions[character][0] in creatures:
                if character == coordinates:
                    positions[character][1] -= 2
        # Adding the cooldown to the dictionary of the player if he attack has been used
        player1[hero]['cooldown'] += 1

    # If hero in player2
    if hero in player2:
        for character in positions:
            if character in player2:
                if positions[character] == coordinates:
                    player2[character]['life_points'] -= 2
            elif positions[character][0] in creatures:
                if character == coordinates:
                    positions[character][1] -= 2
        # Adding the cooldown to the dictionary of the player if he attack has been used
        player2[hero]['cooldown'] += 1

    return positions, player1, player2


def ovibus(positions, hero, player1, player2, creatures, coordinates):
    """The creature/enemy on the target coordinates is unable to act during a given number of turn.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero: Name of the hero (str)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)
    creatures: Has every information of each creature (list)
    coordinates: Where the special capacity 'ovibus' is being used (tuple)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    player1: Level, number of point, etc. of the heroes of player 1 updated (dict)
    player2: Level, number of point, etc. of the heroes of player 2 updated (dict)

    Version:
    --------
    specification: Manon Michaux (v.2 05/05/19)
    implementation: Manon Michaux (v.2 05/05/19)
    """

    # If hero in player1
    if hero in player1:
        for character in positions:
            if character in player2:
                if positions[character] == coordinates:
                    print()
            elif positions[character][0] in creatures:
                if character == coordinates:
                    print()
        # Adding the cooldown to the dictionary of the player if he attack has been used
        player1[hero]['cooldown'] += 1

    # If hero in player2
    if hero in player2:
        for character in positions:
            if character in player2:
                if positions[character] == coordinates:
                    print()
            elif positions[character][0] in creatures:
                if character == coordinates:
                    print()
        # Adding the cooldown to the dictionary of the player if he attack has been used
        player2[hero]['cooldown'] += 1

    return positions, player1, player2
