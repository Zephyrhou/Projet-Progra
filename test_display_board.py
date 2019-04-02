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
                display_line += u"-"
            elif character == 'spawn_player_1':
                display_line += '1'
            elif character == 'spawn_player_2':
                display_line += '2'
            elif character == 'spur':
                display_line += '+'
            else:
                display_line += str(character)
        print(display_line)


positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', ('20', '38'): 'spur', ('20', '39'): 'spur',
             ('21', '38'): 'spur', ('21', '39'): 'spur', ('10', '10'): 'bear', ('10', '20'): 'bear',
             ('15', '10'): 'wolf', 'B': ('4', '3'), 'H': ('20', '6'), 'M': ('17', '3'), 'R': ('8', '11')}

players_positions = {'spawn_player_1': ('20', '3'), 'spawn_player_2': ('20', '38'), 'Baz': ('20', '3'),
                     'Hee': ('21', '3'), 'May': ('10', '3'), 'Rob': ('15', '5'), 'Buf': ('20', '30'),
                     'Hia': ('18', '3'), 'Mey': ('2', '8'), 'Ran': ('21', '35')}


print(display_board(positions, 25, 40))

# print(get_content(positions, 20, 3))

# u"\u2610"
# []
# for position in positions:
#     for word in position:
#         for letter in word:
#             print(letter)

# if positions['spur'] == [(row, column)]:
#     character = '.'
# elif positions['spawn_player_1'] == (row, column):
#     character = '*'
# elif positions['spawn_player_2'] == (row, column):
#     character = '**'
# elif positions['bear'] == [(row, column)]:
#     character = 'b'
# elif positions['wolf'] == [(row, column)]:
#     character = 'w'
# elif positions['B'] == (row, column):
#     character = 'B'
# elif positions['M'] == (row, column):
#     character = 'M'
# elif positions['R'] == (row, column):
#     character = 'R'
# elif positions['H'] == (row, column):
#     character = 'H'
# else:
#     character = u"\u2610"
