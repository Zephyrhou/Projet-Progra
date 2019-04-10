from Barbarian import *
from Healer import *
from Mage import *
from Rogue import *
from test import *
import math


# Function 1
def launch(board_file):
    """Starts the game.

    Parameter:
    ----------
    board_file: Path of the file used to create the board (str)

    Version:
    --------
    specification: Zephyr Houyoux (v.2 04/03/19)
    implementation: Aude Lekeux (v.3 08/04/19)
    """

    player1, player2, positions, ROWS, COLUMNS, nb_turns_wanted, creatures = initialization(board_file)

    nb_turn = 0
    nb_spur_p1 = 0
    nb_spur_p2 = 0

    # While the game is not over the next turn begins
    while not is_game_over(nb_turns_wanted, nb_spur_p1, nb_spur_p2):
        nb_spur_p1, nb_spur_p2, positions = game(nb_spur_p1, nb_spur_p2, player1, player2, positions, creatures)
        display_board(ROWS, COLUMNS, positions)
        nb_turn += 1


# Function 2
def initialization(board_file):
    """Initialization of the game. Creation of the board and the heroes.

    Parameter:
    ----------
    board_file: Path of the file used to create the board (str)

    Returns:
    --------
    player_1: Level, number of point, etc. of the heroes of player 1 created (dict)
    player_2: Level, number of point, etc. of the heroes of player 2 created (dict)
    positions: Contains all the coordinates of the board (dict)
    ROWS: Number of rows of the board (int)
    COLUMNS: Number of columns of the board (int)
    nb_turns_wanted: Number of turns to be on the spur in order to win (int)
    creatures: Has every information of each creature (list)

    Version:
    --------
    specification: Zephyr Houyoux (v.3 02/04/19)
    implementation: Aude Lekeux (v.3 08/04/19)
    """

    player_1 = create_heroes()
    player_2 = create_heroes()

    ROWS, COLUMNS, NB_TURNS, positions, creatures = create_board(board_file, player_1, player_2)

    display_board(ROWS, COLUMNS, positions)

    return player_1, player_2, positions, ROWS, COLUMNS, NB_TURNS, creatures


def game(nb_spur_p1, nb_spur_p2, player_1, player_2, positions, creatures):
    """Starts a new turn if the game is not finished.

    Parameters:
    -----------
    nb_spur_p1: Number of turns a hero from player 1 is on spur (int)
    nb_spur_p2: Number of turns a hero from player 2 is on spur (int)
    player_1: Level, number of point, etc. of the heroes of player 1 (dict)
    player_2: Level, number of point, etc. of the heroes of player 2 (dict)
    positions: Contains all the coordinates of the board (dict)
    creatures: Has every information of each creature (list)

    Returns:
    --------
    nb_spur_p1: Number of turns a hero from player 1 is on spur (int)
    nb_spur_p2: Number of turns a hero from player 2 is on spur (int)
    positions: Contains all the coordinates of the board updated (dict)

    Version:
    --------
    specification: Zephyr Houyoux (v.5 08/04/19)
    implementation: Aude Lekeux (v.1 08/04/19)
    """

    choice1 = input('Player 1: Enter your orders for your heroes: ')
    choice2 = input('Player 2: Enter your orders for your heroes: ')

    positions, player_1, player_2, creatures = players_choice(choice1, positions, player_1, player_2, creatures)
    positions, player_1, player_2, creatures = players_choice(choice2, positions, player_1, player_2, creatures)

    player_1, player_2, positions, creatures = defeated(player_1, player_2, positions, creatures)

    nb_spur_p1, nb_spur_p2 = is_on_spur(nb_spur_p1, nb_spur_p2, player_1, player_2, positions)

    return nb_spur_p1, nb_spur_p2, positions


