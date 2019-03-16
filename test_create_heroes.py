def create_heroes(positions, classes):
    """Takes the player's input, splits the information and stores it into a dictionary.

    Parameter:
    ----------
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board and the heroes (dict)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)

    Notes:
    ------
    The names of the different heroes must all be unique and can't contain special characters.

    Version:
    --------
    specification: Zephyr Houyoux (v.3 09/03/19)
    implementation: Aude Lekeux (v.2 15/03/19)
    """

    player_input = input(str('Enter your four heroes and their type[name:type]: '))

    # conditions syntax + type: healer mage rogue barbarian (nothing else possible)
    # ask again while syntax is invalid
    invalid_syntax = True

    player_input = player_input.split(" ")
    
    while invalid_syntax:
        invalid_syntax = False

        for sp in player_input:
            name, type = sp.split(":")

            #for letter in name:

            if not name.isalpha():
                print('The name is not appropriated, it should contain only letters! ')
                invalid_syntax = True
            else:
                positions[name] = type

            if type not in classes:
                print('The type of your hero is unknown! ')

    print(positions)


positions = {(10, 24): 'Wolf', (35, 20): 'Lion'}
classes = {'barbarian': {'energise': [[1, 1, 1], [2, 1, 1], [3, 2, 1], [4, 2, 1]],
                            'stun': [[1, 1, 1], [2, 2, 2], [3, 3, 1]]},
              'healer': {'invigorate': [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]],
                         'immunise': [[1, 0, 1], [2, 0, 3], [3, 0, 3]]},
              'mage': {'fulgura': [[1, 3, 1], [2, 3, 1], [3, 4, 1], [4, 4, 1]],
                       'ovibus': [[1, 1, 3], [2, 2, 3], [3, 2, 3]]},
              'rogue':{'reach': [[1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1]],
                       'brust': [[1, 1, 1], [2, 2, 1], [3, 3, 1]]}}

print(create_heroes(positions, classes))

# Baz:barbarian Lee:healer May:mage Rob:rogue
