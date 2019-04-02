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

    # Level increase depending on the hero's victory points
    for hero in player:
        # If hero is under 100 victory points
        if player[hero]['victory_points'] < 100:
            print('Hero ' + hero + ' remains on level 1')
            player[hero]['level'] = 1
            player[hero]['life_points'] = 10
            player[hero]['damage_points'] = 2
        # If hero is over 100 points
        else:
            if player[hero]['class'] == 'barbarian':
                if player[hero]['victory_points'] < 200:
                    player[hero]['level'] = 2
                    player[hero]['life_points'] = 13
                    player[hero]['damage_points'] = 3
                elif player[hero]['victory_points'] < 400:
                    player[hero]['level'] = 3
                    player[hero]['life_points'] = 16
                    player[hero]['damage_points'] = 4
                elif player[hero]['victory_points'] < 800:
                    player[hero]['level'] = 4
                    player[hero]['life_points'] = 19
                    player[hero]['damage_points'] = 5
                elif player[hero]['victory_points'] > 800:
                    player[hero]['level'] = 5
                    player[hero]['life_points'] = 22
                    player[hero]['damage_points'] = 6
            elif player[hero]['class'] == 'healer':
                if player[hero]['victory_points'] < 200:
                    player[hero]['level'] = 2
                    player[hero]['life_points'] = 11
                    player[hero]['damage_points'] = 2
                elif player[hero]['victory_points'] < 400:
                    player[hero]['level'] = 3
                    player[hero]['life_points'] = 12
                    player[hero]['damage_points'] = 3
                elif player[hero]['victory_points'] < 800:
                    player[hero]['level'] = 4
                    player[hero]['life_points'] = 13
                    player[hero]['damage_points'] = 3
                elif player[hero]['victory_points'] > 800:
                    player[hero]['level'] = 5
                    player[hero]['life_points'] = 14
                    player[hero]['damage_points'] = 4
            elif player[hero]['class'] == 'mage':
                if player[hero]['victory_points'] < 200:
                    player[hero]['level'] = 2
                    player[hero]['life_points'] = 12
                    player[hero]['damage_points'] = 3
                elif player[hero]['victory_points'] < 400:
                    player[hero]['level'] = 3
                    player[hero]['life_points'] = 14
                    player[hero]['damage_points'] = 4
                elif player[hero]['victory_points'] < 800:
                    player[hero]['level'] = 4
                    player[hero]['life_points'] = 16
                    player[hero]['damage_points'] = 5
                elif player[hero]['victory_points'] > 800:
                    player[hero]['level'] = 5
                    player[hero]['life_points'] = 18
                    player[hero]['damage_points'] = 6
            elif player[hero]['class'] == 'rogue':
                if player[hero]['victory_points'] < 200:
                    player[hero]['level'] = 2
                    player[hero]['life_points'] = 12
                    player[hero]['damage_points'] = 3
                elif player[hero]['victory_points'] < 400:
                    player[hero]['level'] = 3
                    player[hero]['life_points'] = 14
                    player[hero]['damage_points'] = 4
                elif player[hero]['victory_points'] < 800:
                    player[hero]['level'] = 4
                    player[hero]['life_points'] = 16
                    player[hero]['damage_points'] = 5
                elif player[hero]['victory_points'] > 800:
                    player[hero]['level'] = 5
                    player[hero]['life_points'] = 18
                    player[hero]['damage_points'] = 6
            print('Hero ' + hero + ' has increased to level ' + str(player[hero]['level']))

    return player


player1 = {'Baz': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'May': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

print(player1)

player1 = {'Baz': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 506, 'damage_points': 2},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 101, 'damage_points': 2},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 99, 'damage_points': 2},
           'May': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 467, 'damage_points': 2}}

print(increase_level(player1))
print(player1)
