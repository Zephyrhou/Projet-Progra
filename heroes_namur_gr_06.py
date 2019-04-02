# Function 1
def launch(board_file):
    """Starts the game.

    Parameter:
    ----------
    board_file: Path of the file used to create the board (str)

    Version:
    --------
    specification: Zephyr Houyoux (v.2 04/03/19)
    implementation: Aude Lekeux (v.2 02/04/19)
    """

    initialization(board_file)
    # game()


# Function 2
def initialization(board_file):
    """Initialization of the game. Creation of the board and the heroes.

    Parameter:
    ----------
    board_file: Path of the file used to create the board (str)

    Version:
    --------
    specification: Zephyr Houyoux (v.3 02/04/19)
    implementation: Aude Lekeux (v.2 02/04/19)
    """

    player_1 = create_heroes()
    player_2 = create_heroes()

    ROWS, COLUMNS, NB_TURNS, positions, creatures = create_board(board_file, player_1, player_2)

    display_board(ROWS, COLUMNS, positions)


def game():
    """Starts a new turn if the game is not finished.

    Returns:
    --------
    nb_turns_wanted: Number of turns needed to be on the spur in order to win (int)
    nb_turns1: Number of turns a hero of player1 stands on the spur (int)
    nb_turns2: Number of turns a hero of player2 stands on the spur (int)
    inactivity: Number of turns no activity has been observed (int)

    Version:
    --------
    specification: Zephyr Houyoux (v.4 02/04/19)
    implementation:
    """

    update_level(player_1)
    update_level(player_2)

    return nb_turns_wanted, nb_turns1, nb_turns2, inactivity_time


# Function 3
def create_board(board_file, player_1, player_2):
    """Creates the map and displays it.

    Parameter:
    ----------
    board_file : Path of the file used to create the board (str)
    player_1: Level, number of point, etc. of the heroes of player 1 (dict)
    player_2: Level, number of point, etc. of the heroes of player 2 (dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board (dict)
    creatures: Has every information of each creature (dict)
    NB_TURNS: Number of turns the heroes need to be on spur to win (int)
    ROWS: Number of rows of the board (int)
    COLUMNS: Number of columns of the board (int)

    Version:
    --------
    specification : Manon Michaux (v.6 02/04/19)
    implementation: Aude Lekeux (v.3 02/04/19)
    """

    b_file = open(board_file, 'r')
    board = []
    lines = []
    lines += b_file.readlines()

    for line in lines:
        line = line.replace('\n', '')
        line = line.replace(':', '')
        line = line.split(' ')
        board += line

    del lines
    b_file.close()

    positions = {}
    creatures = {}

    ROWS = int(board[1])
    COLUMNS = int(board[2])
    NB_TURNS = int(board[3])

    SPAWN_PLAYER_1 = (board[5], board[6])
    SPAWN_PLAYER_2 = (board[7], board[8])
    positions[SPAWN_PLAYER_1] = 'spawn_player_1'
    positions[SPAWN_PLAYER_2] = 'spawn_player_2'

    # Puts heroes in positions with the right position
    for hero in player_1:
        positions[hero] = SPAWN_PLAYER_1
    for hero in player_2:
        positions[hero] = SPAWN_PLAYER_2

    # Index des mots "spur" et "creatures"
    spur_index = None
    creatures_index = None

    # Determine a partir de ou commence les coordonnes du spur ou des creatures
    for index in range(9, len(board)):
        if board[index] == 'spur':
            spur_index = index
        elif board[index] == 'creatures':
            creatures_index = index

    # Stock le spur
    for index in range(spur_index + 1, creatures_index, 2):
        positions[(board[index], board[index + 1])] = 'spur'

    # Stock les creatures
    for index in range(creatures_index + 1, len(board), 7):
        positions[(board[index + 1], board[index + 2])] = board[index]

    # creatures[board[19]]['h_points'] = board[22]
    # creatures[board[19]]['d_points'] = board[23]
    # creatures[board[19]]['creature_wage'] = board[24]
    # creatures[board[19]]['v_points'] = board[25]
    # creatures[board[26]]['h_points'] = board[29]
    # creatures[board[26]]['d_points'] = board[30]
    # creatures[board[26]]['creature_wage'] = board[31]
    # creatures[board[26]]['v_points'] = board[32]

    # for item in range(board[19], board[25]):
    #     creatures['h_points'] = item
    #     creatures['d_points'] = board[23]
    #     creatures['creature_wage'] = board[24]
    #     creatures['v_points'] = board[25]
    #
    # for creatures in board[26]:
    #     creatures['h_points'] = board[29]
    #     creatures['d_points'] = board[30]
    #     creatures['creature_wage'] = board[31]
    #     creatures['v_points'] = board[32]

    del board

    return ROWS, COLUMNS, NB_TURNS, positions, creatures


