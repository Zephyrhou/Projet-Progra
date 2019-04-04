def get_content(positions, row, column):
    """Get what character to print depending on what is on the position (row, column)

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    row: Row of the character looked for (int)
    column: Column f the character looked for (int)

    Returns:
    --------
    character: Character to be printed in the board (str)

    Version:
    --------
    specification: Aude Lekeux (v.1 1/04/19)
    implementation: Aude Lekeux (v.3 2/04/19)
    """

    row = str(row)
    column = str(column)

    for key in positions:
        if key == (row, column):
            if type(positions[key]) == list:
                return positions[key][0]
            else:
                return positions[key]
        elif positions[key] == (row, column):
            return key


def display_board(positions, nb_rows, nb_columns):
    """Displays the board.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)

    Version:
    --------
    specification: Manon Michaux (v.2 25/02/19)
    implementation: Aude Lekeux (v.6 2/04/19)
    """

    for row in range(nb_rows):
        display_line = ''
        for column in range(nb_columns):
            character = get_content(positions, row, column)
            if character is None:
                display_line += '-'
            elif character == 'spawn_player_1':
                display_line += '1'
            elif character == 'spawn_player_2':
                display_line += '2'
            elif character == 'spur':
                display_line += '+'
            else:
                display_line += character[0]
        print(display_line)


positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'), 'Lee': ('24', '3'),
             'May': ('14', '6'), 'Rob': ('20', '17'), 'Buf': ('20', '17'), 'Lia': ('19', '7'), 'Mey': ('3', '3'),
             'Tob': ('2', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ['bear', '20', '5', '3', '100'],
             ('10', '20'): ['bear', '20', '5', '3', '100'], ('15', '10'): ['wolf', '10', '3', '2', '50']}

display_board(positions, 25, 40)
