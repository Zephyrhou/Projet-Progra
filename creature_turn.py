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
    implementation: Manon Michaux (v.5 25/04/19)
    """

    # For each creature if its next to a hero it attacks
    for creature in creatures:
        for key, value in positions.items():
            if value[0] == creature:
                for hero, position in positions.items():
                    if (hero in player1) or (hero in player2):
                        if gap_calculator(key, position) < 1.5:
                            print(key, value, hero, position, creature)
                            print(gap_calculator(key, position))
                            positions, player1, player2, creatures = attack(positions, creature, '', (0, 0), position,
                                                                            player1, player2, creatures)

    return positions, player1, player2


positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'), 'Lee': ('12', '20'),
             'May': ('24', '10'), 'Rob': ('10', '21'), 'Buf': ('9', '10'), 'Lia': ('10', '7'), 'Mey': ('3', '3'),
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

positions, player1, player2 = creature_turn(positions, creatures, player1, player2)

print(positions)
print(player1)
print(player2)