# Function 4
def create_heroes():
    """Takes the player's input, splits the information and stores it into a dictionary.

    Returns:
    --------
    player: Level, number of point, etc. of the heroes of player (dict)

    Notes:
    ------
    The names of the different heroes must all be unique and can't contain special characters.

    Version:
    --------
    specification: Zephyr Houyoux (v.4 02/04/19)
    implementation: Aude Lekeux (v.5 02/04/19)
    """

    classes = {'barbarian': {'energise': [[1, 1, 1], [2, 1, 1], [3, 2, 1], [4, 2, 1]],
                             'stun': [[1, 1, 1], [2, 2, 2], [3, 3, 1]]},
               'healer': {'invigorate': [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]],
                          'immunise': [[1, 0, 1], [2, 0, 3], [3, 0, 3]]},
               'mage': {'fulgura': [[1, 3, 1], [2, 3, 1], [3, 4, 1], [4, 4, 1]],
                        'ovibus': [[1, 1, 3], [2, 2, 3], [3, 2, 3]]},
               'rogue': {'reach': [[1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1]],
                         'brust': [[1, 1, 1], [2, 2, 1], [3, 3, 1]]}}

    player = {}
    invalid_syntax = True

    # ask again while syntax is invalid and creates the dictionary of the player
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

        # initializes the data of the heroes
        for key, value in player.items():
            if value == 'barbarian':
                player[key] = {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0,
                               'damage_points': 2}
            elif value == 'rogue':
                player[key] = {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}
            elif value == 'healer':
                player[key] = {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0,
                               'damage_points': 2}
            elif value == 'mage':
                player[key] = {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}

    return player


# Function 5.2
def get_content(row, column, positions):
    """Returns the content of a certain row and column in the board.

    Parameters:
    -----------
    row: Number of the row (int)
    column: Number of the column (int)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    key: Key which is on the coordinates asked (str)

    Version:
    --------
    specification: Aude Lekeux (v.1 02/04/19)
    implementation: Aude Lekeux (v.2 02/04/19)
    """
    row = str(row)
    column = str(column)

    for key in positions:
        if key == (row, column):
            return positions[key]
        elif positions[key] == (row, column):
            return key


# Function 5
def display_board(ROWS, COLUMNS, positions):
    """Displays the board.

    Parameters:
    -----------
    ROWS: Number of rows of the board (int)
    COLUMNS: Number of columns of the board (int)
    positions: Contains all the coordinates of the board (dict)

    Version:
    --------
    specification: Manon Michaux (v.3 02/04/19)
    implementation: Aude Lekeux (v.4 02/04/19)
    """

    for row in range(ROWS):
        display_line = ''
        for column in range(COLUMNS):
            character = get_content(row, column, positions)
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


# Function 7
def is_game_over(nb_turns_wanted, nb_turns1, nb_turns2, inactivity_time):
    """Checks whether the game is over or not.

    Parameters:
    -----------
    nb_turns_wanted: Number of turns the heroes need to be on spur to win (int)
    nb_turns1: Number of turns a hero of player1 stands on the spur (int)
    nb_turns2: Number of turns a hero of player2 stands on the spur (int)
    inactivity_time: Number of turns no activity has been observed (int)

    Returns:
    -------
    game_over: Is the game over or not (bool)

    Notes:
    ------
    A hero must stay for a given number of consecutive turns on the spur in order to win, this number is in board_file.

    Version:
    --------
    specification: Aude Lekeux (v.4 04/03/2019)
    implementation: Zéphyr Houyoux (v.2 21/03/2019)
    """

    if nb_turns_wanted == nb_turns1 or nb_turns2:
        return True
    elif inactivity_time == 40:
        return True
    else:
        return False


