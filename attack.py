from heroes_namur_gr_06 import *
from Barbarian import *
from Healer import *
from Mage import *
from Rogue import *


def attack(positions, hero, capacity, coordinates, attack, player1, player2, creatures):
    """Checks whether the hero can do the attack, if yes, does it, if no, the attack is ignored.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero: Name of the hero wanting to attack (str)
    coordinates: Coordinates where the hero wants to use his special capacity (tuple)
    capacity: Name of the special capacity (str)
    attack: Where the attack is made (tuple)
    player1: All the data about heroes of player1 (dict)
    player2: All the data about heroes of player2 (dict)
    creatures:

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    player1: All the data about heroes of player1 updated (dict)
    player2: All the data about heroes of player2 updated (dict)


    Notes:
    ------
    A hero can attack with a special capacity if he's on a level high enough, or he can do a simple attack.

    Version:
    --------
    specification: Zephyr Houyoux (v.5 09/04/19)
    implementation: Manon Michaux (v.3 09/04/19)
    """

    # If there's no capacity name then it's a simple attack
    if capacity == '':
        for key in positions:

            # If the hero attacks another hero
            if positions[key] == attack:
                if key in player1:
                    player1[key]['life_points'] -= player2[hero]['damage_points']
                elif key in player2:
                    player2[key]['life_points'] -= player1[hero]['damage_points']
                print('Hero', hero, 'has attacked', key)
                return positions, player1, player2

            # If the hero attacks a creature
            elif key == attack:
                if hero in player1:
                    # If the creature has enough life points left
                    if int(positions[key][1]) > player1[hero]['damage_points']:
                        positions[key][1] = int(positions[key][1]) - player1[hero]['damage_points']

                elif hero in player2:
                    if int(positions[key][1]) > player2[hero]['damage_points']:
                        positions[key][1] = int(positions[key][1]) - player2[hero]['damage_points']

                print('Hero', hero, 'has attacked', positions[key][0])

    # If there's no position to attack then it's a special capacity
    elif attack == (0, 0):

        if hero in player1:
            hero_class = get_class(hero, player1)
            hero_level = get_level(hero, player1)
        elif hero in player2:
            hero_class = get_class(hero, player2)
            hero_level = get_level(hero, player2)

        # If hero is on level 1 he can't use a special capacity yet
        if hero_level == 1:
            print('You cannot use a special capacity yet')
            return positions, player1, player2
        else:
            # If hero on level 2 to 5 he can use a special capacity
            for level in range(2, 6):
                positions = special_capacity_usage(positions, hero, player, hero_level, hero_class, capacity, coordinates)
                return positions, player1, player2

    return positions, player1, player2, creatures


def special_capacity_usage(positions, hero, player, hero_level, hero_class, capacity, coordinates):
    """Verifies if a gero can use a special capacity or not.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero: Name of the hero wanting to use a special capacity (str)
    player: All the data about heroes of the player (dict)
    hero_level: Level of the hero wanting to use a special capacity (int)
    hero_class: Class of the hero wanting to use a special capacity (str)
    capacity: Name of the special capacity (str)
    coordinates: Coordinates where the hero wants to use his special capacity (tuple)

    Notes:
    ------
    Not every special capacity needs coordinates.
    Only immunise, fulgura, ovibus and reach need coordinates.

    Version:
    --------
    specification: Aude Lekeux (v.1 08/04/19)
    implementation: Aude Lekeux (v.1 08/04/19)
    """

    # If the hero is on level 2 he can only use one of his special capacity yet
    if hero_level == 2:
        # If the hero is a barbarian he can only use energise
        if hero_class == 'barbarian':
            if capacity != 'energise':
                print('You cannot use the capacity ' + capacity)
                return positions
            else:
                positions = energise(positions, hero, player)
                return positions

        # If the hero is a healer he can only use invigorate
        elif hero_class == 'healer':
            if capacity != 'invigorate':
                print('You cannot use the capacity ' + capacity)
                return positions
            else:
                positions = invigorate(positions, hero, player)
                return positions

        # If the hero is a mage he can only use fulgura
        elif hero_class == 'mage':
            if capacity != 'fulgura':
                print('You cannot use the capacity ' + capacity)
                return positions
            else:
                positions = fulgura(coordinates, positions, hero, player)
                return positions

        # If the hero is a rogue he can only use reach
        elif hero_class == 'rogue':
            if capacity != 'reach':
                print('You cannot use the capacity ' + capacity)
                return positions
            else:
                positions = reach(positions, hero, coordinates)
                return positions

    # If the hero is on level 3 or more he can use both of his special capacities
    elif hero_level >= 3:
        # Barbarian can use energise and stun
        if hero_class == 'barbarian':
            if capacity == 'energise':
                positions = energise(positions, hero, player)
                return positions
            elif capacity == 'stun':
                positions = stun(positions, player, creatures, hero)
                return positions

        # Healer can use invigorate and immunise
        elif hero_class == 'healer':
            if capacity == 'invigorate':
                positions = invigorate(positions, hero, player)
                return positions
            elif capacity == 'immunise':
                positions = immunise(positions, player, creatures, hero, coordinates)
                return positions

        # Mage can use fulgura and ovibus
        elif hero_class == 'mage':
            if capacity == 'fulgura':
                positions = fulgura(coordinates, positions, hero, player)
                return positions
            elif capacity == 'ovibus':
                positions = ovibus(positions, hero, coordinates, creatures)
                return positions

        # Rogue can use reach and burst
        elif hero_class == 'rogue':
            if capacity == 'reach':
                positions = reach(positions, hero, coordinates)
                return positions
            elif capacity == 'burst':
                positions = burst(positions, hero, creatures)
                return positions


player1 = {'Baz': {'class': 'barbarian', 'level': 2, 'life_points': 13, 'victory_points': 100, 'damage_points': 3},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'May': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

player2 = {'Buf': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Lia': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Mey': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Tob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'), 'Lee': ('24', '3'),
             'May': ('14', '6'), 'Rob': ('20', '17'), 'Buf': ('20', '16'), 'Lia': ('19', '7'), 'Mey': ('3', '3'),
             'Tob': ('2', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ['bear', '20', '5', '3', '100'],
             ('10', '20'): ['bear', '3', '5', '3', '100'], ('15', '10'): ['wolf', '10', '3', '2', '50']}

creatures = ['bear', 'bear', 'wolf']

positions, player1, player2, creatures = attack(positions, 'Baz', '', (0, 0), ('10', '20'), player1, player2, creatures)
print(positions)
player1, positions, creatures = defeated(player1, 1, positions, creatures)

print(positions)
print(creatures)