# Function 3
def create_board(board_file, player_1, player_2):
    """Creates the map and displays it.

    Parameter:
    ----------
    board_file: Path of the file used to create the board (str)
    player_1: Level, number of point, etc. of the heroes of player 1 (dict)
    player_2: Level, number of point, etc. of the heroes of player 2 (dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    creatures: Has every information of each creature (list)
    nb_turns_wanted: Number of turns to be on the spur in order to win (int)
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
    nb_turns_wanted = int(board[3])

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

    return ROWS, COLUMNS, nb_turns_wanted, positions, creatures


# Function 4
def create_heroes():
    """Takes the player's input, splits the information and stores it into a dictionary.

    Returns:
    --------
    player: Level, number of point, etc. of the heroes of player created (dict)

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
def is_game_over(nb_turns_wanted, nb_spur_p1, nb_spur_p2):
    """Checks whether the game is over or not.

    Parameters:
    -----------
    nb_turns_wanted: Number of turns to be on the spur in order to win (int)
    nb_spur_p1: Number of turns a hero from player 1 is on spur (int)
    nb_spur_p2: Number of turns a hero from player 2 is on spur (int)

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

    if nb_spur_p1 == nb_turns_wanted:
        print('Player1 won')
        return True
    elif nb_spur_p2 == nb_turns_wanted:
        print('Player2 won')
        return True

    # i_time = inactivity(positions, initial_positions, creatures, initial_creatures, inactivity_time)
    # print(i_time[0])
    # if i_time[0] >= 40:
    #     return True
    # else:
    #     return False


# Function 8
def creature_turn(positions, creatures, player1, player2):
    """Checks where a creature should attack or move depending on it's surrounding.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    creatures: Has every information of each creature (list)
    player1: Level, number of point, etc. of heroes of player1 (dict)
    player2: Level, number of point, etc. of heroes of player2 (dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    player1: Level, number of point, etc. of heroes of player1 updated (dict)
    player2: Level, number of point, etc. of heroes of player2 updated (dict)

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
    positions: Contains all the coordinates of the board (dict)
    initial_positions: Contains all the coordinates of the board and the heroes before changes (dict)
    creatures: Has every information of each creature (list)
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
def defeated(player1, player2, positions, creatures):
    """Whenever a hero or a creature is defeated.

    Parameters:
    -----------
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)
    creatures: Has every information of each creature (list)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    player1: Level, number of point, etc. of the heroes of player 1 updated (dict)
    player2: Level, number of point, etc. of the heroes of player 2 updated (dict)
    position: Contains all the coordinates of the board updated (dict)
    creatures: Has every information of each creature updated (list)

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
    for hero in player1:
        if player1[hero]['life_points'] <= 0:
            for key in positions:
                if positions[key] == 'spawn_player_1':
                    positions[hero] = key
                    # Reset life points of the hero depending on his class and level
                    player1 = reset(hero, player1)

    for hero in player2:
        if player2[hero]['life_points'] <= 0:
            for key in positions:
                if positions[key] == 'spawn_player_2':
                    positions[hero] = key
                    # Reset life points of the hero depending on his class and level
                    player2 = reset(hero, player2)

    print('The hero', hero, 'is respawning')

    # Delete a creature when it's defeated
    for key, value in positions.copy().items():
        if value[0] in creatures:
            if int(value[1]) <= 0:
                print('The creature', value[0], 'is dead')
                # If a creature is dead its victory points are distributed
                hero_count = 0
                hero_list = []
                for hero in positions:
                    if type(positions[hero]) is tuple:
                        print(positions[hero], key)
                        if gap_calculator(positions[hero], key) < 1.5:
                            hero_count += 1
                            hero_list.append(hero)
                points = math.ceil(int(positions[key][4]) / hero_count)
                for hero in hero_list:
                    if hero in player1:
                        player1[hero]['victory_points'] += points
                    elif hero in player2:
                        player2[hero]['victory_points'] += points
                del positions[key]
                del creatures[creatures.index(value[0])]

    return player1, player2, positions, creatures


def reset(hero, player):
    """Resets the data of the hero who has been defeated and respawning.

    Parameters:
    -----------
    hero: Name of the hero respawning (str)
    player: Level, number of point, etc. of the heroes of the player (dict)

    Returns:
    --------
    player: Level, number of point, etc. of the heroes of the player updated (dict)

    Version:
    --------
    specification: Aude Lekeux (v.1 10/04/19)
    implementation: Aude Lekeux (v.1 08/04/19)
    """

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

    return player


# Function 10
def players_choice(choice, positions, player1, player2, creatures):
    """Translates the player's order and calls the functions move or attack.

    Parameters:
    -----------
    choice: Order of the player (str)
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of heroes of player1 (dict)
    player2: Level, number of point, etc. of heroes of player2 (dict)
    creatures: Has every information of each creature (list)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    player1: Level, number of point, etc. of heroes of player1 updated (dict)
    player2: Level, number of point, etc. of heroes of player2 updated (dict)
    creatures: Has every information of each creature (list)

    Notes:
    ------
    The order of the player must be with the expected format = 'hero_name:@r-c', 'hero_name:*r-c'
    or 'hero_name:capacity'.
    @ stands for a movement, * stands for a simple attack or 'capacity' is the name of a special capacity
    a hero wants to use.

    Version:
    --------
    specification: Zéphyr Houyoux (v.7 09/04/19)
    implementation: Zéphyr Houyoux (v.5 09/04/19)
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
            move_coordinates = (result[item][1:3], result[item][4:6])
            positions = move(positions, item, move_coordinates)
        elif result[item][0] == '*':
            attack_coordinates = (result[item][1:3], result[item][4:6])
            positions, player1, player2, creatures = attack(positions, item, '', (0, 0), attack_coordinates, player1, player2, creatures)
        else:
            if type(result[item]) is tuple:
                name_capacity = result[item][0]
                coordinates = (result[item][1][0:2], result[item][1][3:5])
                positions, player1, player2, creatures = attack(positions, item, name_capacity, coordinates, (0, 0), player1, player2, creatures)
            else:
                name_capacity = result[item]
                positions, player1, player2, creatures = attack(positions, item, name_capacity, (0, 0), (0, 0), player1, player2, creatures)

    return positions, player1, player2, creatures


# Function 11
def attack(positions, hero, capacity, coordinates, attack, player1, player2, creatures):
    """Checks whether the hero can do the attack, if yes, does it, if no, the attack is ignored.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero: Name of the hero attacking (str)
    coordinates: Coordinates where the hero wants to use his special capacity (tuple)
    capacity: Name of the special capacity (str)
    attack: Where the attack is made (tuple)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)
    creatures: Has every information of each creature (list)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    player1: Level, number of point, etc. of the heroes of player 1 updated (dict)
    player2: Level, number of point, etc. of the heroes of player 2 updated (dict)
    creatures: Has every information of each creature (list)


    Notes:
    ------
    A hero can attack with a special capacity if he's on a level high enough, or he can do a simple attack.

    Version:
    --------
    specification: Zephyr Houyoux (v.5 09/04/19)
    implementation: Manon Michaux (v.3 09/04/19)
    """

    # If there's no capacity name then it's a simple attack
    if capacity == '':
        for key in positions:

            # If the hero attacks another hero
            if positions[key] == attack:
                if key in player1:
                    player1[key]['life_points'] -= player2[hero]['damage_points']
                elif key in player2:
                    player2[key]['life_points'] -= player1[hero]['damage_points']
                print('Hero', hero, 'has attacked', key)
                return positions, player1, player2, creatures

            # If the hero attacks a creature
            elif key == attack:
                if hero in player1:
                    positions[key][1] = int(positions[key][1]) - player1[hero]['damage_points']

                elif hero in player2:
                    positions[key][1] = int(positions[key][1]) - player2[hero]['damage_points']

                print('Hero', hero, 'has attacked', positions[key][0])

                # If the creature doesn't have enough life points left it's defeated
                if int(positions[key][1]) <= 0:
                    print(positions[key][0], 'has been defeated')

                return positions, player1, player2, creatures

    # If there's no position to attack then it's a special capacity
    elif attack == (0, 0):

        if hero in player1:
            hero_class = get_class(hero, player1)
            hero_level = get_level(hero, player1)
        elif hero in player2:
            hero_class = get_class(hero, player2)
            hero_level = get_level(hero, player2)

        # If hero is on level 1 he can't use a special capacity yet
        if hero_level == 1:
            print('You cannot use a special capacity yet')
            return positions, player1, player2, creatures
        else:
            # If hero on level 2 to 5 he can use a special capacity
            for level in range(2, 6):
                positions = special_capacity_usage(positions, hero, player, hero_level, hero_class, capacity, coordinates)
                return positions, player1, player2, creatures

    return positions, player1, player2, creatures


def special_capacity_usage(positions, hero, player, hero_level, hero_class, capacity, coordinates):
    """Verifies if a gero can use a special capacity or not.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero: Name of the hero using a special capacity (str)
    player: Level, number of point, etc. of the heroes of the player (dict)
    hero_level: Level of the hero wanting to use a special capacity (int)
    hero_class: Class of the hero wanting to use a special capacity (str)
    capacity: Name of the special capacity (str)
    coordinates: Coordinates where the hero wants to use his special capacity (tuple)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)

    Notes:
    ------
    Not every special capacity needs coordinates.
    Only immunise, fulgura, ovibus and reach need coordinates.

    Version:
    --------
    specification: Aude Lekeux (v.1 08/04/19)
    implementation: Aude Lekeux (v.1 08/04/19)
    """

    # If the hero is on level 2 he can only use one of his special capacity yet
    if hero_level == 2:
        # If the hero is a barbarian he can only use energise
        if hero_class == 'barbarian':
            if capacity != 'energise':
                print('You cannot use the capacity ' + capacity)
                return positions
            else:
                positions = energise(positions, hero, player)
                return positions

        # If the hero is a healer he can only use invigorate
        elif hero_class == 'healer':
            if capacity != 'invigorate':
                print('You cannot use the capacity ' + capacity)
                return positions
            else:
                positions = invigorate(positions, hero, player)
                return positions

        # If the hero is a mage he can only use fulgura
        elif hero_class == 'mage':
            if capacity != 'fulgura':
                print('You cannot use the capacity ' + capacity)
                return positions
            else:
                positions = fulgura(coordinates, positions, hero, player)
                return positions

        # If the hero is a rogue he can only use reach
        elif hero_class == 'rogue':
            if capacity != 'reach':
                print('You cannot use the capacity ' + capacity)
                return positions
            else:
                positions = reach(positions, hero, coordinates)
                return positions

    # If the hero is on level 3 or more he can use both of his special capacities
    elif hero_level >= 3:
        # Barbarian can use energise and stun
        if hero_class == 'barbarian':
            if capacity == 'energise':
                positions = energise(positions, hero, player)
                return positions
            elif capacity == 'stun':
                positions = stun(positions, player, creatures, hero)
                return positions

        # Healer can use invigorate and immunise
        elif hero_class == 'healer':
            if capacity == 'invigorate':
                positions = invigorate(positions, hero, player)
                return positions
            elif capacity == 'immunise':
                positions = immunise(positions, player, creatures, hero, coordinates)
                return positions

        # Mage can use fulgura and ovibus
        elif hero_class == 'mage':
            if capacity == 'fulgura':
                positions = fulgura(coordinates, positions, hero, player)
                return positions
            elif capacity == 'ovibus':
                positions = ovibus(positions, hero, coordinates, creatures)
                return positions

        # Rogue can use reach and burst
        elif hero_class == 'rogue':
            if capacity == 'reach':
                positions = reach(positions, hero, coordinates)
                return positions
            elif capacity == 'burst':
                positions = burst(positions, hero, creatures)
                return positions


# Function 12
def move(positions, hero, movement):
    """Checks if the position he will end on is allowed. Do it if it is allowed.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero: Name of the hero moving (str)
    movement: Coordinates the hero wants to go to (tuple)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)

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

    # Computes the gap between the position of the hero and where he wants to go
    gap = gap_calculator(positions[hero], movement)

    # If the hero is already on the position he wants to go on
    if movement[0] == positions[hero][0] and movement[1] == positions[hero][1]:
        print('Your are already in this position', hero)
        return positions
    # If the position the hero wants to go on is already taken
    for key in positions:
        if positions[key][0] == movement[0] and positions[key][1] == movement[1]:
            print('This position is already taken', key)
            return positions
    else:
        # If the gap is less than 1.5 he can move
        if gap < 1.5:
            positions = move_hero(hero, movement, positions)
            return positions
        else:
            print('This position is too far from where you are ' + hero)
            return positions


# Function 13
def update_level(player):
    """Checks if a hero can level up and upgrade their characteristics.

    Parameters:
    -----------
    player: Level, number of point, etc. of the heroes of the player (dict)

    Returns:
    --------
    player: Level, number of point, etc. of the heroes of the player updated (dict)

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
    hero: Name of the hero (str)

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


def summarize(player_1, initial_p1, player_2, initial_p2, nb_turns, initial_positions, positions, ROWS, COLUMNS, creatures):
    """Summarizes the state of the game.

    Parameters:
    -----------
    player_1: Level, number of point, etc. of heroes of player1 (dict)
    initial_p1: Level, number of point, etc. of heroes of player1 before changes (dict)
    player_2: Level, number of point, etc. of heroes of player2 (dict)
    initial_p2: Level, number of point, etc. of heroes of player2 before changes (dict)
    nb_turns: Number of turns of the game (int)
    initial_positions: Contains all the coordinates of the board before changes (dict)
    positions: Contains all the coordinates of the board (dict)
    ROWS: Number of rows of the board (int)
    COLUMNS: Number of columns of the board (int)
    creatures: Has every information of each creature (list)

    Returns:
    --------
    initial_positions: Contains all the coordinates of the board before next turn (dict)
    positions: Contains all the coordinates of the board (dict)
    initial_p1: Level, number of point, etc. of the heroes of player 1 before next turn (dict)
    initial_p2: Level, number of point, etc. of the heroes of player 2 before next turn (dict)
    creatures: Has every information of each creature (list)

    Version:
    --------
    specification: Manon Michaux (v.4 06/04/19)
    implementation: Aude Lekeux (v.3 06/04/19)
    """

    # for hero in positions:
    #     if positions[hero] != initial_positions[hero]:
    #         # Whenever a hero has been respawning
    #         for key, value in positions.copy().items():
    #             if positions[hero] == key:
    #                 print(hero + ' has been respawning to ' + str(key))

    player_1, player_2, positions, creatures = defeated(player_1, player_2, positions, creatures)

    # Whenever a hero leveled up he can use a special capacity
    for hero1 in player_1:
        if player_1[hero1]['level'] != initial_p1[hero1]['level']:
            special_capacity_available(player_1, hero1)
    for hero2 in player_2:
        if player_2[hero2]['level'] != initial_p2[hero2]['level']:
            special_capacity_available(player_2, hero2)

    # print('Creatures = ' + str(creatures))
    # print('Positions = ' + str(positions))
    # print('Number of turns played = ' + str(nb_turns))
    # print('Number of turns player is on spur = ' + str(nb_turns_player))
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
    player: Level, number of point, etc. of the heroes of the player (dict)

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
    player: Level, number of point, etc. of the heroes of the player (dict)

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
    player: Level, number of point, etc. of the heroes of the player (dict)

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
    player: Level, number of point, etc. of the heroes of the player (dict)

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
    player: Level, number of point, etc. of the heroes of the player (dict)

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


def is_on_spur(nb_spur_p1, nb_spur_p2, player1, player2, positions):
    """Checks whether a hero is on spur.

    Parameters:
    -----------
    nb_spur_p1: Number of turns a hero from player 1 is on spur (int)
    nb_spur_p2: Number of turns a hero from player 2 is on spur (int)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    nb_spur_p1: Number of turns a hero from player 1 is on spur (int)
    nb_spur_p2: Number of turns a hero from player 2 is on spur (int)

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    is_p1_on_spur = False
    is_p2_on_spur = False

    for item in positions:
        if positions[item] == 'spur':
            for hero in player1:
                if positions[hero] == item:
                    nb_spur_p1 += 1
                    is_p1_on_spur = True
            for hero in player2:
                if positions[hero] == item:
                    nb_spur_p2 += 1
                    is_p2_on_spur = True

    if is_p1_on_spur and is_p2_on_spur:
        nb_spur_p1 = 0
        nb_spur_p2 = 0

    return nb_spur_p1, nb_spur_p2


def move_hero(hero, new_position, positions):
    """Move from one cell to another.

    Parameters:
    -----------
    hero: Name of the hero (str)
    new_position: Position the character wants to go on (tuple)
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

    if hero in positions:
        positions[hero] = new_position

    return positions


def move_creatures(creature, start, new_position, positions, creatures):
    """Move from one cell to another.

    Parameters:
    -----------
    creature: Name of the creature (str)
    start: Position the character is on now (tuple)
    new_position: Position the character wants to go on (tuple)
    positions: Contains all the coordinates of the board (dict)
    creatures: Has every information of each creature (list)

    Returns:
    --------
    creatures: Has every information of each creature updated (list)
    positions: Contains all the coordinates of the board updated (dict)

    Notes:
    ------
    This function is called only when the movement can be executed.

    Version:
    --------
    specification: Aude Lekeux (v.1 07/04/19)
    implementation: Aude Lekeux (v.1 07/04/19)
    """

    if creature in creatures:
        for key, value in positions.copy().items():
            if key == start:
                # Adds the new position and deletes the previous one
                positions[new_position] = positions[key]
                del positions[key]

    return creatures, positions
