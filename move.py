def move(dico_positions, movement, position_player):
    """Checks if the position he will end on is allowed. Do it if it is allowed.

    Parameters:
    -----------
    dico_positions: Contains all the coordinates of the board (dict)    movement: Coordinates the hero will go (str)
    movement: It is the positions that the heroe wants to go
    position_player: It is the positions of the player that want to move

    Returns:
    --------
    dico_positions: Contains the updated coordinates of the board (dict)

    Notes:
    ------
    It isn't allowed to move if there is already a hero or a creatures where you want to move.
    If the movement can't be done an error message is displayed and the movement is ignored.
    Movement can only be of one step in one of the eight directions.

    Version:
    --------
    specification: Zephyr Houyoux (v.4 25/03/19)
    implementation: Zephyr Houyoux (v.1 25/03/19)
    """
    possible = gap_calculator(dico_positions, movement, position_player)
    error_message = 'You can\'t move there'
    for things in dico_positions:
        iteration = str(things)
        if dico_positions[iteration]!=dico_positions['spur'] or dico_positions['spawn']!=dico_positions[iteration]:
            if dico_positions[iteration]['nb_rows']==dico_positions['movement']['nb_rows'] and dico_positions[iteration]['nb_columns']==dico_positions['movement']:
                print(error_message)
                return
            else:
                if possible < 1.5:
                    dico_positions[position_player] = dico_positions[movement]
                    return dico_positions
                else:
                    print(error_message)
                    return
        else:
                if possible < 1.5:
                    dico_positions[position_player] = dico_positions[movement]
                    return dico_positions
