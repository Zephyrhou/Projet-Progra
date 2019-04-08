def is_cell_empty(cell, positions):
    """Checks whether the cell is empty or not

    Parameters:
    -----------
    cell: Position of the cell (tuple)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    cell_empty: If the cell is empty or not (bool)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    cell_empty = True

    for item in positions:
        if cell == item or cell == positions[item]:
            cell_empty = False

    return cell_empty


def get_class(hero, player):
    """Determines the class of a hero depending on his name

    Parameters:
    -----------
    hero: Name of the hero (str)
    player: All the data about heroes (dict)

    Returns:
    --------
    class: Class of the hero (str)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    for heroes in player:
        if hero == heroes:
            return player[heroes]['class']


def get_level(hero, player):
    """Determines the class of a hero depending on his name

    Parameters:
    -----------
    hero: Name of the hero (str)
    player: All the data about heroes (dict)

    Returns:
    --------
    level: Level of the hero (int)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    for heroes in player:
        if hero == heroes:
            return player[heroes]['level']


def get_life_points(hero, player):
    """Determines the class of a hero depending on his name

    Parameters:
    -----------
    hero: Name of the hero (str)
    player: All the data about heroes (dict)

    Returns:
    --------
    life_points: Life points of the hero (int)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    for heroes in player:
        if hero == heroes:
            return player[heroes]['life_points']


def get_victory_points(hero, player):
    """Determines the class of a hero depending on his name

    Parameters:
    -----------
    hero: Name of the hero (str)
    player: All the data about heroes (dict)

    Returns:
    --------
    victory_points: Victory points of the hero (int)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    for heroes in player:
        if hero == heroes:
            return player[heroes]['victory_points']


def get_damage_points(hero, player):
    """Determines the class of a hero depending on his name

    Parameters:
    -----------
    hero: Name of the hero (str)
    player: All the data about heroes (dict)

    Returns:
    --------
    damage_points: Damage points of the hero (int)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    for heroes in player:
        if hero == heroes:
            return player[heroes]['damage_points']


def is_on_spur(hero, positions):
    """Checks whether a hero is on spur.

    Parameters:
    -----------
    hero: Name of the heo (str)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    on_spur: If the hero is on spur or not (bool)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    for item in positions:
        if positions[item] == 'spur':
            if positions[hero] == item:
                return True
    return False


def move_cell(character, start, new_position, positions, creatures):
    """Move from one cell to another.

    Parameters:
    -----------
    character: Either the name of a hero or of a creature (str)
    start: Position the character is on now (tuple)
    finish: Position the character wants to go on (tuple)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)

    Notes:
    ------
    This function is called only when the movement can be executed.

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    if character in positions:
        positions[character] = new_position

    elif character in creatures:
        for key, value in positions.copy().items():
            if key == start:
                # Adds the new position and deletes the previous one
                positions[new_position] = positions[key]
                del positions[key]

    return positions


player1 = {'Baz': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'May': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'), 'Lee': ('24', '3'),
             'May': ('14', '6'), 'Rob': ('23', '38'), 'Buf': ('20', '17'), 'Lia': ('19', '7'), 'Mey': ('3', '3'),
             'Tob': ('2', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ['bear', '20', '5', '3', '100'],
             ('10', '20'): ['bear', '20', '5', '3', '100'], ('15', '10'): ['wolf', '10', '3', '2', '50']}

creatures = ['bear', 'bear', 'wolf']

print(is_on_spur('Rob', positions))
# print(move_cell('bear', ('10', '20'), ('5', '7'), positions, creatures))