# Function 8
def creature_turn(positions, creatures, player1, player2):
    """Checks where a creature should attack or move depending on it's surrounding.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    creatures: Has every information of each creature (dict)
    player1: Level, number of point, etc. of heroes of player1 (dict)
    player2: Level, number of point, etc. of heroes of player2 (dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of heroes of player1 (dict)
    player2: Level, number of point, etc. of heroes of player2 (dict)

    Notes:
    ------
    A creature attacks or moves towards the closest enemy.
    It can also do nothing.

    Version:
    --------
    specification: Aude Lekeux(v.4 04/03/2019)
    implementation:
    """


def inactivity(positions, inactivity, incativity_time):
    """Count the inactivity of the players.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board and the heroes(dict)
    inactivity: Contains all the coordinates of the board and the heroes of the previous turn(dict)

    Returns:
    --------
    inactivity: Contains all the coordinates of the board and the heroes of the previous turn(dict)
    inactivity_time: Number of inactivity turn(int)

    Versions:
    ---------
    specification: Zéphyr Houyoux (v.1 17/03/19)
    implementation: Zéphyr Houyoux(v.2 21/03/19)
    """

    if positions == inactivity:
        inactivity_time = + 1
    inactivity = positions

    return inactivity, inactivity_time


def gap_calculator(positions, name_character1, name_character2):
    """ Compute the gap between two things.

    Parameter:
    -----------
    positions : Contains all the coordinates of the board (dict)    name_character1 :

    Returns:
    -------
    gap : gap between two things (int)

    Version:
    --------
    specification : Manon Michaux (v.1 08/03/19)
    implementaion : Zéphyr Houyoux (v.1 17/03/19)
    """

    pos1h = positions[name_character1]['nb_rows']
    pos1l = positions[name_character1]['nb_columns']
    pos2h = positions[name_character2]['nb_rows']
    pos2l = positions[name_character2]['nb_columns']
    gap = ((pos1l - pos2l) ** 2 + (pos1h - pos2h) ** 2) ** 0.5

    return gap


# Function 9
def defeated(player, nb_player, creature, positions):
    """Whenever a hero or a creature is defeated.

    Parameters:
    -----------
    player: Information on the player's defeated hero who will respawn (dict)
    creature: Information on the creature that dies (dict)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    player: Information on the player's defeated hero who will respawn (dict)
    position: Contains all the coordinates of the board (dict)

    Notes:
    ------
    A hero or a creature is defeated whenever their health points are at O or less.
    When a hero is defeated he respawns.
    When a creature is defeated it dies and it's victory points are distributed to the heroes around.

    Version:
    --------
    specification: Aude Lekeux (v.5 04/03/2019)
    implementation: Aude Lekeux (v.3 19/03/19)
    """

    if player['life_points'] <= 0:
        positions[player] = 'respawn' + nb_player
        print('The player', player, 'is respawn')
    if positions[creature] <= 0:
        del positions[creature]
        print('The creature', creature, 'is dead')

    return player, positions


# Function 10
def players_choice(choice, positions):
    """Translates the player's order into actions.

    Parameters:
    -----------
    choice: Order of the player (str)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board (dict)

    Notes:
    ------
    The order of the player must be with the expected format = "hero_name : @r-c(movement) or *r-c(attack) "

    Version:
    --------
    specification: Manon Michaux (v.3 04/03/19)
    implementation:
    """


# Function 11
def attack(name_attack, positions, player, creatures):
    """Checks whether the hero can do the attack, if yes, does it, if no, the attack is ignored.

    Parameters:
    -----------
    name_attack: Name of the attack (str)
    positions: Contains all the coordinates of the board (dict)
    player: All the data about heroes (dict)
    creatures: All the data about creatures (dict)

    Returns:
    --------
    player: All the data about heroes (dict)
    creatures: All the data about creatures (dict)

    Version:
    --------
    specification: Zephyr Houyoux (v.3 04/03/19)
    implementation: 
    """


# Function 12
def move(positions, movement):
    """Checks if the position he will end on is allowed. If the movement is ok, it's being executed.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    movement: Coordinates the hero will go (str)

    Returns:
    --------
    positions: Contains the updated coordinates of the board (dict)

    Notes:
    ------
    It isn't allowed to move if there is already a hero or a creatures where you want to move.
    If the movement can't be done an error message is displayed and the movement is ignored.
    Movement can only be of one step in one of the eight directions.

    Version:
    --------
    specification: Zephyr Houyoux (v.3 04/03/19)
    implementation:
    """


