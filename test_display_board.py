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
