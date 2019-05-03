from heroes_namur_gr_06 import *


def infighting(character, positions, player1, player2):
    """Verifies if a hero is next to another hero or a creature.

    Parameters:
    -----------
    character: Name of the character (str)
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)

    Returns:
    --------
    is_infighting: If a character is next to the hero or not (bool)
    character: Name of the character which is next to the hero (str)

    Version:
    --------
    specification: Aude Lekeux (v.2 03/05/2019)
    implementation: Aude Lekeux (v.2 03/05/2019)
    """

    for character, value in positions.items():
        if type(positions[character]) is tuple:
            if type(positions[character]) is tuple:
                if character in player1 and character in player2:
                    if gap_calculator(positions[character], positions[character]) < 2:
                        return True, character
                elif character in player2 and character in player1:
                    if gap_calculator(positions[character], positions[character]) < 2:
                        return True, character
        else:
            return False, ''


def ally_in_zone(hero, positions, player1, player2):
    """Verifies if an ally is in the zone of the hero.

    Parameters:
    -----------
    hero: Name of the hero (str)
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)

    Returns:
    --------
    is_ally_in_zone: If an ally is in the zone of the hero or not (bool)
    ally: Name of the ally which is in the zone of the hero (str)

    Version:
    --------
    specification: Aude Lekeux (v.1 03/05/2019)
    implementation: Aude Lekeux (v.1 03/05/2019)
    """

    for ally in positions:
        if hero in player1:
            if ally in player2:
                if gap_calculator(positions[hero], positions[ally]) > 2:
                    return True, ally
        elif hero in player2:
            if ally in player1:
                if gap_calculator(positions[hero], positions[ally]) > 2:
                    return True, ally


def enemy_in_zone(hero, positions, player1, player2):
    """Verifies is an enemy is in the zone of the hero.

    Parameters:
    -----------
    hero: Name of the hero (str)
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)

    Returns:
    --------
    is_enemy_in_zone: If an enemy in the zone of the hero or not (bool)
    enemy: Name of the enemy which is in the zone of the hero (str)

    Version:
    --------
    specification: Aude Lekeux (v.1 03/05/2019)
    implementation: Aude Lekeux (v.1 03/05/2019)
    """

    for enemy in positions:
        if hero in player1:
            if enemy in player2:
                if gap_calculator(positions[hero], positions[enemy]) > 2:
                    return True, enemy
        elif hero in player2:
            if enemy in player1:
                if gap_calculator(positions[hero], positions[enemy]) > 2:
                    return True, enemy


def move_towards(hero, position, positions):
    """A hero wants to move towards a certain position

    Parameters:
    -----------
    hero: Name of the hero (str)
    position: Position where to move to (tuple)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    new_value: New position on the hero (tuple)

    Notes:
    ------
    A hero can only move in one of the eight boxes around him

    Version:
    --------
    specification: Aude Lekeux (v.2 03/05/2019)
    implementation: Aude Lekeux (v.2 03/05/2019)
    """

    for key, value in positions.copy().items():
        if key == hero:
            if type(position) is tuple:
                x_hero = int(value[0])
                y_hero = int(value[1])
                x_position = int(position[0])
                y_position = int(position[1])
                previous_value = value
                value = list(previous_value)
                # The result will be positive, negative or zero
                if (x_hero - x_position) == 0:
                    # Moves y
                    if y_hero < y_position:
                        y_hero += 1
                        value[1] = str(y_hero)
                    elif y_hero > y_position:
                        y_hero -= 1
                        value[1] = str(y_hero)
                else:
                    # Moves x
                    if x_hero < x_position:
                        x_hero += 1
                        value[0] = str(x_hero)
                    elif x_hero > x_position:
                        x_hero -= 1
                        value[0] = str(x_hero)

            new_value = tuple(value)
            return new_value


