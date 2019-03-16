def initializaion():

    positions = {(10, 24): 'Wolf', (35, 20): 'Lion'}

    classes = {'barbarian': {'energise': [[1, 1, 1], [2, 1, 1], [3, 2, 1], [4, 2, 1]],
                             'stun': [[1, 1, 1], [2, 2, 2], [3, 3, 1]]},
               'healer': {'invigorate': [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]],
                          'immunise': [[1, 0, 1], [2, 0, 3], [3, 0, 3]]},
               'mage': {'fulgura': [[1, 3, 1], [2, 3, 1], [3, 4, 1], [4, 4, 1]],
                        'ovibus': [[1, 1, 3], [2, 2, 3], [3, 2, 3]]},
               'rogue': {'reach': [[1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1]],
                         'brust': [[1, 1, 1], [2, 2, 1], [3, 3, 1]]}}


    player1 = create_heroes(classes)
    # player2 = create_heroes(classes)

    print(player1)


def create_heroes(classes):
    """Takes the player's input, splits the information and stores it into a dictionary.

    Parameter:
    ----------
    positions: Contains all the coordinates of the board (dict)
    classes:
    hero_number:

    Returns:
    --------
    positions: Contains all the coordinates of the board and the heroes (dict)
    player: Level, number of point, etc. of the heroes of player (dict)

    Notes:
    ------
    The names of the different heroes must all be unique and can't contain special characters.

    Version:
    --------
    specification: Zephyr Houyoux (v.3 09/03/19)
    implementation: Aude Lekeux (v.2 15/03/19)
    """

    # conditions syntax
    # ask again while syntax is invalid
    player = {}
    invalid_syntax = True
    
    while invalid_syntax and len(player) < 4:
        invalid_syntax = False
        player_input = input(str('Enter your four heroes and their type[name:type]: '))
        player_input = player_input.split(" ")

        for sp in player_input:
            name, type = sp.split(":")

            if not name.isalpha():
                print('The name ' + name + ' is not appropriated, it should contain only letters!')
                invalid_syntax = True

            elif type not in classes:
                print('The type ' + type + ' of your hero is unknown!')
                invalid_syntax = True

            elif name not in player:
                player[name] = type

            elif name in player:
                print('The name ' + name + ' is already taken!')
                player = {}
                invalid_syntax = True

    return player


# Baz:barbarian Lee:healer May:mage Rob:rogue
initializaion()
