from heroes_namur_gr_06 import gap_calculator, attack


def creature_turn(positions, creatures, player1, player2):
    """Checks where a creature should attack or move depending on it's surrounding.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)   
    creatures: Has every information of each creature (list)
    player1: Level, number of point, etc. of heroes of player1 (dict)
    player2: Level, number of point, etc. of heroes of player2 (dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of heroes of player 1 (dict)
    player2: Level, number of point, etc. of heroes of player 2 (dict)

    Notes:
    ------
    A creature attacks or moves towards the closest enemy.
    It can also do nothing.

    Version:
    --------
    specification: Aude Lekeux (v.5 10/04/19)
    implementation: Manon Michaux (v.4 10/04/19)
    """

    smallest_gap = {}

    # Gap calculating for player 1
    for character in positions:
        if positions[character][0] in creatures:
            creature = character
            if character in player1:
                hero = character
                smallest_gap[hero][creature] = gap_calculator(positions[hero], creature)

    # Gap calculating for player 2
    for character in positions:
        if positions[character][0] in creatures:
            creature = character
            if character in player2:
                hero = character
                smallest_gap[hero][creature] = gap_calculator(positions[hero], creature)

    evil = []

    # Comparing the gap with each creature's wage
    for creature in creatures:
        for people in smallest_gap:
            evil.append(smallest_gap[people][creature])
        closest = evil.sort()
        for people in smallest_gap:
            if smallest_gap[people][creature] == closest[0]:
                target = people
                if smallest_gap[target] <= positions[creature][3]:
                    attack_coord = positions[target]
                    positions, player1, player2, creatures = attack(positions, creature, '', (0, 0), attack_coord,
                                                                    player1, player2, creatures)
                else:
                    for item in positions:
                        if gap_calculator(item, target) == (positions[creature][3] - 1):
                            positions, player1, player2, creatures = attack(positions, creature, '', (0, 0),
                                                                            item, player1, player2,
                                                                            creatures)

    return positions, player1, player2


positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'), 'Lee': ('24', '3'),
             'May': ('14', '6'), 'Rob': ('20', '17'), 'Buf': ('20', '17'), 'Lia': ('19', '7'), 'Mey': ('3', '3'),
             'Tob': ('2', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ['fox', '20', '5', '3', '100'],
             ('10', '20'): ['arrack', '20', '5', '3', '100'], ('15', '10'): ['wolf', '10', '3', '2', '50']}

player1 = {'Baz': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'May': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

player2 = {'Buf': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Lia': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Mey': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Tob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

creatures = ['arrack', 'wolf', 'fox']
choice_creature = 'arrack:@30-31 wolf:@30-21 fox:*10-15'

positions, player1, player2 = creature_turn(positions, creatures, player1, player2)
