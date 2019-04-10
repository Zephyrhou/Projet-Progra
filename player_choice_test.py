def players_choice(choice, positions, player1, player2, creatures):
    """Translates the player's order and calls the functions move or attack.

    Parameters:
    -----------
    choice: Order of the player (str)
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of heroes of player1 (dict)
    player2: Level, number of point, etc. of heroes of player2 (dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated(dict)
    player1: Level, number of point, etc. of heroes of player1 updated (dict)
    player2: Level, number of point, etc. of heroes of player2 updated (dict)

    Notes:
    ------
    The order of the player must be with the expected format = 'hero_name:@r-c', 'hero_name:*r-c'
    or 'hero_name:capacity'.
    @ stands for a movement, * stands for a simple attack or 'capacity' is the name of a special capacity
    a hero wants to use.

    Version:
    --------
    specification: Zéphyr Houyoux (v.7 09/04/19)
    implementation: Zéphyr Houyoux (v.5 09/04/19)
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
            positions = move(positions, item, move_coordinates)
        elif result[item][0] == '*':
            attack_coordinates = (result[item][1:3], result[item][4:6])
            positions, player1, player2, creatures = attack(positions, item, '', (0, 0), attack_coordinates, player1, player2, creatures)
        else:
            if type(result[item]) is tuple:
                name_capacity = result[item][0]
                coordinates = (result[item][1][0:2], result[item][1][3:5])
                positions, player1, player2, creatures = attack(positions, item, name_capacity, coordinates, (0, 0), player1, player2, creatures)
            else:
                name_capacity = result[item]
                positions, player1, player2, creatures = attack(positions, item, name_capacity, (0, 0), (0, 0), player1, player2, creatures)

    return positions, player1, player2, creatures