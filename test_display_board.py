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
    """

    Parameters:
    -----------
    positions:
    row:
    column:

    Returns:
    --------
    character:

    Version:
    --------
    specification:
    implementation:
    """

    if positions['spur'] == (row, column):
        character = '.'
    elif positions['spawn_player_1'] == (row, column):
        character = '*'
    elif positions['spawn_player_2'] == (row, column):
        character = '*'
    elif positions['bear'] == (row, column):
        character = 'b'
    elif positions['wolf'] == (row, column):
        character = 'w'
    # elif positions['barbarian'] == (row, column):
    #     character = 'B'
    # elif positions['mage'] == (row, column):
    #     character = 'M'
    # elif positions['rogue'] == (row, column):
    #     character = 'R'
    # elif positions['healer'] == (row, column):
    #     character = 'H'
    else:
        character = u"\u2610"

    return character


positions = {'spawn_player_1': ('20', '3'), 'spawn_player_2': ('20', '38'),
             'spur': [('20', '38'), ('20', '39'), ('21', '38'), ('21', '39')],
             'bear': [('10', '10'), ('10', '20')], 'wolf': [('15', '10')]}

print(display_board(positions, 25, 40))

# u"\u2610"
# []
