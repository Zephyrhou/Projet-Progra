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


def game(player_1, player_2):
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
    implementation: Aude Lekeux (v.4 04/04/19)
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
    creatures = []

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

    # Index the words "spur" and "creatures"
    spur_index = None
    creatures_index = None

    # Determines from where begins the coordinates of spur or the creatures
    for index in range(9, len(board)):
        if board[index] == 'spur':
            spur_index = index
        elif board[index] == 'creatures':
            creatures_index = index

    # Stock the spur in positions
    for index in range(spur_index + 1, creatures_index, 2):
        positions[(board[index], board[index + 1])] = 'spur'

    # Stock the creatures in positions and creatures
    for index in range(creatures_index + 1, len(board), 7):
        positions[(board[index + 1], board[index + 2])] = [board[index], board[index + 3], board[index + 4],
                                                           board[index + 5], board[index + 6]]
        creatures += [board[index]]

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
    implementation: Aude Lekeux (v.3 04/04/19)
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
                display_line += character[0]
        print(display_line)


# Function 7
def is_game_over(nb_turns_wanted, nb_turns1, nb_turns2, inactivity_time, positions, initial_positions, creatures, initial_creatures):
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
    specification: Aude Lekeux (v.5 07/04/2019)
    implementation: Zéphyr Houyoux (v.3 07/04/2019)
    """

    if nb_turns1 == nb_turns_wanted or nb_turns2 == nb_turns_wanted:
        return True

    i_time = inactivity(positions, initial_positions, creatures, initial_creatures, inactivity_time)
    print(i_time[0])
    if i_time[0] >= 40:
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


def inactivity(positions, initial_positions, creatures, initial_creatures, inactivity_time):
    """Count the inactivity of the players.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board and the heroes (dict)
    initial_positions: Contains all the coordinates of the board and the heroes before changes (dict)
    creatures: Has every information of each creature (dict)
    initial_creatures: Has every information of each creature before changes (dict)
    inactivity_time: Number of turns no changes has been made (int)

    Returns:
    --------
    inactivity_time: Number of turns where the game is inactive (int)

    Notes:
    ------
    If no changes has been made in the game (no moves, no attacks, etc.) for 40 turns then the game is over.

    Versions:
    ---------
    specification: Zéphyr Houyoux(v.2 05/04/19)
    implementation: Zéphyr Houyoux(v.6 07/04/19)
    """

    # If no changes has been made to positions or if no changes has been made in creatures
    if positions == initial_positions or len(creatures) == len(initial_creatures):
        # Then inactivity increased by one
        inactivity_time += 1

    return inactivity_time


def gap_calculator(position_1, position_2):
    """Computes the gap between two characters.

    Parameter:
    -----------
    position_1: Position of the first character (tuple)
    position_2: Position of the second character (tuple)

    Returns:
    -------
    gap: Gap between two characters (int)

    Version:
    --------
    specification: Manon Michaux (v.3 04/04/19)
    implementation: Zéphyr Houyoux (v.3 04/04/19)
    """

    pos1c = int(position_1[0])
    pos1r = int(position_1[1])
    pos2c = int(position_2[0])
    pos2r = int(position_2[1])

    gap = ((pos1r - pos2r) ** 2 + (pos1c - pos2c) ** 2) ** 0.5

    return gap


# Function 9
def defeated(player, nb_player, positions, creatures):
    """Whenever a hero or a creature is defeated.

    Parameters:
    -----------
    player: Information on the player's defeated hero who will respawn (dict)
    nb_player: Number of the player whose hero is defeated (int)
    creatures: Information on the creature that dies (list)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    player: Information on the player's defeated hero who will respawn (dict)
    position: Contains all the coordinates of the board (dict)
    creatures: Information on the creature that dies (list)

    Notes:
    ------
    A hero or a creature is defeated whenever their health points are at O or less.
    When a hero is defeated he respawns.
    When a creature is defeated it dies and it's victory points are distributed to the heroes around.

    Version:
    --------
    specification: Aude Lekeux (v.6 03/04/19)
    implementation: Aude Lekeux (v.4 03/04/19)
    """

    # Respawn a hero when he's defeated
    for hero in player:
        if player[hero]['life_points'] <= 0:
            if nb_player == 1:
                for key in positions:
                    if positions[key] == 'spawn_player_1':
                        positions[hero] = key
            if nb_player == 2:
                for key in positions:
                    if positions[key] == 'spawn_player_2':
                        positions[hero] = key

            # Reset life points of the hero depending on his class and level
            if player[hero]['class'] == 'barbarian':
                if player[hero]['level'] == 1:
                    player[hero]['life_points'] = 10
                elif player[hero]['level'] == 2:
                    player[hero]['life_points'] = 13
                elif player[hero]['level'] == 3:
                    player[hero]['life_points'] = 16
                elif player[hero]['level'] == 4:
                    player[hero]['life_points'] = 19
                elif player[hero]['level'] == 5:
                    player[hero]['life_points'] = 22
            elif player[hero]['class'] == 'healer':
                if player[hero]['level'] == 1:
                    player[hero]['life_points'] = 10
                elif player[hero]['level'] == 2:
                    player[hero]['life_points'] = 11
                elif player[hero]['level'] == 3:
                    player[hero]['life_points'] = 12
                elif player[hero]['level'] == 4:
                    player[hero]['life_points'] = 13
                elif player[hero]['level'] == 5:
                    player[hero]['life_points'] = 14
            elif player[hero]['class'] == 'mage':
                if player[hero]['level'] == 1:
                    player[hero]['life_points'] = 10
                elif player[hero]['level'] == 2:
                    player[hero]['life_points'] = 12
                elif player[hero]['level'] == 3:
                    player[hero]['life_points'] = 14
                elif player[hero]['level'] == 4:
                    player[hero]['life_points'] = 16
                elif player[hero]['level'] == 5:
                    player[hero]['life_points'] = 18
            elif player[hero]['class'] == 'rogue':
                if player[hero]['level'] == 1:
                    player[hero]['life_points'] = 10
                elif player[hero]['level'] == 2:
                    player[hero]['life_points'] = 12
                elif player[hero]['level'] == 3:
                    player[hero]['life_points'] = 14
                elif player[hero]['level'] == 4:
                    player[hero]['life_points'] = 16
                elif player[hero]['level'] == 5:
                    player[hero]['life_points'] = 18
            print('The hero', hero, 'is respawning')

    # Delete a creature when it's defeated
    for key, value in positions.copy().items():
        if value[0] in creatures:
            if int(value[1]) <= 0:
                del positions[key]
                del creatures[creatures.index(value[0])]
                print('The creature', value[0], 'is dead')
                # If a creature is dead its victory points are distributed

    return player, positions, creatures


# Function 10
def players_choice(choice, positions, player):
    """Translates the player's order and calls the functions move or attack.

    Parameters:
    -----------
    choice: Order of the player (str)
    positions: Contains all the coordinates of the board (dict)
    player: Level, number of point, etc. of heroes of the player (dict)

    Notes:
    ------
    The order of the player must be with the expected format = 'hero_name:@r-c', 'hero_name:*r-c'
    or 'hero_name:capacity'.
    @ stands for a movement, * stands for a simple attack or 'capacity' is the name of a special capacity
    a hero wants to use.

    Version:
    --------
    specification: Zéphyr Houyoux (v.6 07/04/19)
    implementation: Zéphyr Houyoux (v.3 07/04/19)
    """

    choice = choice.split(' ')
    temp = []
    result = {}

    for items in choice:
        temp += items.split(':')

    # Puts the input of the player in a dictionary
    for index in range(len(choice)):
        temp[index] = choice[index].split(':')
        if temp[index][1] != temp[index][-1]:
            name = temp[index][0]
            action = temp[index][1]
            pos = temp[index][2]
            result[name] = (action, pos)
        else:
            name = temp[index][0]
            action = temp[index][1]
            result[name] = action

    # Reads the dictionary and calls the right function (move or attack)
    for item in result:
        if result[item][0] == '@':
            move(positions, item, (result[item][1:3], result[item][4:6]))
        elif result[item][0] == '*':
            attack(positions, item, '', (result[item][1:3], result[item][4:6]), player)
        else:
            name_capacity = result[item]
            attack(positions, item, name_capacity, (0, 0), player)


# Function 11
def attack(positions, hero, capacity, coordinates, attack, player):
    """Checks whether the hero can do the attack, if yes, does it, if no, the attack is ignored.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    player: All the data about heroes (dict)
    capacity: Name of the special capacity (str)
    attack: Where the attack is made (tuple)

    Returns:
    --------
    player: All the data about heroes (dict)
    creatures: All the data about creatures (dict)

    Notes:
    ------
    A hero can attack with a special capacity if he can, or he can do a simple attack.

    Version:
    --------
    specification: Zephyr Houyoux (v.3 04/03/19)
    implementation:
    """


# Function 12
def move(positions, hero, movement):
    """Checks if the position he will end on is allowed. Do it if it is allowed.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero: Name of the hero who wants to move (str)
    movement: Coordinates the hero wants to go to (tuple)

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
    specification: Zephyr Houyoux (v.5 04/04/19)
    implementation: Zephyr Houyoux (v.4 06/04/19)
    """

    position_hero = positions[hero]
    # Computes the gap between the position of the hero and where he wants to go
    gap = gap_calculator(movement, position_hero)

    # If the hero is already on the position he wants to go on
    if movement[0] == positions[hero][0] and movement[1] == positions[hero][1]:
        return 'Your are already in this position'
    # If the position the hero wants to go on is already taken
    for key in positions:
        if positions[key][0] == movement[0] and positions[key][1] == movement[1]:
            return 'This position is already taken'
    else:
        # If the gap is less than 1.5 he can move
        if gap < 1.5:
            positions[hero] = movement
            return positions
        else:
            return 'This position is too far from where you are'


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
def special_capacity_available(player, hero):
    """Whenever a hero reaches level 2 or 3 he can start using special capacities.

    Parameters:
    -----------
    player: Level, number of point, etc. of the heroes of player (dict)
    hero: Name of the hero who leveled up (str)

    Version:
    --------
    specification: Aude Lekeux (v.2 05/04/19)
    implementation: Aude Lekeux (v.2 05/04/19)
    """

    if player[hero]['level'] == 2:
        if player[hero]['class'] == 'barbarian':
            print('The hero ' + hero + ' can now use the capacity energise')
        if player[hero]['class'] == 'healer':
            print('The hero ' + hero + ' can now use the capacity invigorate')
        if player[hero]['class'] == 'mage':
            print('The hero ' + hero + ' can now use the capacity fulgura')
        if player[hero]['class'] == 'rogue':
            print('The hero ' + hero + ' can now use the capacity reach')

    if player[hero]['level'] == 3:
        if player[hero]['class'] == 'barbarian':
            print('The hero ' + hero + ' can now use the capacity stun')
        if player[hero]['class'] == 'healer':
            print('The hero ' + hero + ' can now use the capacity immunise')
        if player[hero]['class'] == 'mage':
            print('The hero ' + hero + ' can now use the capacity ovibus')
        if player[hero]['class'] == 'rogue':
            print('The hero ' + hero + ' can now use the capacity burst')


def summarize(player_1, initial_p1, player_2, initial_p2, nb_turns, nb_turns_player, initial_positions, positions, ROWS,
              COLUMNS, creatures):
    """Summarizes the state of the game.

    Parameters:
    -----------
    player_1: Level, number of point, etc. of heroes of player1 (dict)
    initial_p1: Level, number of point, etc. of heroes of player1 before changes (dict)
    player_2: Level, number of point, etc. of heroes of player2 (dict)
    initial_p2: Level, number of point, etc. of heroes of player2 before changes (dict)
    nb_turns: Number of turns of the game (int)
    nb_turns_player: Number of turns a hero of a player is on spur (int)
    initial_positions: Contains all the coordinates of the board before changes (dict)
    positions: Contains all the coordinates of the board (dict)
    ROWS: Number of rows of the board (int)
    COLUMNS: Number of columns of the board (int)
    creatures: All the data about creatures (dict)

    Version:
    --------
    specification: Manon Michaux (v.4 06/04/19)
    implementation: Aude Lekeux (v.3 06/04/19)
    """

    for hero in positions:
        if positions[hero] != initial_positions[hero]:
            # Whenever a hero has been respawning
            for key, value in positions.copy().items():
                if positions[hero] == key:
                    print(hero + ' has been respawning to ' + str(key))

    # Whenever a hero leveled up he can use a special capacity
    for hero1 in player_1:
        if player_1[hero1]['level'] != initial_p1[hero1]['level']:
            special_capacity_available(player_1, hero1)
    for hero2 in player_2:
        if player_2[hero2]['level'] != initial_p2[hero2]['level']:
            special_capacity_available(player_2, hero2)

    print('Creatures = ' + str(creatures))
    print('Positions = ' + str(positions))
    print('Number of turns played = ' + str(nb_turns))
    print('Number of turns player is on spur = ' + str(nb_turns_player))
    display_board(ROWS, COLUMNS, positions)

    # Resets initial positions to positions
    initial_positions = positions
    # Resets the players to initial players
    initial_p1 = player_1
    initial_p2 = player_2

    return initial_positions, positions, initial_p1, initial_p2, creatures


def is_cell_empty(cell, positions):
    """Checks whether the cell is empty or not

    Parameters:
    -----------
    cell: Position of the cell (tuple)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    cell_empty: If the cell is empty or not (bool)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    cell_empty = True

    for item in positions:
        if cell == item or cell == positions[item]:
            cell_empty = False

    return cell_empty


