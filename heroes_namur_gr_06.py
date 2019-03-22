#Function 1
def launch(board_file):
    """Starts the game.

    Parameter:
    ----------
    board_file: Path of the file used to create the board (str)

    Version:
    --------
    specification: Zephyr Houyoux (v.2 04/03/19)
    implementation: Aude Lekeux (v.1 22/03/19)
    """

    initialization(board_file)

    while not is_game_over(nb_turns_wanted, nb_turns1, nb_turns2, inactivity_time):
        game()


#Function 2
def initialization(board_file):
    """Initialization of the game. Creation of the board and the heroes.

    Parameter:
    ----------
    board_file: Path of the file used to create the board (str)

    Returns:
    --------
    positions: Contains all the coordinates of the board and the heroes (dict)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)

    Version:
    --------
    specification: Zephyr Houyoux (v.2 04/03/19)
    implementation: Aude Lekeux (v.2 22/03/19)
    """

    classes = {'barbarian': {'energise': [[1, 1, 1], [2, 1, 1], [3, 2, 1], [4, 2, 1]],
                             'stun': [[1, 1, 1], [2, 2, 2], [3, 3, 1]]},
               'healer': {'invigorate': [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]],
                          'immunise': [[1, 0, 1], [2, 0, 3], [3, 0, 3]]},
               'mage': {'fulgura': [[1, 3, 1], [2, 3, 1], [3, 4, 1], [4, 4, 1]],
                        'ovibus': [[1, 1, 3], [2, 2, 3], [3, 2, 3]]},
               'rogue': {'reach': [[1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1]],
                         'brust': [[1, 1, 1], [2, 2, 1], [3, 3, 1]]}}

    nb_ranges, nb_columns, nb_turns_wanted, positions, creatures = create_board(board_file)

    player1 = create_heroes(classes, positions)
    player2 = create_heroes(classes, positions)

    # Puts heroes in positions with the right position
    for hero in player1:
        positions[hero] = positions['spawn_player_1']
    for hero in player2:
        positions[hero] = positions['spawn_player_2']

    return positions, player1, player2, nb_turns_wanted

    # Baz:barbarian Lee:healer May:mage Rob:rogue
    # Buf:barbarian Lia:rogue Mey:mage Tob:rogue


def game():
    """Starts a new turn if the game is not finished.

    Returns:
    --------
    nb_turns1: Number of turns a hero of player1 stands on the spur (int)
    nb_turns2: Number of turns a hero of player2 stands on the spur (int)
    inactivity: Number of turns no activity has been observed (int)

    Version:
    --------
    specification: Zephyr Houyoux (v.3 04/03/19)
    implementation:
    """

    return nb_turns_wanted, nb_turns1, nb_turns2, inactivity_time


