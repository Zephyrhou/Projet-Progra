from heroes_namur_gr_06 import *


def infighting(hero):
    """Verifies if a hero is next to another hero or a creature.

    Parameters:
    -----------
    hero: Name of the hero (str)

    Returns:
    --------
    is_infighting: If a character is next to the hero or not (bool)
    character: Name of the character which is next to the hero (str)

    Version:
    --------
    specification:
    implementation:
    """


def ally_in_zone(hero):
    """Verifies if an ally is in the zone of the hero.

    Parameters:
    -----------
    hero: Name of the hero (str)

    Returns:
    --------
    is_ally_in_zone: If an ally is in the zone of the hero or not (bool)
    ally: Name of the ally which is in the zone of the hero (str)

    Version:
    --------
    specification:
    implementation:
    """


def enemy_in_zone(hero):
    """Verifies is an enemy is in the zone of the hero.

    Parameters:
    -----------
    hero: Name of the hero (str)

    Returns:
    --------
    is_enemy_in_zone: If an enemy in the zone of the hero or not (bool)
    enemy: Name of the enemy which is in the zone of the hero (str)

    Version:
    --------
    specification:
    implementation:
    """


def spur_available():
    """Verifies if the spur is available or not.

    Returns:
    --------
    is_spur_available: If spur is available or not (bool)

    Notes:
    ------
    spur is only available after the 20 first turns of the game.

    Version:
    --------
    specification:
    implementation:
    """


def get_ia_orders(positions, player1, player2, nb_spur_p1, nb_spur_p2):
    """Decides what each hero will do.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)

    Returns:
    --------
    choice: Orders for each hero (str)

    Version:
    --------
    specification: Aude Lekeux (v.1 25/04/2019)
    implementation: Aude Lekeux (v.1 25/04/2019)
    """

    # Choice of the IA is built as you go
    choice = ''
    hero_class = ''
    player = ''

    # Verify if a hero is on spur (si_p1_on_spur and is_p2_on_spur are needed for the function)
    nb_spur_p1, nb_spur_p2, is_p1_on_spur, is_p2_on_spur = is_on_spur(nb_spur_p1, nb_spur_p2, player1, player2,
                                                                      positions)

    # Initialises the variables needed for the rest of the function
    for hero in positions:
        if hero in player1:
            hero_class = player1[hero]['class']
            player = player1
            choice += str(hero)
        elif hero in player2:
            hero_class = player2[hero]['class']
            player = player2
            choice += str(hero)

        # Depending on the class of the hero
        # If hero is a barbarian
        if hero_class == 'barbarian':
            if infighting(hero):
                if available_attack('stun', player, hero):
                    choice += ':stun '
                elif ally_in_zone(hero):
                    if available_attack('energise', player, hero):
                        choice += ':energise '
                else:
                    # If no special capacity if available; do a simple attack
                    choice += ':*'
            else:
                if spur_available():
                    if hero in player1:
                        if is_p1_on_spur:
                            # Do nothing
                            choice += ':@'
                    elif hero in player2:
                        if is_p2_on_spur:
                            # Do nothing
                            choice += ':@'
                    else:
                        # Move towards spur
                        choice += ':@'
                else:
                    # Move towards enemy
                    choice += ':@'

        # If hero is a healer
        elif hero_class == 'healer':
            if ally_in_zone(hero):
                if enemy_in_zone(hero):
                    if available_attack('immunise', player, hero):
                        choice += ':immunise '
                elif available_attack('invigorate', player, hero):
                    choice += ':invigorate '
            elif enemy_in_zone(hero):
                # If no special capacity if available; do a simple attack
                choice += ':*'
            else:
                if spur_available():
                    if hero in player1:
                        if is_p1_on_spur:
                            # Do nothing
                            choice += ':@'
                    elif hero in player2:
                        if is_p2_on_spur:
                            # Do nothing
                            choice += ':@'
                    else:
                        # Move towards spur
                        choice += ':@'
                else:
                    # Move towards enemy
                    choice += ':@'

        # If hero is a mage
        elif hero_class == 'mage':
            if infighting(hero) or enemy_in_zone(hero):
                if available_attack('ovibus', player, hero):
                    choice += ':ovibus '
                elif available_attack('fulgura', player, hero):
                    choice += ':fulgura '
                else:
                    # If no special capacity if available; do a simple attack
                    choice += ':*'
            elif spur_available():
                if hero in player1:
                    if is_p1_on_spur:
                        # Do nothing
                        choice += ':@'
                elif hero in player2:
                    if is_p2_on_spur:
                        # Do nothing
                        choice += ':@'
                else:
                    # Move towards spur
                    choice += ':@'
            else:
                # Move towards enemy
                choice += ':@'

        # If hero is a rogue
        elif hero_class == 'rogue':
            if infighting(hero) or enemy_in_zone(hero):
                if available_attack('burst', player, hero):
                    choice += ':burst '
                else:
                    # If no special capacity if available; do a simple attack
                    choice += ':*'
            elif available_attack('reach', player, hero):
                choice += ':reach '
            elif spur_available():
                if hero in player1:
                    if is_p1_on_spur:
                        # Do nothing
                        choice += ':@'
                elif hero in player2:
                    if is_p2_on_spur:
                        # Do nothing
                        choice += ':@'
                else:
                    # Move towards spur
                    choice += ':@'

    return choice


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
    implementation: Manon Michaux (v.2 26/04/19)
    """

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

    # # Cooldown ok ?
    # if used == 1:
    #     if good[hero_name][cooldown][name_attack] == 0:
    #         return True
    #     else:
    #         return False
    # else:
    #     return False


player1 = {'Baz': {'class': 'barbarian', 'level': 4, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'May': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

print(available_attack('energise', player1, 'Baz'))