def get_class(hero, player):
    """Determines the class of a hero depending on his name

    Parameters:
    -----------
    hero: Name of the hero (str)
    player: All the data about heroes (dict)

    Returns:
    --------
    class: Class of the hero (str)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    for heroes in player:
        if hero == heroes:
            return player[heroes]['class']


def get_level(hero, player):
    """Determines the class of a hero depending on his name

    Parameters:
    -----------
    hero: Name of the hero (str)
    player: All the data about heroes (dict)

    Returns:
    --------
    level: Level of the hero (int)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    for heroes in player:
        if hero == heroes:
            return player[heroes]['level']


def get_life_points(hero, player):
    """Determines the class of a hero depending on his name

    Parameters:
    -----------
    hero: Name of the hero (str)
    player: All the data about heroes (dict)

    Returns:
    --------
    life_points: Life points of the hero (int)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    for heroes in player:
        if hero == heroes:
            return player[heroes]['life_points']


def get_victory_points(hero, player):
    """Determines the class of a hero depending on his name

    Parameters:
    -----------
    hero: Name of the hero (str)
    player: All the data about heroes (dict)

    Returns:
    --------
    victory_points: Victory points of the hero (int)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    for heroes in player:
        if hero == heroes:
            return player[heroes]['victory_points']


def get_damage_points(hero, player):
    """Determines the class of a hero depending on his name

    Parameters:
    -----------
    hero: Name of the hero (str)
    player: All the data about heroes (dict)

    Returns:
    --------
    damage_points: Damage points of the hero (int)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    for heroes in player:
        if hero == heroes:
            return player[heroes]['damage_points']


def is_on_spur(hero, positions):
    """Checks whether a hero is on spur.

    Parameters:
    -----------
    hero: Name of the heo (str)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    on_spur: If the hero is on spur or not (bool)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    for item in positions:
        if positions[item] == 'spur':
            if positions[hero] == item:
                return True
    return False


def move_cell(character, start, new_position, positions, creatures):
    """Move from one cell to another.

    Parameters:
    -----------
    character: Either the name of a hero or of a creature (str)
    start: Position the character is on now (tuple)
    finish: Position the character wants to go on (tuple)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)

    Notes:
    ------
    This function is called only when the movement can be executed.

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    if character in positions:
        positions[character] = new_position

    elif character in creatures:
        for key, value in positions.copy().items():
            if key == start:
                # Adds the new position and deletes the previous one
                positions[new_position] = positions[key]
                del positions[key]

    return positions
