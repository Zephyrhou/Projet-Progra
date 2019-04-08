from heroes_namur_gr_06 import *


def players_choice(choice, positions, player):
    """Translates the player's order and calls the functions move or attack.

    Parameters:
    -----------
    choice: Order of the player (str)
    positions: Contains all the coordinates of the board (dict)

    Notes:
    ------
    The order of the player must be with the expected format = 'hero_name:@r-c', 'hero_name:*r-c'
    or 'hero_name:capacity'.
    @ stands for a movement, * stands for a simple attack or 'capacity' is the name of a special capacity
    a hero wants to use.

    Version:
    --------
    specification: Zéphyr Houyoux (v.6 07/04/19)
    implementation: Zéphyr Houyoux (v.3 07/04/19)
    """

    choice = choice.split(' ')
    temp = []
    result = {}

    for items in choice:
        temp += items.split(':')

    # Puts the input of the player in a dictionary
    for index in range(len(choice)):
        temp[index] = choice[index].split(':')
        if temp[index][1] != temp[index][-1]:
            name = temp[index][0]
            action = temp[index][1]
            pos = temp[index][2]
            result[name] = (action, pos)
        else:
            name = temp[index][0]
            action = temp[index][1]
            result[name] = action

    # Reads the dictionary and calls the right function (move or attack)
    for item in result:
        if result[item][0] == '@':
            move_coordinates = (result[item][1:3], result[item][4:6])
            move(positions, item, move_coordinates)
        elif result[item][0] == '*':
            attack_coordinates = (result[item][1:3], result[item][4:6])
            attack(positions, item, '', (0, 0), attack_coordinates, player)
        else:
            if type(result[item]) is tuple:
                name_capacity = result[item][0]
                coordinates = (result[item][1][0:2], result[item][1][3:5])
                attack(positions, item, name_capacity, coordinates, (0, 0), player)
            else:
                name_capacity = result[item]
                attack(positions, item, name_capacity, (0, 0), (0, 0), player)


player1 = {'Baz': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'May': {'class': 'mage', 'level': 2, 'life_points': 12, 'victory_points': 100, 'damage_points': 3},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'), 'Lee': ('24', '3'),
             'May': ('14', '6'), 'Rob': ('20', '17'), 'Buf': ('20', '17'), 'Lia': ('19', '7'), 'Mey': ('3', '3'),
             'Tob': ('2', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ['bear', '20', '5', '3', '100'],
             ('10', '20'): ['bear', '20', '5', '3', '100'], ('15', '10'): ['wolf', '10', '3', '2', '50']}

choices = 'Baz:@30-31 Lee:invigorate May:fulgura:10-10 Rob:*10-15'

players_choice(choices, positions, player1)

