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
                character = str(character[0])
                display_line += character
        print(display_line)


positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', ('20', '38'): 'spur', ('20', '39'): 'spur',
             ('21', '38'): 'spur', ('21', '39'): 'spur', ('10', '10'): 'bear', ('10', '20'): 'bear',
             ('15', '10'): 'wolf', 'Baz': ('4', '3'), 'Hat': ('20', '6'), 'May': ('17', '3'), 'Rob': ('8', '11')}

print(display_board(positions, 25, 40))

# u"\u2610"
# []
