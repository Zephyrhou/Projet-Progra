def available_attack(name_attack, player, hero):
    """Checks whether the hero can or not use a special capacity

    Parameters:
    -----------
    name_attack: Name of the special capacity the hero wants to use (str)
    player: Level, number of point, etc. of heroes of the player (dict)
    hero: Name of the hero using a special capacity (str)

    Return:
    -------
    availability: Whether the hero can use the special capacity or not (bool)

    Notes:
    ------
    availability is true if the hero can use the special capacity and false otherwise.

    Version:
    --------
    specification: Manon Michaux (v.2 26/04/19)
    implementation: Manon Michaux (v.3 01/05/19)
    """

    # If player is on level 1 he can't use a special capacity yet
    if player[hero]['level'] < 2:
        return False

    # Checks whether the cool down is at 0 or not
    if player[hero]['cooldown'] != 0:
        return False

    # Checks whether the hero has a level high enough in order to use a special capacity
    if player[hero]['class'] == 'barbarian':
        if name_attack == 'energise':
            if player[hero]['level'] >= 2:
                return True
        elif name_attack == 'stun':
            if player[hero]['level'] >= 3:
                return True
        else:
            return False

    elif player[hero]['class'] == 'healer':
        if name_attack == 'invigorate':
            if player[hero]['level'] >= 2:
                return True
        elif name_attack == 'immunise':
            if player[hero]['level'] >= 3:
                return True
        else:
            return False

    elif player[hero]['class'] == 'mage':
        if name_attack == 'fulgura':
            if player[hero]['level'] >= 2:
                return True
        elif name_attack == 'ovibus':
            if player[hero]['level'] >= 3:
                return True
        else:
            return False

    elif player[hero]['class'] == 'rogue':
        if name_attack == 'reach':
            if player[hero]['level'] >= 2:
                return True
        elif name_attack == 'burst':
            if player[hero]['level'] >= 3:
                return True
        else:
            return False


player1 = {'Baz': {'class': 'barbarian', 'level': 4, 'life_points': 10, 'victory_points': 0, 'damage_points': 2,
                   'cooldown': 0},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2,
                   'cooldown': 0},
           'May': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2,
                   'cooldown': 0},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2,
                   'cooldown': 0}}

print(available_attack('energise', player1, 'Baz'))
