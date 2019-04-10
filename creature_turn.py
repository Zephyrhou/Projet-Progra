from heroes_namur_gr_06 import *


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
    correct_coord = 0

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


choice_creature = 'arrack:@30-31 wolf:@30-21 fox:*10-15'
positions, player1, player2 = creature_turn(positions, creatures, player1, player2)