# Function 13
def update_level(player):
    """Checks if a hero can level up and upgrade their characteristics.

    Parameters:
    -----------
    player: All the data about the heroes (dict)

    Returns:
    --------
    player: Updated data about the heroes (dict)

    Version:
    --------
    specification: Manon Michaux (v.3 04/03/19)
    implementation: Aude Lekeux (v.4 02/04/19)
    """

    # Level increase depending on the hero's victory points
    for hero in player:
        # If hero is under 100 victory points
        if player[hero]['victory_points'] < 100:
            print('Hero ' + hero + ' remains on level 1')
            player[hero]['level'] = 1
            player[hero]['life_points'] = 10
            player[hero]['damage_points'] = 2
        # If hero is over 100 points
        else:
            if player[hero]['class'] == 'barbarian':
                if player[hero]['victory_points'] < 200:
                    player[hero]['level'] = 2
                    player[hero]['life_points'] = 13
                    player[hero]['damage_points'] = 3
                elif player[hero]['victory_points'] < 400:
                    player[hero]['level'] = 3
                    player[hero]['life_points'] = 16
                    player[hero]['damage_points'] = 4
                elif player[hero]['victory_points'] < 800:
                    player[hero]['level'] = 4
                    player[hero]['life_points'] = 19
                    player[hero]['damage_points'] = 5
                elif player[hero]['victory_points'] > 800:
                    player[hero]['level'] = 5
                    player[hero]['life_points'] = 22
                    player[hero]['damage_points'] = 6
            elif player[hero]['class'] == 'healer':
                if player[hero]['victory_points'] < 200:
                    player[hero]['level'] = 2
                    player[hero]['life_points'] = 11
                    player[hero]['damage_points'] = 2
                elif player[hero]['victory_points'] < 400:
                    player[hero]['level'] = 3
                    player[hero]['life_points'] = 12
                    player[hero]['damage_points'] = 3
                elif player[hero]['victory_points'] < 800:
                    player[hero]['level'] = 4
                    player[hero]['life_points'] = 13
                    player[hero]['damage_points'] = 3
                elif player[hero]['victory_points'] > 800:
                    player[hero]['level'] = 5
                    player[hero]['life_points'] = 14
                    player[hero]['damage_points'] = 4
            elif player[hero]['class'] == 'mage':
                if player[hero]['victory_points'] < 200:
                    player[hero]['level'] = 2
                    player[hero]['life_points'] = 12
                    player[hero]['damage_points'] = 3
                elif player[hero]['victory_points'] < 400:
                    player[hero]['level'] = 3
                    player[hero]['life_points'] = 14
                    player[hero]['damage_points'] = 4
                elif player[hero]['victory_points'] < 800:
                    player[hero]['level'] = 4
                    player[hero]['life_points'] = 16
                    player[hero]['damage_points'] = 5
                elif player[hero]['victory_points'] > 800:
                    player[hero]['level'] = 5
                    player[hero]['life_points'] = 18
                    player[hero]['damage_points'] = 6
            elif player[hero]['class'] == 'rogue':
                if player[hero]['victory_points'] < 200:
                    player[hero]['level'] = 2
                    player[hero]['life_points'] = 12
                    player[hero]['damage_points'] = 3
                elif player[hero]['victory_points'] < 400:
                    player[hero]['level'] = 3
                    player[hero]['life_points'] = 14
                    player[hero]['damage_points'] = 4
                elif player[hero]['victory_points'] < 800:
                    player[hero]['level'] = 4
                    player[hero]['life_points'] = 16
                    player[hero]['damage_points'] = 5
                elif player[hero]['victory_points'] > 800:
                    player[hero]['level'] = 5
                    player[hero]['life_points'] = 18
                    player[hero]['damage_points'] = 6
            print('Hero ' + hero + ' has increased to level ' + str(player[hero]['level']))

    return player


# Function 14
def summarize(player, creatures, nb_turns):
    """Summarizes the state of the game.

    Parameters:
    -----------
    player: All the data about the heroes (dict)
    creatures: All the data about creatures (dict)
    nb_turns: Number of turns of the game (int)

    Version:
    --------
    specification: Manon Michaux (v.2 25/02/19)
    implementation: Aude Lekeux (v.2 15/03/19)
    """
