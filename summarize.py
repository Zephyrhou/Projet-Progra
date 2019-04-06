from heroes_namur_gr_06 import *


def special_capacity(player, hero):
    """Whenever a hero reaches level 2 or 3 he can start using special capacities.

    Parameters:
    -----------
    player: Level, number of point, etc. of the heroes of player (dict)
    hero: Name of the hero who leveled up (str)

    Version:
    --------
    specification: Aude Lekeux (v.2 05/04/19)
    implementation: Aude Lekeux (v.2 05/04/19)
    """

    if player[hero]['level'] == 2:
        if player[hero]['class'] == 'barbarian':
            print('The hero ' + hero + ' can now use the capacity energise')
        if player[hero]['class'] == 'healer':
            print('The hero ' + hero + ' can now use the capacity invigorate')
        if player[hero]['class'] == 'mage':
            print('The hero ' + hero + ' can now use the capacity fulgura')
        if player[hero]['class'] == 'rogue':
            print('The hero ' + hero + ' can now use the capacity reach')

    if player[hero]['level'] == 3:
        if player[hero]['class'] == 'barbarian':
            print('The hero ' + hero + ' can now use the capacity stun')
        if player[hero]['class'] == 'healer':
            print('The hero ' + hero + ' can now use the capacity immunise')
        if player[hero]['class'] == 'mage':
            print('The hero ' + hero + ' can now use the capacity ovibus')
        if player[hero]['class'] == 'rogue':
            print('The hero ' + hero + ' can now use the capacity burst')


def summarize(player_1, initial_p1, player_2, initial_p2, nb_turns, nb_turns_player, initial_positions, positions, ROWS,
              COLUMNS):
    """Summarizes the state of the game.

    Parameters:
    -----------
    player_1: Level, number of point, etc. of heroes of player1 (dict)
    initial_p1: Level, number of point, etc. of heroes of player1 before changes (dict)
    player_2: Level, number of point, etc. of heroes of player2 (dict)
    initial_p2: Level, number of point, etc. of heroes of player2 before changes (dict)
    nb_turns: Number of turns of the game (int)
    nb_turns_player: Number of turns a hero of a player is on spur (int)
    initial_positions: Contains all the coordinates of the board before changes (dict)
    positions: Contains all the coordinates of the board (dict)
    ROWS: Number of rows of the board (int)
    COLUMNS: Number of columns of the board (int)

    Version:
    --------
    specification: Manon Michaux (v.4 06/04/19)
    implementation: Aude Lekeux (v.3 06/04/19)
    """

    for hero in positions:
        if positions[hero] != initial_positions[hero]:
            # Whenever a hero has been respawning
            for key, value in positions.copy().items():
                if positions[hero] == key:
                    print(hero + ' has been respawning to ' + str(key))

    # Whenever a hero leveled up he can use a special capacity
    for hero1 in player_1:
        if player_1[hero1]['level'] != initial_p1[hero1]['level']:
            special_capacity(player_1, hero1)
    for hero2 in player_2:
        if player_2[hero2]['level'] != initial_p2[hero2]['level']:
            special_capacity(player_2, hero2)

    print('Creatures = ' + str(creatures))
    print('Positions = ' + str(positions))
    print('Number of turns played = ' + str(nb_turns))
    print('Number of turns player is on spur = ' + str(nb_turns_player))
    display_board(ROWS, COLUMNS, positions)

    # Resets initial positions to positions
    initial_positions = positions
    # Resets the players to initial players
    initial_p1 = player1
    initial_p2 = player2

    return initial_positions, positions, initial_p1, initial_p2


initial_positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'),
                     'Lee': ('24', '3'), 'May': ('14', '6'), 'Rob': ('20', '17'), 'Buf': ('20', '17'),
                     'Lia': ('19', '7'), 'Mey': ('3', '3'), 'Tob': ('2', '37'), ('20', '38'): 'spur',
                     ('20', '39'): 'spur', ('21', '38'): 'spur', ('21', '39'): 'spur',
                     ('10', '10'): ['bear', '20', '5', '3', '100'], ('10', '20'): ['bear', '20', '5', '3', '100'],
                     ('15', '10'): ['wolf', '10', '3', '2', '50']}

positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'), 'Lee': ('24', '3'),
             'May': ('14', '6'), 'Rob': ('20', '24'), 'Buf': ('20', '17'), 'Lia': ('20', '37'), 'Mey': ('3', '3'),
             'Tob': ('6', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ['bear', '20', '5', '3', '100'],
             ('10', '20'): ['bear', '20', '5', '3', '100'], ('15', '10'): ['wolf', '10', '3', '2', '50']}

initial_creatures = ['bear', 'bear', 'wolf']

creatures = ['bear', 'wolf']

initial_p_1 = {'Baz': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
               'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
               'May': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
               'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

player1 = {'Baz': {'class': 'barbarian', 'level': 2, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'May': {'class': 'mage', 'level': 3, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

initial_p_2 = {'B': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
               'L': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
               'My': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
               'R': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

player2 = {'B': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'L': {'class': 'healer', 'level': 3, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'My': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'R': {'class': 'rogue', 'level': 2, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

nb_turns = 0
nb_turns_left = 0
ROWS = 27
COLUMNS = 40

initial_positions, positions, player1, player2 = summarize(player1, initial_p_1, player2, initial_p_2, nb_turns,
                                                           nb_turns_left, initial_positions, positions, ROWS, COLUMNS)