#Function 3
def create_board(board_file):
    """Creates the map and displays it.

    Parameter:
    ----------
    board_file : Path of the file used to create the board (str)

    Returns:
    --------
    positions: Contains all the coordinates of the board (dict)
    nb_turns_wanted: Number of turns the heroes need to be on spur to win (int)
    creatures: Has every information of each creature (dict)
    nb_ranges: number of ranges of the board (int)
    nb_columns: number of columns of the board (int)

    Version:
    --------
    specification : Manon Michaux (v.5 04/03/19)
    implementation: Manon Michaux (v.2 17/03/19)
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
    print(board)

    b_file.close()

    positions = {}
    creatures = {}

    nb_ranges = board[1]
    nb_columns = board[2]
    nb_turns_wanted = board[3]

    positions['spawn_player_1'] = (board[5], board[6])
    positions['spawn_player_2'] = (board[7], board[8])

    # item = ''
    # for index in range(9, len(board)):
    #     while board[index+1]
    #
    #     if board[index] in ['spur', 'creatures']:
    #         item = board[index]
    #         temp = item
    #
    #         while item == temp:

    spur_index = None
    creatures_index = None

    for index in range(9, len(board)):
        if board[index] == 'spur':
            spur_index = index
        elif board[index] == 'creatures':
            creatures_index = index

    coordinates = []
    for index in range(spur_index + 1, creatures_index, 2):
        coordinates.append((board[index], board[index + 1]))

    positions['spur'] = coordinates

    creatures_type = []
    for index in range(creatures_index + 1, len(board)):
        if board[index].isalpha():
            creatures_type.append(index)

    coordinates = []
    previous_creature = board[creatures_type[0]]
    for creature in creatures_type:
        current_creature = board[creature]
        if current_creature == previous_creature:
            for index in range(creature, creature + 5, 7):
                coordinates.append((board[index + 1], board[index + 2]))
                previous_creature = current_creature
        else:
            positions[previous_creature] = coordinates
            coordinates = []
            for index in range(creature, creature + 5, 7):
                coordinates.append((board[index + 1], board[index + 2]))
                previous_creature = current_creature

    positions[previous_creature] = coordinates

    # del board

    print(positions)

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

    print(creatures)

    return nb_ranges, nb_columns, nb_turns_wanted, positions, creatures


#Function 4
def create_heroes(classes):
    """Takes the player's input, splits the information and stores it into a dictionary.

    Parameter:
    ----------
    classes: Different classes a hero can be (dict)

    Returns:
    --------
    player: Level, number of point, etc. of the heroes of player (dict)

    Notes:
    ------
    The names of the different heroes must all be unique and can't contain special characters.

    Version:
    --------
    specification: Zephyr Houyoux (v.3 09/03/19)
    implementation: Aude Lekeux (v.5 22/03/19)
    """

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

#Function 5
def display_board(positions):
    """Displays the board.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)

    Version:
    --------
    specification: Manon Michaux (v.2 25/02/19)
    implementation: Aude Lekeux (v.2 15/03/19)
    """


#Function 7
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

#Function 8
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


#Function 9
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


#Function 10
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

#Function 11
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

#Function 12
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

#Function 13
def level(player, classes):
    """Checks if a hero can level up and upgrade their characteristics.

    Parameters:
    -----------
    player: All the data about the heroes (dict)
    classes: The four classes of hero possible and their information (dict)

    Returns:
    --------
    player: Updated data about the heroes (dict)

    Version:
    --------
    specification: Manon Michaux (v.3 04/03/19)
    implementation: Aude Lekeux (v.2 15/03/19)
    """

    # level upgrade depending on the hero's victory points
    for hero in player:
        if hero['victory_points'] < 100:
            print('Hero ' + hero + ' does not have enough victory points in order to level up')
        if hero['class'] == 'barbarian':
            if hero['victory_points'] < 200:
                hero['level'] = 2
                hero['life_points'] = 13
                hero['damage_points'] = 3
            if hero['victory_points'] < 400:
                hero['level'] = 3
                hero['life_points'] = 16
                hero['damage_points'] = 4
            if hero['victory_points'] < 800:
                hero['level'] = 4
                hero['life_points'] = 19
                hero['damage_points'] = 5
            if hero['victory_points'] > 800:
                hero['level'] = 5
                hero['life_points'] = 22
                hero['damage_points'] = 6
        if hero['class'] == 'healer':
            if hero['victory_points'] < 200:
                hero['level'] = 2
                hero['life_points'] = 11
                hero['damage_points'] = 2
            if hero['victory_points'] < 400:
                hero['level'] = 3
                hero['life_points'] = 12
                hero['damage_points'] = 3
            if hero['victory_points'] < 800:
                hero['level'] = 4
                hero['life_points'] = 13
                hero['damage_points'] = 3
            if hero['victory_points'] > 800:
                hero['level'] = 5
                hero['life_points'] = 14
                hero['damage_points'] = 4
        if hero['class'] == 'mage':
            if hero['victory_points'] < 200:
                hero['level'] = 2
                hero['life_points'] = 12
                hero['damage_points'] = 3
            if hero['victory_points'] < 400:
                hero['level'] = 3
                hero['life_points'] = 14
                hero['damage_points'] = 4
            if hero['victory_points'] < 800:
                hero['level'] = 4
                hero['life_points'] = 16
                hero['damage_points'] = 5
            if hero['victory_points'] > 800:
                hero['level'] = 5
                hero['life_points'] = 18
                hero['damage_points'] = 6
        if hero['class'] == 'rogue':
            if hero['victory_points'] < 200:
                hero['level'] = 2
                hero['life_points'] = 12
                hero['damage_points'] = 3
            if hero['victory_points'] < 400:
                hero['level'] = 3
                hero['life_points'] = 14
                hero['damage_points'] = 4
            if hero['victory_points'] < 800:
                hero['level'] = 4
                hero['life_points'] = 16
                hero['damage_points'] = 5
            if hero['victory_points'] > 800:
                hero['level'] = 5
                hero['life_points'] = 18
                hero['damage_points'] = 6


#Function 14
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