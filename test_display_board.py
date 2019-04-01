def display_board(positions, nb_rows, nb_columns):
    """Displays the board.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)

    Version:
    --------
    specification: Manon Michaux (v.2 25/02/19)
    implementation: Aude Lekeux (v.5 1/04/19)
    """

    for row in range(nb_rows):
        display_line = ''
        for column in range(nb_columns):
            display_line += get_content(positions, row, column)
        print(display_line)


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
    implementation: Aude Lekeux (v.1 1/04/19)
    """

    row = str(row)
    column = str(column)

    if positions['spur'] == (row, column):
        character = '.'
    elif positions['spawn_player_1'] == (row, column):
        character = '*'
    elif positions['spawn_player_2'] == (row, column):
        character = '**'
    elif positions['bear'] == [(row, column)]:
        character = 'b'
    elif positions['wolf'] == [(row, column)]:
        character = 'w'
    elif positions['B'] == (row, column):
        character = 'B'
    elif positions['M'] == (row, column):
        character = 'M'
    elif positions['R'] == (row, column):
        character = 'R'
    elif positions['H'] == (row, column):
        character = 'H'
    else:
        character = u"\u2610"

    return character


positions = {'spawn_player_1': ('20', '3'), 'spawn_player_2': ('20', '38'),
             'spur': [('20', '38'), ('20', '39'), ('21', '38'), ('21', '39')],
             'bear': [('10', '10'), ('10', '20')], 'wolf': [('15', '10')], 'B': ('4', '3'),
             'H': ('20', '6'), 'M': ('17', '3'), 'R': ('8', '11')}

players_positions = {'spawn_player_1': ('20', '3'), 'spawn_player_2': ('20', '38'), 'Baz': ('20', '3'),
                     'Lee': ('20', '3'), 'May': ('20', '3'), 'Rob': ('20', '3'), 'Buf': ('20', '38'),
                     'Lia': ('20', '38'), 'Mey': ('20', '38'), 'Tob': ('20', '38')}


print(display_board(positions, 25, 40))

# u"\u2610"
# []
