def increase_level(player):
    """Checks if a hero can level up and upgrade their characteristics.

    Parameters:
    -----------
    player: All the data about the heroes (dict)

    Returns:
    --------
    player: Updated data about the heroes (dict)

    Version:
    --------
    specification: Manon Michaux (v.3 04/03/19)
    implementation: Aude Lekeux (v.3 02/04/19)
    """

    # level upgrade depending on the hero's victory points
    for hero in player:
        if hero['class'] == 'barbarian':
            if hero['victory_points'] < 200:
                hero['level'] = 2
                hero['life_points'] = 13
                hero['damage_points'] = 3
            if hero['victory_points'] < 400:
                hero['level'] = 3
                hero['life_points'] = 16
                hero['damage_points'] = 4
            if hero['victory_points'] < 800:
                hero['level'] = 4
                hero['life_points'] = 19
                hero['damage_points'] = 5
            if hero['victory_points'] > 800:
                hero['level'] = 5
                hero['life_points'] = 22
                hero['damage_points'] = 6
        if hero['class'] == 'healer':
            if hero['victory_points'] < 200:
                hero['level'] = 2
                hero['life_points'] = 11
                hero['damage_points'] = 2
            if hero['victory_points'] < 400:
                hero['level'] = 3
                hero['life_points'] = 12
                hero['damage_points'] = 3
            if hero['victory_points'] < 800:
                hero['level'] = 4
                hero['life_points'] = 13
                hero['damage_points'] = 3
            if hero['victory_points'] > 800:
                hero['level'] = 5
                hero['life_points'] = 14
                hero['damage_points'] = 4
        if hero['class'] == 'mage':
            if hero['victory_points'] < 200:
                hero['level'] = 2
                hero['life_points'] = 12
                hero['damage_points'] = 3
            if hero['victory_points'] < 400:
                hero['level'] = 3
                hero['life_points'] = 14
                hero['damage_points'] = 4
            if hero['victory_points'] < 800:
                hero['level'] = 4
                hero['life_points'] = 16
                hero['damage_points'] = 5
            if hero['victory_points'] > 800:
                hero['level'] = 5
                hero['life_points'] = 18
                hero['damage_points'] = 6
        if hero['class'] == 'rogue':
            if hero['victory_points'] < 200:
                hero['level'] = 2
                hero['life_points'] = 12
                hero['damage_points'] = 3
            if hero['victory_points'] < 400:
                hero['level'] = 3
                hero['life_points'] = 14
                hero['damage_points'] = 4
            if hero['victory_points'] < 800:
                hero['level'] = 4
                hero['life_points'] = 16
                hero['damage_points'] = 5
            if hero['victory_points'] > 800:
                hero['level'] = 5
                hero['life_points'] = 18
                hero['damage_points'] = 6
        print('Hero', hero, 'has increased to level', hero['level'])


classes = {'barbarian': {'energise': [[1, 1, 1], [2, 1, 1], [3, 2, 1], [4, 2, 1]],
                         'stun': [[1, 1, 1], [2, 2, 2], [3, 3, 1]]},
           'healer': {'invigorate': [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]],
                      'immunise': [[1, 0, 1], [2, 0, 3], [3, 0, 3]]},
           'mage': {'fulgura': [[1, 3, 1], [2, 3, 1], [3, 4, 1], [4, 4, 1]],
                    'ovibus': [[1, 1, 3], [2, 2, 3], [3, 2, 3]]},
           'rogue': {'reach': [[1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1]],
                     'brust': [[1, 1, 1], [2, 2, 1], [3, 3, 1]]}}

player1 = {'Baz': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'May': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

level = {'barbarian': [[2, 100, 13, 3], [3, 200, 16, 4], [4, 400, 19, 5], [5, 800, 22, 6]],
         'healer': [[2, 100, 11, 2], [3, 200, 12, 3], [4, 400, 13, 3], [5, 800, 14, 4]],
         'mage': [[2, 100, 12, 3], [3, 200, 14, 4], [4, 400, 16, 5], [5, 800, 18, 6]],
         'rogue': [[2, 100, 12, 3], [3, 200, 14, 4], [4, 400, 16, 5], [5, 800, 18, 6]]}

print(increase_level(player1))
