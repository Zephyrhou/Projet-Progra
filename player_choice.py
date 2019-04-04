def players_choice(choice, positions, order, attack, player, creatures):
    """Translates the player's order into actions.

    Parameters:
    -----------
    choice: Order of the player (str)
    positions: Contains all the coordinates of the board (dict)
    order: Contains the order of the player for this turn (dict)
    attack: Contains all the special attack (dict)
    player: Level, number of point, etc. of heroes of the player (dict)
    creatures: Has every information of each creature (list)

    Returns:
    --------
    positions: Contains all the coordinates of the board (dict)
    order: Contains the order of the player for this turn (dict)

    Notes:
    ------
    The order of the player must be with the expected format = "hero_name : @r-c(movement) or *r-c(attack) "

    Version:
    --------
    specification: Zéphyr Houyoux (v.4 04/03/19)
    implementation: Zéphyr Houyoux (v.1 03/04/19)
    """

    attack = choice.split(' ')
    result = {}
    temp = {}

    order = {'arrack': {'order': (), 'name_attack': (), 'where': {'nb_rows': '', 'nb_columns': ''}},
             'wolf': {'order': (), 'name_attack': (), 'where': {'nb_rows': '', 'nb_columns': ''}},
             'fox': {'order': (), 'name_attack': (), 'where': {'nb_rows': '', 'nb_columns': ''}},
             'brebi': {'order': (), 'name_attack': (), 'where': {'nb_rows': '', 'nb_columns': ''}}}

    for x in range(len(attack)):
        index = str(x)
        result[index] = attack[x].split(':')
        if result[index][1] != result[index][-1]:
            name = result[index][0]
            action = result[index][1]
            pos = result[index][2]
            temp[name] = (action, pos)
        else:
            name = result[index][0]
            action = result[index][1]
            temp[name] = action

    for y in temp:
        if temp[y][0] == '@':
            order[y]['order'] = 'move'
            order[y]['where']['nb_rows'] = temp[y][1:].split('-')[0]
            order[y]['where']['nb_columns'] = temp[y][1:].split('-')[1]
            positions['movement'] = order[y]['where']
            move(positions, positions['movement'], positions[y])
        elif temp[y][0] == '*':
            order[y]["order"] = 'attack'
            order[y]["name_attack"] = 'basic'
            order[y]['where']['nb_rows'] = temp[y][1:].split('-')[0]
            order[y]['where']['nb_columns'] = temp[y][1:].split('-')[1]
            attack('basic', order[y]['where']['nb_rows'], order[y]['where']['nb_columns'], player, creatures)
        else:
            order[y]['order'] = 'attack'
            order[y]['where']['nb_rows'] = temp[y][1].split('-')[0]
            order[y]['where']['nb_columns'] = temp[y][1].split('-')[1]
            order[y]['name_attack'] = temp[y][0]
            attack(order[y]['name_attack'], order[y]['where']['nb_rows'], order[y]['where']['nb_columns'],
                   player, creatures)

    return positions, player, creatures
