def attack(positions, hero, capacity, attack, player):
    """Checks whether the hero can do the attack, if yes, does it, if no, the attack is ignored.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    player: All the data about heroes (dict)
    capacity: Name of the special capacity (str)
    attack: Where the attack is made (tuple)

    Returns:
    --------
    player: All the data about heroes (dict)
    creatures: All the data about creatures (dict)

    Notes:
    ------
    A hero can attack with a special capacity if he can, or he can do a simple attack.

    Version:
    --------
    specification: Zephyr Houyoux (v.3 04/03/19)
    implementation: Manon Michaux (v.1 07/04/19)
    """

    # If there's no capacity name then it's a simple attack
    # if capacity == '':
    #     if positions[attack] is not None:
    #         hero_class = get_class(hero, player)
    #         hero_level = get_level(hero, player)
    #         if hero_level == 1:
    #             if hero_class == 'barbarian':
    #                 positions[attack] =
    # # If there's no position to attack then it's a special capacity
    # elif attack == (0,0):


def get_class(hero, player):
    """Determines the class of a hero depending on his name

    Parameters:
    -----------
    hero:
    player:

    Returns:
    --------
    class:

    Version:
    --------
    specification:
    implementation:
    """

    for heroes in player:
        if hero == heroes:
            return player[heroes]['class']


def get_level(hero, player):
    """Determines the class of a hero depending on his name

    Parameters:
    -----------
    hero:
    player:

    Returns:
    --------
    class:

    Version:
    --------
    specification:
    implementation:
    """

    for heroes in player:
        if hero == heroes:
            return player[heroes]['level']


player1 = {'Baz': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'May': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

print(get_class('Lee', player1))
