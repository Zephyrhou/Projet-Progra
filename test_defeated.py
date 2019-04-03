def defeated(player, nb_player, positions, creatures):
    """Whenever a hero or a creature is defeated.

    Parameters:
    -----------
    player: Information on the player's defeated hero who will respawn (dict)
    nb_player: Number of the player whose hero is defeated (int)
    creatures: Information on the creature that dies (list)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    player: Information on the player's defeated hero who will respawn (dict)
    position: Contains all the coordinates of the board (dict)
    creatures: Information on the creature that dies (list)

    Notes:
    ------
    A hero or a creature is defeated whenever their health points are at O or less.
    When a hero is defeated he respawns.
    When a creature is defeated it dies and it's victory points are distributed to the heroes around.

    Version:
    --------
    specification: Aude Lekeux (v.6 03/04/19)
    implementation: Aude Lekeux (v.4 03/04/19)
    """

    # Respawn a hero when he's defeated
    for hero in player:
        if player[hero]['life_points'] <= 0:
            if nb_player == 1:
                for key in positions:
                    if positions[key] == 'spawn_player_1':
                        positions[hero] = key
            if nb_player == 2:
                for key in positions:
                    if positions[key] == 'spawn_player_2':
                        positions[hero] = key

            # Reset life points of the hero depending on his class and level
            if player[hero]['class'] == 'barbarian':
                if player[hero]['level'] == 1:
                    player[hero]['life_points'] = 10
                elif player[hero]['level'] == 2:
                    player[hero]['life_points'] = 13
                elif player[hero]['level'] == 3:
                    player[hero]['life_points'] = 16
                elif player[hero]['level'] == 4:
                    player[hero]['life_points'] = 19
                elif player[hero]['level'] == 5:
                    player[hero]['life_points'] = 22
            elif player[hero]['class'] == 'healer':
                if player[hero]['level'] == 1:
                    player[hero]['life_points'] = 10
                elif player[hero]['level'] == 2:
                    player[hero]['life_points'] = 11
                elif player[hero]['level'] == 3:
                    player[hero]['life_points'] = 12
                elif player[hero]['level'] == 4:
                    player[hero]['life_points'] = 13
                elif player[hero]['level'] == 5:
                    player[hero]['life_points'] = 14
            elif player[hero]['class'] == 'mage':
                if player[hero]['level'] == 1:
                    player[hero]['life_points'] = 10
                elif player[hero]['level'] == 2:
                    player[hero]['life_points'] = 12
                elif player[hero]['level'] == 3:
                    player[hero]['life_points'] = 14
                elif player[hero]['level'] == 4:
                    player[hero]['life_points'] = 16
                elif player[hero]['level'] == 5:
                    player[hero]['life_points'] = 18
            elif player[hero]['class'] == 'rogue':
                if player[hero]['level'] == 1:
                    player[hero]['life_points'] = 10
                elif player[hero]['level'] == 2:
                    player[hero]['life_points'] = 12
                elif player[hero]['level'] == 3:
                    player[hero]['life_points'] = 14
                elif player[hero]['level'] == 4:
                    player[hero]['life_points'] = 16
                elif player[hero]['level'] == 5:
                    player[hero]['life_points'] = 18
            print('The hero', hero, 'is respawning')

    # Delete a creature when it's defeated
    for key, value in positions.copy().items():
        if value[0] in creatures:
            if value[1] <= 0:
                del positions[key]
                del creatures[creatures.index(value[0])]
                print('The creature', value[0], 'is dead')

    return player, positions, creatures


positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '4'), 'Lee': ('20', '3'),
             'May': ('20', '3'), 'Rob': ('20', '3'), 'Buf': ('20', '37'), 'Lia': ('20', '37'), 'Mey': ('20', '37'),
             'Tob': ('20', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ('bear', 0, 5, 3, 100), ('10', '20'): ('bear', 10, 5, 3, 100),
             ('15', '10'): ('wolf', 10, 5, 3, 100)}

player1 = {'Baz': {'class': 'barbarian', 'level': 2, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'May': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

creatures = ['bear', 'bear', 'wolf']

player1 = {'Baz': {'class': 'barbarian', 'level': 2, 'life_points': 0, 'victory_points': 0, 'damage_points': 2},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'May': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}


player1, positions, creatures = defeated(player1, 1, positions, creatures)

print()
print(player1)
print()
print(positions)
print()
print(creatures)
