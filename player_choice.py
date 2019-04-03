def players_choice(choice, dico_positions, dict_order, list_attack, dico_player, dico_creatures):
    """Translates the player's order into actions.

    Parameters:
    -----------
    choice: Order of the player (str)
    dico_positions: Contains all the coordinates of the board (dict)    dict_order: Contains the order of the player for this turn (dict)    list_attack: Contains all the special attack (dict)
    Returns:
    --------
    dico_positions: Contains all the coordinates of the board (dict)    dict_order: Contains the order of the player for this turn (dict)    Notes:
    ------
    The order of the player must be with the expected format = "hero_name : @r-c(movement) or *r-c(attack) "

    Version:
    --------
    specification: Zéphyr Houyoux (v.4 04/03/19)
    implementation: Zéphyr Houyoux (v.1 03/04/19)
    """
    dico_attack = choice.split(' ')
    result = {}
    tempory_dict = {}
    dict_order = {'arrack': {'order':(), 'name_attack':(), 'where':{'nb_rows':'','nb_columns':''}}, 'wolf': {'order':(), 'name_attack':(), 'where':{'nb_rows':'','nb_columns':''}}, 'fox': {'order':(), 'name_attack':(), 'where':{'nb_rows':'','nb_columns':''}}, 'brebi': {'order':(), 'name_attack':(), 'where':{'nb_rows':'','nb_columns':''}}}
    for x in range(len(dico_attack)):
        dico_indice = str(x)
        result[dico_indice] = dico_attack[x].split(':')
        if result[dico_indice][1] != result[dico_indice][-1]:
            name = result[dico_indice][0]
            action = result[dico_indice][1]
            pos = result[dico_indice][2]
            tempory_dict[name] = (action, pos)
        else:
            name = result[dico_indice][0]
            action = result[dico_indice][1]
            tempory_dict[name] = action
    for y in tempory_dict:
        if tempory_dict[y][0] == '@':
            dict_order[y]['order'] = 'move'
            dict_order[y]['where']['nb_rows'] = tempory_dict[y][1:].split('-')[0]
            dict_order[y]['where']['nb_columns'] = tempory_dict[y][1:].split('-')[1]
            dico_positions['movement'] = dict_order[y]['where']
            move(dico_positions, dico_positions['movement'], dico_positions[y])
        elif tempory_dict[y][0] == '*':
            dict_order[y]["order"] = 'attack'
            dict_order[y]["name_attack"] = 'basic'
            dict_order[y]['where']['nb_rows'] = tempory_dict[y][1:].split('-')[0]
            dict_order[y]['where']['nb_columns'] = tempory_dict[y][1:].split('-')[1]
            attack('basic', dict_order[y]['where']['nb_rows'], dict_order[y]['where']['nb_columns'], dico_player, dico_creatures)        else:
            dict_order[y]['order'] = 'attack'
            dict_order[y]['where']['nb_rows'] = tempory_dict[y][1].split('-')[0]
            dict_order[y]['where']['nb_columns'] = tempory_dict[y][1].split('-')[1]
            dict_order[y]['name_attack'] = tempory_dict[y][0]
            attack(dict_order[y]['name_attack'], dict_order[y]['where']['nb_rows'], dict_order[y]['where']['nb_columns'], dico_player, dico_creatures)
    return dico_positions, dico_player, dico_creatures