def get_ia_orders(positions, player1, player2, nb_spur_p1, nb_spur_p2, nb_turns, creatures):
    """Decides what each hero will do.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)
    nb_spur_p1: Number of turns a hero from player 1 is on spur (int)
    nb_spur_p2: Number of turns a hero from player 2 is on spur (int)
    nb_turns: Number of turns played (int)
    creatures: Has every information of each creature (list)

    Returns:
    --------
    choice: Orders for each hero (str)

    Version:
    --------
    specification: Aude Lekeux (v.3 03/05/2019)
    implementation: Aude Lekeux (v.3 03/05/2019)
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
        if hero in player1 or hero in player2:
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
                is_infighting, character = infighting(hero, positions, player1, player2)
                if is_infighting:
                    if available_attack('stun', player, hero):
                        choice += ':stun '
                    ally_is_in_zone, ally = ally_in_zone(hero, positions, player1, player2)
                    if ally_is_in_zone:
                        if available_attack('energise', player, hero):
                            choice += ':energise '
                    else:
                        # If no special capacity is available; do a simple attack
                        for position in positions:
                            if type(positions[position]) is tuple:
                                if gap_calculator(positions[hero], positions[position]) < 2:
                                    if hero != position:
                                        choice += ':*' + positions[position][0] + '-' + positions[position][1] + ' '
                else:
                    if nb_turns >= 20:
                        if hero in player1:
                            if is_p1_on_spur:
                                # Do nothing
                                choice += ': '
                        elif hero in player2:
                            if is_p2_on_spur:
                                # Do nothing
                                choice += ': '
                        else:
                            # Move towards spur
                            for key, value in positions.items():
                                if value == 'spur':
                                    new_position = move_towards(hero, key, positions)
                                    choice += ':@' + new_position[0] + '-' + new_position[1] + ' '
                    else:
                        # Move towards enemy
                        all_gaps = {}
                        for key, value in positions.items():
                            if key not in player:
                                if type(value) is tuple:
                                    all_gaps[value] = round(gap_calculator(positions[hero], value), 2)

                        smallest_gap = min(all_gaps)
                        new_position = move_towards(hero, smallest_gap, positions)
                        choice += ':@' + new_position[0] + '-' + new_position[1] + ' '

            # If hero is a healer
            elif hero_class == 'healer':
                ally_is_in_zone, ally = ally_in_zone(hero, positions, player1, player2)
                if ally_is_in_zone:
                    enemy_is_in_zone, enemy = enemy_in_zone(hero, positions, player1, player2)
                    if enemy_is_in_zone:
                        if available_attack('immunise', player, hero):
                            choice += ':immunise' + positions[ally][0] + '-' + positions[ally][1] + ' '
                    elif available_attack('invigorate', player, hero):
                        choice += ':invigorate '
                enemy_is_in_zone, enemy = enemy_in_zone(hero, positions, player1, player2)
                if enemy_is_in_zone:
                    # If no special capacity is available; do a simple attack
                    choice += ':*' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                else:
                    if nb_turns >= 20:
                        if hero in player1:
                            if is_p1_on_spur:
                                # Do nothing
                                choice += ': '
                        elif hero in player2:
                            if is_p2_on_spur:
                                # Do nothing
                                choice += ': '
                        else:
                            # Move towards spur
                            for key, value in positions.items():
                                if value == 'spur':
                                    new_position = move_towards(hero, key, positions)
                                    choice += ':@' + new_position[0] + '-' + new_position[1] + ' '
                    else:
                        # Move towards enemy
                        all_gaps = {}
                        for key, value in positions.items():
                            if key not in player:
                                if type(value) is tuple:
                                    all_gaps[value] = round(gap_calculator(positions[hero], value), 2)

                        smallest_gap = min(all_gaps)
                        new_position = move_towards(hero, smallest_gap, positions)
                        choice += ':@' + new_position[0] + '-' + new_position[1] + ' '

            # If hero is a mage
            elif hero_class == 'mage':
                is_infighting, enemy = infighting(hero, positions, player1, player2)
                enemy_is_in_zone, enemy = enemy_in_zone(hero, positions, player1, player2)
                if is_infighting or enemy_is_in_zone:
                    if available_attack('ovibus', player, hero):
                        choice += ':ovibus' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                    elif available_attack('fulgura', player, hero):
                        choice += ':fulgura' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                    else:
                        # If no special capacity is available; do a simple attack
                        choice += ':*' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                elif nb_turns >= 20:
                    if hero in player1:
                        if is_p1_on_spur:
                            # Do nothing
                            choice += ': '
                    elif hero in player2:
                        if is_p2_on_spur:
                            # Do nothing
                            choice += ': '
                    else:
                        # Move towards spur
                        for key, value in positions.items():
                            if value == 'spur':
                                new_position = move_towards(hero, key, positions)
                                choice += ':@' + new_position[0] + '-' + new_position[1] + ' '
                else:
                    # Move towards enemy
                    all_gaps = {}
                    for key, value in positions.items():
                        if key not in player:
                            if type(value) is tuple:
                                all_gaps[value] = round(gap_calculator(positions[hero], value), 2)

                    smallest_gap = min(all_gaps)
                    new_position = move_towards(hero, smallest_gap, positions)
                    choice += ':@' + new_position[0] + '-' + new_position[1] + ' '

            # If hero is a rogue
            elif hero_class == 'rogue':
                is_infighting, enemy = infighting(hero, positions, player1, player2)
                enemy_is_in_zone, enemy = enemy_in_zone(hero, positions, player1, player2)
                if is_infighting or enemy_is_in_zone:
                    if available_attack('burst', player, hero):
                        choice += ':burst' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                    elif available_attack('reach', player, hero):
                        choice += ':reach' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                    else:
                        # If no special capacity is available; do a simple attack
                        choice += ':*' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                elif nb_turns >= 20:
                    if hero in player1:
                        if is_p1_on_spur:
                            # Do nothing
                            choice += ': '
                    elif hero in player2:
                        if is_p2_on_spur:
                            # Do nothing
                            choice += ': '
                    else:
                        # Move towards spur
                        for key, value in positions.items():
                            if value == 'spur':
                                new_position = move_towards(hero, key, positions)
                                choice += ':@' + new_position[0] + '-' + new_position[1] + ' '
                else:
                    # Move towards enemy
                    all_gaps = {}
                    for key, value in positions.items():
                        if key not in player:
                            if type(value) is tuple:
                                all_gaps[value] = round(gap_calculator(positions[hero], value), 2)

                    smallest_gap = min(all_gaps)
                    new_position = move_towards(hero, smallest_gap, positions)
                    choice += ':@' + new_position[0] + '-' + new_position[1] + ' '

    # Removes the last char which is a space
    choice = choice[0:-1]
    print(choice)
    positions, player1, player2, creatures = players_choice(choice, positions, player1, player2, creatures)

    return positions, player1, player2, creatures


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

player2 = {'Buf': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Lia': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Mey': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Tob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

nb_spur_p1 = 0
nb_spur_p2 = 0
nb_turns = 13

creatures = ['bear', 'bear', 'wolf']

positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'), 'Lee': ('24', '3'),
             'May': ('14', '6'), 'Rob': ('20', '17'), 'Buf': ('21', '18'), 'Lia': ('19', '7'), 'Mey': ('3', '3'),
             'Tob': ('2', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ['bear', '20', '5', '3', '100'],
             ('10', '20'): ['bear', '20', '5', '3', '100'], ('15', '10'): ['wolf', '10', '3', '2', '50']}

# print(available_attack('invigorate', player1, 'Lee'))
positions, player1, player2, creatures = get_ia_orders(positions, player1, player2, nb_spur_p1, nb_spur_p2, nb_turns,
                                                       creatures)
print(positions)
print(player1)
print(player2)
print(creatures)
