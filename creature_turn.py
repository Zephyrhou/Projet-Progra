from heroes_namur_gr_06 import gap_calculator, attack, move


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
    implementation: Manon Michaux (v.6 29/04/19)
    """

    all_gaps = {}
    creature = ''

    for creature in creatures:
        for key, value in positions.items():
            if value[0] == creature:
                for hero, position in positions.items():
                    if (hero in player1) or (hero in player2):
                        gap = gap_calculator(key, position)
                        # If a hero is next to a creature it attacks
                        if gap < int(value[3]):
                            positions, player1, player2, creatures = attack(positions, creature, '', (0, 0), position,
                                                                            player1, player2, creatures)
                        # If no hero is in its influence zone
                        else:
                            all_gaps[hero] = round(gap, 2)

    # If a creature can't attack it moves towards the closest hero
    smallest_gap = min(all_gaps)
    positions = move(positions, creature, positions[smallest_gap], player1, player2, creatures)

    return positions, player1, player2


positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('12', '20'), 'Lee': ('10', '3'),
             'May': ('24', '10'), 'Rob': ('10', '21'), 'Buf': ('9', '10'), 'Lia': ('10', '7'), 'Mey': ('3', '3'),
             'Tob': ('2', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ['fox', '20', '3', '5', '100'],
             ('10', '20'): ['arrack', '20', '5', '2', '100'], ('15', '10'): ['wolf', '10', '4', '2', '50']}

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

print('po', positions)
print(player1)
print(player2)
