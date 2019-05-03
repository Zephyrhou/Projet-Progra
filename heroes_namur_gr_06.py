import math


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

    classes = ['barbarian', 'healer', 'mage', 'rogue']

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
                               'damage_points': 2, 'cooldown': 0}
            elif value == 'rogue':
                player[key] = {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2,
                               'cooldown': 0}
            elif value == 'healer':
                player[key] = {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0,
                               'damage_points': 2, 'cooldown': 0}
            elif value == 'mage':
                player[key] = {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2,
                               'cooldown': 0}

    return player


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

    nb_spur_p1, nb_spur_p2, is_p1_on_spur, is_p2_on_spur = is_on_spur(nb_spur_p1, nb_spur_p2, player_1, player_2,
                                                                      positions)

    return nb_spur_p1, nb_spur_p2, positions


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


def actions_turn(positions, player1, player2, creatures):
    """Determines the order of attacks / moves following the choices of both player and the creatures' ones.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    player1: All the data about the heroes of the first player (dict)
    player2: All the data about the heroes of the second player (dict)
    creatures: Contains all the data about creatures (dict)

    Returns:
    --------
    player1: All the data about the heroes of the first player (dict)
    player2: All the data about the heroes of the second player (dict)
    creatures: Contains all the data about creatures (dict)
    positions: Contains all the coordinates of the board (dict)
    """

    attacking = []
    moving = []

    # Split the orders within attacks and movements
    for character in positions:
        if character in creatures:
            if positions[character]['order'] == 'attack':
                attacking += character
            else:
                moving += character
        elif character in player1:
            if positions[character]['order'] == 'attack':
                attacking += character
            else:
                moving += character

        else:
            if positions[character]['order'] == 'attack':
                attacking += character
            else:
                moving += character

    # Execute the attacks
    for character in attacking:
        # First attacking : the creatures
        if character in creatures:
            hero_name = character
            name_attack = positions[character]['name_attack']
            attack_coord = positions[character]['where']
            attack(positions, hero_name, name_attack, (0, 0), attack_coord, player1, player2, creatures)
        # Then the heroes of the first player
        elif character in player1:
            hero_name = character
            name_attack = positions[character]['name_attack']
            attack_coord = positions[character]['where']
            attack(positions, hero_name, name_attack, (0, 0), attack_coord, player1, player2, creatures)
        # Finally the ones of the second player
        else:
            hero_name = character
            name_attack = positions[character]['name_attack']
            attack_coord = positions[character]['where']
            attack(positions, hero_name, name_attack, (0, 0), attack_coord, player1, player2, creatures)

    for character in moving:
        print(character, moving)
        # First moving : the creatures
        if character in creatures:
            hero_name = character
            movement_coord = positions[character]['where']
            move(hero_name, positions, movement_coord, player1, player2, creatures)

        # Then the heroes of the first player
        elif character in player1:
            hero_name = character
            movement_coord = positions[character]['where']
            move(hero_name, positions, movement_coord, player1, player2, creatures)

        # Finally the ones of the second player
        else:
            hero_name = character
            movement_coord = positions[character]['where']
            move(hero_name, positions, movement_coord, player1, player2, creatures)

    return player1, player2, positions, creatures


def infighting(character, positions, player1, player2):
    """Verifies if a hero is next to another hero or a creature.

    Parameters:
    -----------
    character: Name of the character (str)
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)

    Returns:
    --------
    is_infighting: If a character is next to the hero or not (bool)
    character: Name of the character which is next to the hero (str)

    Version:
    --------
    specification: Aude Lekeux (v.2 03/05/2019)
    implementation: Aude Lekeux (v.2 03/05/2019)
    """

    for key, value in positions.items():
        if type(positions[key]) is tuple:
            if type(positions[character]) is tuple:
                if character in player1 and key in player2:
                    if gap_calculator(positions[key], positions[character]) < 2:
                        return True, key
                elif character in player2 and key in player1:
                    if gap_calculator(positions[key], positions[character]) < 2:
                        return True, key
        else:
            return False, ''


def ally_in_zone(hero, positions, player1, player2):
    """Verifies if an ally is in the zone of the hero.

    Parameters:
    -----------
    hero: Name of the hero (str)
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)

    Returns:
    --------
    is_ally_in_zone: If an ally is in the zone of the hero or not (bool)
    ally: Name of the ally which is in the zone of the hero (str)

    Version:
    --------
    specification: Aude Lekeux (v.1 03/05/2019)
    implementation: Aude Lekeux (v.1 03/05/2019)
    """

    for ally in positions:
        if hero in player1:
            if ally in player2:
                if gap_calculator(positions[hero], positions[ally]) > 2:
                    return True, ally
        elif hero in player2:
            if ally in player1:
                if gap_calculator(positions[hero], positions[ally]) > 2:
                    return True, ally


def enemy_in_zone(hero, positions, player1, player2):
    """Verifies is an enemy is in the zone of the hero.

    Parameters:
    -----------
    hero: Name of the hero (str)
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)

    Returns:
    --------
    is_enemy_in_zone: If an enemy in the zone of the hero or not (bool)
    enemy: Name of the enemy which is in the zone of the hero (str)

    Version:
    --------
    specification: Aude Lekeux (v.1 03/05/2019)
    implementation: Aude Lekeux (v.1 03/05/2019)
    """

    for enemy in positions:
        if hero in player1:
            if enemy in player2:
                if gap_calculator(positions[hero], positions[enemy]) > 2:
                    return True, enemy
        elif hero in player2:
            if enemy in player1:
                if gap_calculator(positions[hero], positions[enemy]) > 2:
                    return True, enemy


def move_towards(hero, position, positions):
    """A hero wants to move towards a certain position

    Parameters:
    -----------
    hero: Name of the hero (str)
    position: Position where to move to (tuple)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    new_value: New position on the hero (tuple)

    Notes:
    ------
    A hero can only move in one of the eight boxes around him

    Version:
    --------
    specification: Aude Lekeux (v.2 03/05/2019)
    implementation: Aude Lekeux (v.2 03/05/2019)
    """

    for key, value in positions.copy().items():
        if key == hero:
            if type(position) is tuple:
                x_hero = int(value[0])
                y_hero = int(value[1])
                x_position = int(position[0])
                y_position = int(position[1])
                previous_value = value
                value = list(previous_value)
                # The result will be positive, negative or zero
                if (x_hero - x_position) == 0:
                    # Moves y
                    if y_hero < y_position:
                        y_hero += 1
                        value[1] = str(y_hero)
                    elif y_hero > y_position:
                        y_hero -= 1
                        value[1] = str(y_hero)
                else:
                    # Moves x
                    if x_hero < x_position:
                        x_hero += 1
                        value[0] = str(x_hero)
                    elif x_hero > x_position:
                        x_hero -= 1
                        value[0] = str(x_hero)

            new_value = tuple(value)
            return new_value


def get_ia_orders(positions, player1, player2, nb_spur_p1, nb_spur_p2, nb_turns, creatures):
    """Decides what each hero will do.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)
    nb_spur_p1: Number of turns a hero from player 1 is on spur (int)
    nb_spur_p2: Number of turns a hero from player 2 is on spur (int)
    nb_turns: Number of turns played (int)
    creatures: Has every information of each creature (list)

    Returns:
    --------
    choice: Orders for each hero (str)

    Version:
    --------
    specification: Aude Lekeux (v.3 03/05/2019)
    implementation: Aude Lekeux (v.3 03/05/2019)
    """

    # Choice of the IA is built as you go
    choice = ''
    hero_class = ''
    player = ''

    # Verify if a hero is on spur (si_p1_on_spur and is_p2_on_spur are needed for the function)
    nb_spur_p1, nb_spur_p2, is_p1_on_spur, is_p2_on_spur = is_on_spur(nb_spur_p1, nb_spur_p2, player1, player2,
                                                                      positions)

    # Initialises the variables needed for the rest of the function
    for hero in positions:
        if hero in player1 or hero in player2:
            if hero in player1:
                hero_class = player1[hero]['class']
                player = player1
                choice += str(hero)
            elif hero in player2:
                hero_class = player2[hero]['class']
                player = player2
                choice += str(hero)

            # Depending on the class of the hero
            # If hero is a barbarian
            if hero_class == 'barbarian':
                is_infighting, character = infighting(hero, positions, player1, player2)
                if is_infighting:
                    if available_attack('stun', player, hero):
                        choice += ':stun '
                    ally_is_in_zone, ally = ally_in_zone(hero, positions, player1, player2)
                    if ally_is_in_zone:
                        if available_attack('energise', player, hero):
                            choice += ':energise '
                    else:
                        # If no special capacity is available; do a simple attack
                        for position in positions:
                            if type(positions[position]) is tuple:
                                if gap_calculator(positions[hero], positions[position]) < 2:
                                    if hero != position:
                                        choice += ':*' + positions[position][0] + '-' + positions[position][1] + ' '
                else:
                    if nb_turns >= 20:
                        if hero in player1:
                            if is_p1_on_spur:
                                # Do nothing
                                choice += ': '
                        elif hero in player2:
                            if is_p2_on_spur:
                                # Do nothing
                                choice += ': '
                        else:
                            # Move towards spur
                            for key, value in positions.items():
                                if value == 'spur':
                                    new_position = move_towards(hero, key, positions)
                                    choice += ':@' + new_position[0] + '-' + new_position[1] + ' '
                    else:
                        # Move towards enemy
                        all_gaps = {}
                        for key, value in positions.items():
                            if key not in player:
                                if type(value) is tuple:
                                    all_gaps[value] = round(gap_calculator(positions[hero], value), 2)

                        smallest_gap = min(all_gaps)
                        new_position = move_towards(hero, smallest_gap, positions)
                        choice += ':@' + new_position[0] + '-' + new_position[1] + ' '

            # If hero is a healer
            elif hero_class == 'healer':
                ally_is_in_zone, ally = ally_in_zone(hero, positions, player1, player2)
                if ally_is_in_zone:
                    enemy_is_in_zone, enemy = enemy_in_zone(hero, positions, player1, player2)
                    if enemy_is_in_zone:
                        if available_attack('immunise', player, hero):
                            choice += ':immunise' + positions[ally][0] + '-' + positions[ally][1] + ' '
                    elif available_attack('invigorate', player, hero):
                        choice += ':invigorate '
                enemy_is_in_zone, enemy = enemy_in_zone(hero, positions, player1, player2)
                if enemy_is_in_zone:
                    # If no special capacity is available; do a simple attack
                    choice += ':*' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                else:
                    if nb_turns >= 20:
                        if hero in player1:
                            if is_p1_on_spur:
                                # Do nothing
                                choice += ': '
                        elif hero in player2:
                            if is_p2_on_spur:
                                # Do nothing
                                choice += ': '
                        else:
                            # Move towards spur
                            for key, value in positions.items():
                                if value == 'spur':
                                    new_position = move_towards(hero, key, positions)
                                    choice += ':@' + new_position[0] + '-' + new_position[1] + ' '
                    else:
                        # Move towards enemy
                        all_gaps = {}
                        for key, value in positions.items():
                            if key not in player:
                                if type(value) is tuple:
                                    all_gaps[value] = round(gap_calculator(positions[hero], value), 2)

                        smallest_gap = min(all_gaps)
                        new_position = move_towards(hero, smallest_gap, positions)
                        choice += ':@' + new_position[0] + '-' + new_position[1] + ' '

            # If hero is a mage
            elif hero_class == 'mage':
                is_infighting, enemy = infighting(hero, positions, player1, player2)
                enemy_is_in_zone, enemy = enemy_in_zone(hero, positions, player1, player2)
                if is_infighting or enemy_is_in_zone:
                    if available_attack('ovibus', player, hero):
                        choice += ':ovibus' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                    elif available_attack('fulgura', player, hero):
                        choice += ':fulgura' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                    else:
                        # If no special capacity is available; do a simple attack
                        choice += ':*' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                elif nb_turns >= 20:
                    if hero in player1:
                        if is_p1_on_spur:
                            # Do nothing
                            choice += ': '
                    elif hero in player2:
                        if is_p2_on_spur:
                            # Do nothing
                            choice += ': '
                    else:
                        # Move towards spur
                        for key, value in positions.items():
                            if value == 'spur':
                                new_position = move_towards(hero, key, positions)
                                choice += ':@' + new_position[0] + '-' + new_position[1] + ' '
                else:
                    # Move towards enemy
                    all_gaps = {}
                    for key, value in positions.items():
                        if key not in player:
                            if type(value) is tuple:
                                all_gaps[value] = round(gap_calculator(positions[hero], value), 2)

                    smallest_gap = min(all_gaps)
                    new_position = move_towards(hero, smallest_gap, positions)
                    choice += ':@' + new_position[0] + '-' + new_position[1] + ' '

            # If hero is a rogue
            elif hero_class == 'rogue':
                is_infighting, enemy = infighting(hero, positions, player1, player2)
                enemy_is_in_zone, enemy = enemy_in_zone(hero, positions, player1, player2)
                if is_infighting or enemy_is_in_zone:
                    if available_attack('burst', player, hero):
                        choice += ':burst' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                    elif available_attack('reach', player, hero):
                        choice += ':reach' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                    else:
                        # If no special capacity is available; do a simple attack
                        choice += ':*' + positions[enemy][0] + '-' + positions[enemy][1] + ' '
                elif nb_turns >= 20:
                    if hero in player1:
                        if is_p1_on_spur:
                            # Do nothing
                            choice += ': '
                    elif hero in player2:
                        if is_p2_on_spur:
                            # Do nothing
                            choice += ': '
                    else:
                        # Move towards spur
                        for key, value in positions.items():
                            if value == 'spur':
                                new_position = move_towards(hero, key, positions)
                                choice += ':@' + new_position[0] + '-' + new_position[1] + ' '
                else:
                    # Move towards enemy
                    all_gaps = {}
                    for key, value in positions.items():
                        if key not in player:
                            if type(value) is tuple:
                                all_gaps[value] = round(gap_calculator(positions[hero], value), 2)

                    smallest_gap = min(all_gaps)
                    new_position = move_towards(hero, smallest_gap, positions)
                    choice += ':@' + new_position[0] + '-' + new_position[1] + ' '

    # Removes the last char which is a space
    choice = choice[0:-1]
    print(choice)
    positions, player1, player2, creatures = players_choice(choice, positions, player1, player2, creatures)

    return positions, player1, player2, creatures


def available_attack(name_attack, player, hero):
    """Checks whether the hero can or not use a special capacity

    Parameters:
    -----------
    name_attack: Name of the special capacity the hero wants to use (str)
    player: Level, number of point, etc. of heroes of the player (dict)
    hero: Name of the hero using a special capacity (str)

    Return:
    -------
    availability: Whether the hero can use the special capacity or not (bool)

    Notes:
    ------
    availability is true if the hero can use the special capacity and false otherwise.

    Version:
    --------
    specification: Manon Michaux (v.2 26/04/19)
    implementation: Manon Michaux (v.3 01/05/19)
    """

    # If player is on level 1 he can't use a special capacity yet
    if player[hero]['level'] < 2:
        return False

    # Checks whether the cool down is at 0 or not
    if player[hero]['cooldown'] != 0:
        return False

    # Checks whether the hero has a level high enough in order to use a special capacity
    if player[hero]['class'] == 'barbarian':
        if name_attack == 'energise':
            if player[hero]['level'] >= 2:
                return True
        elif name_attack == 'stun':
            if player[hero]['level'] >= 3:
                return True
        else:
            return False

    elif player[hero]['class'] == 'healer':
        if name_attack == 'invigorate':
            if player[hero]['level'] >= 2:
                return True
        elif name_attack == 'immunise':
            if player[hero]['level'] >= 3:
                return True
        else:
            return False

    elif player[hero]['class'] == 'mage':
        if name_attack == 'fulgura':
            if player[hero]['level'] >= 2:
                return True
        elif name_attack == 'ovibus':
            if player[hero]['level'] >= 3:
                return True
        else:
            return False

    elif player[hero]['class'] == 'rogue':
        if name_attack == 'reach':
            if player[hero]['level'] >= 2:
                return True
        elif name_attack == 'burst':
            if player[hero]['level'] >= 3:
                return True
        else:
            return False


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
            positions = move(positions, item, move_coordinates, player1, player2, creatures)
        elif result[item][0] == '*':
            attack_coordinates = (result[item][1:3], result[item][4:6])
            positions, player1, player2, creatures = attack(positions, item, '', (0, 0), attack_coordinates, player1,
                                                            player2, creatures)
        else:
            if type(result[item]) is tuple:
                name_capacity = result[item][0]
                coordinates = (result[item][1][0:2], result[item][1][3:5])
                positions, player1, player2, creatures = attack(positions, item, name_capacity, coordinates, (0, 0),
                                                                player1, player2, creatures)
            else:
                name_capacity = result[item]
                positions, player1, player2, creatures = attack(positions, item, name_capacity, (0, 0), (0, 0), player1,
                                                                player2, creatures)

    return positions, player1, player2, creatures


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
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of heroes of player 1 (dict)
    player2: Level, number of point, etc. of heroes of player 2 (dict)

    Notes:
    ------
    A creature attacks or moves towards the closest enemy.
    It can also do nothing.

    Version:
    --------
    specification: Aude Lekeux (v.5 10/04/19)
    implementation: Manon Michaux (v.6 29/04/19)
    """

    all_gaps = {}
    creature = ''

    for creature in creatures:
        for key, value in positions.items():
            if value[0] == creature:
                for hero, position in positions.items():
                    if (hero in player1) or (hero in player2):
                        gap = gap_calculator(key, position)
                        # If a hero is next to a creature it attacks
                        if gap < int(value[3]):
                            positions, player1, player2, creatures = attack(positions, creature, '', (0, 0), position,
                                                                            player1, player2, creatures)
                        # If no hero is in its influence zone
                        else:
                            all_gaps[hero] = round(gap, 2)

    # If a creature can't attack it moves towards the closest hero
    smallest_gap = min(all_gaps)
    positions = move(positions, creature, positions[smallest_gap], player1, player2, creatures)

    return positions, player1, player2


def attack(positions, character, capacity, coordinates, attack, player1, player2, creatures):
    """Checks whether the hero can do the attack, if yes, does it, if no, the attack is ignored.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    character: Name of the hero attacking (str)
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

    # If a hero wants to attack
    if (character in player1) or (character in player2):
        hero = character
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
                        positions[key][1] = int(positions[key][1]) - get_damage_points(hero, player1)

                    elif hero in player2:
                        positions[key][1] = int(positions[key][1]) - get_damage_points(hero, player2)

                    print('Hero', hero, 'has attacked', positions[key][0])

                    # If the creature doesn't have enough life points left it's defeated
                    if int(positions[key][1]) <= 0:
                        print(positions[key][0], 'has been defeated')

                    return positions, player1, player2, creatures

        # If there's no position to attack then it's a special capacity
        elif attack == (0, 0):

            hero_class = 0
            hero_level = 0

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
                if hero in player1:
                    player = player1
                elif hero in player2:
                    player = player2
                # If hero on level 2 to 5 he can use a special capacity
                for level in range(2, 6):
                    positions = special_capacity_usage(positions, hero, player, hero_level, hero_class, capacity,
                                                       coordinates, creatures)
                return positions, player1, player2, creatures

    # If a creature wants to attack
    damage_points = 0
    for key, value in positions.items():
        if value[0] == character:
            damage_points = int(value[2])

    if character in creatures:
        for key, value in positions.items():
            if value == attack:
                if key in player1:
                    player1[key]['life_points'] -= damage_points
                    print('Hero', key, 'was attacked by', character, 'and lost', damage_points, 'life points and has '
                          'now', player1[key]['life_points'], 'life points left')
                elif key in player2:
                    player2[key]['life_points'] -= damage_points
                    print('Hero', key, 'was attacked by', character, 'and lost', damage_points, 'life points and has '
                          'now', player2[key]['life_points'], 'life points left')

    return positions, player1, player2, creatures


def special_capacity_display(player, hero):
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

    if get_level(hero, player) == 2:
        if get_class(hero, player) == 'barbarian':
            print('The hero ' + hero + ' can now use the capacity energise')
        if get_class(hero, player) == 'healer':
            print('The hero ' + hero + ' can now use the capacity invigorate')
        if get_class(hero, player) == 'mage':
            print('The hero ' + hero + ' can now use the capacity fulgura')
        if get_class(hero, player) == 'rogue':
            print('The hero ' + hero + ' can now use the capacity reach')

    if get_level(hero, player) == 3:
        if get_class(hero, player) == 'barbarian':
            print('The hero ' + hero + ' can now use the capacity stun')
        if get_class(hero, player) == 'healer':
            print('The hero ' + hero + ' can now use the capacity immunise')
        if get_class(hero, player) == 'mage':
            print('The hero ' + hero + ' can now use the capacity ovibus')
        if get_class(hero, player) == 'rogue':
            print('The hero ' + hero + ' can now use the capacity burst')


def special_capacity_usage(positions, hero, player, hero_level, hero_class, capacity, coordinates, creatures):
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


def move(positions, character, movement, player1, player2, creatures):
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
    implementation: Zephyr Houyoux (v.6 01/05/19)
    """

    if (character in player1) or (character in player2):
        hero = character
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

    # Now movement if the position of the hero closest to the creature
    elif character in creatures:
        for key, value in positions.copy().items():
            if value[0] == character:
                x_creature = int(key[0])
                y_creature = int(key[1])
                x_hero = int(movement[0])
                y_hero = int(movement[1])
                previous_key = key
                key = list(key)
                # The result will be positive, negative or zero
                if (x_creature - x_hero) == 0:
                    # Moves y
                    if y_creature < y_hero:
                        y_creature += 1
                        key[1] = str(y_creature)
                    elif y_creature > y_hero:
                        y_creature -= 1
                        key[1] = str(y_creature)
                else:
                    # Moves x
                    if x_creature < x_hero:
                        x_creature += 1
                        key[0] = str(x_creature)
                    elif x_creature > x_hero:
                        x_creature -= 1
                        key[0] = str(x_creature)

                # Deletes the previous one and replaces it by the new position
                new_key = tuple(key)
                positions[new_key] = value
                del positions[previous_key]
                return positions


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
        if get_victory_points(hero, player) < 100:
            print('Hero ' + hero + ' remains on level 1')
            player[hero]['level'] = 1
            player[hero]['life_points'] = 10
            player[hero]['damage_points'] = 2
        # If hero is over 100 points
        else:
            if get_class(hero, player) == 'barbarian':
                if get_victory_points(hero, player) < 200:
                    player[hero]['level'] = 2
                    player[hero]['life_points'] = 13
                    player[hero]['damage_points'] = 3
                elif get_victory_points(hero, player) < 400:
                    player[hero]['level'] = 3
                    player[hero]['life_points'] = 16
                    player[hero]['damage_points'] = 4
                elif get_victory_points(hero, player) < 800:
                    player[hero]['level'] = 4
                    player[hero]['life_points'] = 19
                    player[hero]['damage_points'] = 5
                elif get_victory_points(hero, player) > 800:
                    player[hero]['level'] = 5
                    player[hero]['life_points'] = 22
                    player[hero]['damage_points'] = 6
            elif get_class(hero, player) == 'healer':
                if get_victory_points(hero, player) < 200:
                    player[hero]['level'] = 2
                    player[hero]['life_points'] = 11
                    player[hero]['damage_points'] = 2
                elif get_victory_points(hero, player) < 400:
                    player[hero]['level'] = 3
                    player[hero]['life_points'] = 12
                    player[hero]['damage_points'] = 3
                elif get_victory_points(hero, player) < 800:
                    player[hero]['level'] = 4
                    player[hero]['life_points'] = 13
                    player[hero]['damage_points'] = 3
                elif get_victory_points(hero, player) > 800:
                    player[hero]['level'] = 5
                    player[hero]['life_points'] = 14
                    player[hero]['damage_points'] = 4
            elif get_class(hero, player) == 'mage':
                if get_victory_points(hero, player) < 200:
                    player[hero]['level'] = 2
                    player[hero]['life_points'] = 12
                    player[hero]['damage_points'] = 3
                elif get_victory_points(hero, player) < 400:
                    player[hero]['level'] = 3
                    player[hero]['life_points'] = 14
                    player[hero]['damage_points'] = 4
                elif get_victory_points(hero, player) < 800:
                    player[hero]['level'] = 4
                    player[hero]['life_points'] = 16
                    player[hero]['damage_points'] = 5
                elif get_victory_points(hero, player) > 800:
                    player[hero]['level'] = 5
                    player[hero]['life_points'] = 18
                    player[hero]['damage_points'] = 6
            elif get_class(hero, player) == 'rogue':
                if get_victory_points(hero, player) < 200:
                    player[hero]['level'] = 2
                    player[hero]['life_points'] = 12
                    player[hero]['damage_points'] = 3
                elif get_victory_points(hero, player) < 400:
                    player[hero]['level'] = 3
                    player[hero]['life_points'] = 14
                    player[hero]['damage_points'] = 4
                elif get_victory_points(hero, player) < 800:
                    player[hero]['level'] = 4
                    player[hero]['life_points'] = 16
                    player[hero]['damage_points'] = 5
                elif get_victory_points(hero, player) > 800:
                    player[hero]['level'] = 5
                    player[hero]['life_points'] = 18
                    player[hero]['damage_points'] = 6
            print('Hero ' + hero + ' has increased to level ' + str(player[hero]['level']))

    return player


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
        if get_life_points(hero, player1) <= 0:
            for key in positions:
                if positions[key] == 'spawn_player_1':
                    positions[hero] = key
                    # Reset life points of the hero depending on his class and level
                    player1 = reset(hero, player1)

    for hero in player2:
        if get_life_points(hero, player2) <= 0:
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

    if get_class(hero, player) == 'barbarian':
        if get_level(hero, player) == 1:
            player[hero]['life_points'] = 10
        elif get_level(hero, player) == 2:
            player[hero]['life_points'] = 13
        elif get_level(hero, player) == 3:
            player[hero]['life_points'] = 16
        elif get_level(hero, player) == 4:
            player[hero]['life_points'] = 19
        elif get_level(hero, player) == 5:
            player[hero]['life_points'] = 22
    elif get_class(hero, player) == 'healer':
        if get_level(hero, player) == 1:
            player[hero]['life_points'] = 10
        elif get_level(hero, player) == 2:
            player[hero]['life_points'] = 11
        elif get_level(hero, player) == 3:
            player[hero]['life_points'] = 12
        elif get_level(hero, player) == 4:
            player[hero]['life_points'] = 13
        elif get_level(hero, player) == 5:
            player[hero]['life_points'] = 14
    elif get_class(hero, player) == 'mage':
        if get_level(hero, player) == 1:
            player[hero]['life_points'] = 10
        elif get_level(hero, player) == 2:
            player[hero]['life_points'] = 12
        elif get_level(hero, player) == 3:
            player[hero]['life_points'] = 14
        elif get_level(hero, player) == 4:
            player[hero]['life_points'] = 16
        elif get_level(hero, player) == 5:
            player[hero]['life_points'] = 18
    elif get_class(hero, player) == 'rogue':
        if get_level(hero, player) == 1:
            player[hero]['life_points'] = 10
        elif get_level(hero, player) == 2:
            player[hero]['life_points'] = 12
        elif get_level(hero, player) == 3:
            player[hero]['life_points'] = 14
        elif get_level(hero, player) == 4:
            player[hero]['life_points'] = 16
        elif get_level(hero, player) == 5:
            player[hero]['life_points'] = 18

    return player


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

    return nb_spur_p1, nb_spur_p2, is_p1_on_spur, is_p2_on_spur


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

    player_1, player_2, positions, creatures = defeated(player_1, player_2, positions, creatures)

    # Whenever a hero leveled up he can use a special capacity
    for hero1 in player_1:
        if get_level(hero1, player_1) != get_level(hero1, initial_p1):
            special_capacity_display(player_1, hero1)
    for hero2 in player_2:
        if get_level(hero2, player_2) != get_level(hero2, initial_p2):
            special_capacity_display(player_2, hero2)

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
            return player[hero]['class']


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
            return player[hero]['level']


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
            return player[hero]['life_points']


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
            return player[hero]['victory_points']


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
            return player[hero]['damage_points']


# Special Capacities
# Mage
def fulgura(coordinates, player1, player2, creatures, hero_name, positions):
    """ The creature / ennemy on the target coordinates loses a given number of health points.

    Parameters:
    -----------
    coordinates: Where the hero wants to use ovibus(tupl)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)
    creatures: Has every information of each creature (list)
    hero_name: Name of the hero (str)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    creatures: Has every information of each creature updated (list)
    positions: Contains all the coordinates of the board updated (dict)

    Version:
    --------
    specification: Manon Michaux (v.2 31/03/19)
    implementation: Manon Michaux (v.2 31/03/19)
    """

    good, updated = good(hero_name)
    used = 0

    # Level of the hero = 2
    if good[hero_name]['level'] == 2:
        if gap_calculator(positions, hero_name, coordinates) == 1:
            # For the heroes of the other player
            for heroes in updated:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    updated[heroes]['life_points'] -= 3
                    used += 1
                    print(" %s 's health points have been decreased by 3 " % heroes)
                else:
                    print("%s 's damage points haven't been modified " % heroes)
            # For the creatures
            for enemies in creatures:
                if gap_calculator(positions, hero_name, enemies) == 0:
                    creatures[enemies]['life_points'] -= 3
                    used += 1
                    print(" %s 's health points have been decreased by 3" % enemies)
                else:
                    print("%s 's damage points haven't been modified " % enemies)

            else:
                print("%s 's damage points haven't been modified " % enemies)

    # Level of the hero = 3
    elif good[hero_name][level] == 3:
        if gap_calculator(positions, hero_name, coordinates) <= 2:  # For the heroes of the other player
            for heroes in updated:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    updated[heroes][h_points] -= 3
                    used += 1
                    print(" %s 's health points have been decreased by 3 " % heroes)
                else:
                    print("%s 's damage points haven't been modified " % heroes)
            # For the creatures
            for enemies in creatures:
                if gap_calculator(positions, hero_name, enemies) == 0:
                    creatures[enemies][h_points] -= 3
                    used += 1
                    print(" %s 's health points have been decreased by 3" % enemies)
                else:
                    print("%s 's damage points haven't been modified " % enemies)

            else:
                print("%s 's damage points haven't been modified " % enemies)

    # Level of the hero = 4
    elif good[hero_name][level] == 4:
        if gap_calculator(positions, hero_name, coordinates) <= 3:  # For the heroes of the other player
            for heroes in updated:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    updated[heroes][h_points] -= 4
                    used += 1
                    print(" %s 's health points have been decreased by 4 " % heroes)
                else:
                    print("%s 's damage points haven't been modified " % heroes)
            # For the creatures
            for enemies in creatures:
                if gap_calculator(positions, hero_name, enemies) == 0:
                    creatures[enemies][h_points] -= 4
                    used += 1
                    print(" %s 's health points have been decreased by 4" % enemies)
                else:
                    print("%s 's damage points haven't been modified " % enemies)

            else:
                print("%s 's damage points haven't been modified " % enemies)

    # Level of the hero = 5
    elif good[hero_name][level] == 5:
        if gap_calculator(positions, hero_name, coordinates) <= 4:  # For the heroes of the other player
            for heroes in updated:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    updated[heroes][h_points] -= 4
                    used += 1
                    print(" %s 's health points have been decreased by 4 " % heroes)
                else:
                    print("%s 's damage points haven't been modified " % heroes)
            # For the creatures
            for enemies in creatures:
                if gap_calculator(positions, hero_name, enemies) == 0:
                    creatures[enemies][h_points] -= 4
                    used += 1
                    print(" %s 's health points have been decreased by 4" % enemies)
                else:
                    print("%s 's damage points haven't been modified " % enemies)

            else:
                print("%s 's damage points haven't been modified " % enemies)

    # Level of the hero = 1 or = 2
    else:
        print(" You can't use this attack yet")

    # Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        good[hero_name][cooldown][fulgura] += 1
    else:
        print("You used stun but nothing happened ")

    return updated, creatures, good


def ovibus(positions, hero_name, coordinates, creatures):
    """The creature/ennemy on the target coordinates is unable to act during a given number of turn.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    coordinates: Where the hero wants to use ovibus(tupl)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)
    creatures: Has every information of each creature (list)

    Returns:
    --------
    updated: Updated dictionary of the player which hero isn't using this attack.
    good: Updated dictionary of the player which hero is using this attack.
    creatures: Has every information of each creature updated(list)

    Version:
    --------
    specification: Manon Michaux (v.1 29/03/19)
    implementation: Manon Michaux (v.1 29/03/19)
    """

    good, updated = good(hero_name)

    # Level of the hero = 3
    if good[hero_name][level] == 3:
        if gap_calculator(positions, hero_name, coordinates) == 1:
            # For the heroes of the player
            for heroes in updated:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    used += 1
                    print("%s is confused for one turn" % heroes)

                else:
                    print("Those coordinates don't belong to %s" % heroes)

            # For the creatures
            for ennemy in creatures:
                if gap_calculator(positions, coordinates, ennemy) == 0:
                    used += 1
                    print("%s is confused for one turn" % heroes)
                else:
                    print("Those coordinates don't belong to %s" % heroes)

            print("The coordinates you tried to reach are too far away right now")

    # Level of the hero = 4
    elif good[hero_name][level] == 4:
        if gap_calculator(positions, hero_name, coordinates) <= 2:  # For the heroes of the player
            for heroes in updated:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    used += 1
                    print("%s is confused for one turn" % heroes)

                else:
                    print("Those coordinates don't belong to %s" % heroes)

            # For the creatures
            for ennemy in creatures:
                if gap_calculator(positions, coordinates, ennemy) == 0:
                    used += 1
                    print("%s is confused for one turn" % heroes)
                else:
                    print("Those coordinates don't belong to %s" % heroes)

            print("The coordinates you tried to reach are too far away right now")

    # Level of the hero = 5
    elif good[hero_name][level] == 5:
        if gap_calculator(positions, hero_name, coordinates) <= 3:  # For the heroes of the player
            for heroes in updated:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    used += 1
                    print("%s is confused for one turn" % heroes)

                else:
                    print("Those coordinates don't belong to %s" % heroes)

            # For the creatures
            for ennemy in creatures:
                if gap_calculator(positions, coordinates, ennemy) == 0:
                    used += 1
                    print("%s is confused for one turn" % heroes)
                else:
                    print("Those coordinates don't belong to %s" % heroes)

            print("The coordinates you tried to reach are too far away right now")

    # Level of the hero = 1 or = 2
    else:
        print("You can't use this attack yet")

    # Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        good[hero_name][cooldown][ovibus] += 3
    else:
        print("You used stun but nothing happened ")

    return updated, good, creatures


# Healer
def invigorate_level(hero, type, level_hero, level_ally, updated):
    """If a hero want's to use invigorate.

    Parameters:
    -----------
    hero: Name of the hero using invigorate (str)
    type: Type of the hero (str)
    level_hero: Level of the hero (int)
    level_ally: Level of the ally (int)
    updated: Updated dictionary of the player which hero's using this attack (dict)

    Returns:
    --------
    updated: Updated dictionary of the player which hero's using this attack (dict)

    Version:
    --------
    specification: Aude Lekeux (v.1 03/04/19)
    implementation: Aude Lekeux (v.1 03/04/19)
    """

    # Level of the hero equals 2
    if level_hero == 2:
        if updated[hero]['level'] == level_ally:
            if updated[hero]['life_points'] < max_life_points[type][level]:
                updated[hero]['life_points'] += 1
                print(hero + "' health points have been increased by one for this turn")
            else:
                print(hero + "' health points haven't been modified")

    # Level of the hero from 3 to 5
    elif level_hero >= 3:
        if updated[hero]['level'] == level_ally:
            max_health = max_life_points[type][level_ally] - (level_hero - 1)
            if updated[hero]['life_points'] <= max_health:
                updated[hero]['life_points'] += (level_hero - 1)
                print(hero + "' health points have been increased by one for this turn")
            else:
                print(hero + "' health points haven't been modified")

    return updated


def invigorate(positions, hero_name, player):
    """Raise the health points of the allies in the hero's wage.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    player: Level, number of point, etc. of the heroes of player (dict)
    max_health_dict: Dictionary containing for each class and for each level their own maximum of health points (dict)

    Returns:
    --------
    updated: Updated dictionary of the player which hero's using this attack (dict)

    Version:
    --------
    specification: Manon Michaux (v.2 27/03/19)
    implementation: Manon Michaux (v.4 03/04/19)
    """

    updated, bad_dict = good(hero_name)
    used = 0

    # Level of the hero from 2 to 5
    for level_hero in range(2, 6):
        if updated[hero_name]['level'] == level_hero:
            for heroes in updated:
                if gap_calculator(positions, hero_name, heroes) == level_hero - 1:

                    for type in dict_job:
                        if updated[heroes]['job'] == type:
                            # Level of the ally from 1 to 5
                            for level_ally in range(1, 6):
                                updated = invigorate_level(heroes, type, level_hero, level_ally, updated)
                        else:
                            print(" Class isn't correct")

    # Level of the hero equals 1
    else:
        print(" You can't use this attack yet")

    # Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        good(hero_name)['cooldown']['stun'] += 1
    else:
        print("You used stun but nothing happened")

    return updated


def immunise(positions, player, creatures, hero_name, coordinates):
    """

    :return:
    """


# Barbarian
def energise_level(level, updated, positions, hero_name):
    """When a hero want's to use energise depending on their level.

    Parameters:
    -----------
    level: Level of the hero (str)
    updated: Updated dictionary of the player which hero's using this attack (dict)
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero using energise (str)

    Returns:
    --------
    updated: Updated dictionary of the player which hero's using this attack (dict)

    Version:
    --------
    specification: Aude Lekeux (v.1 03/04/19)
    implementation Aude Lekeux (v.1 03/04/19)
    """

    if level == 2:
        for heroes in updated:
            if gap_calculator(positions, hero_name, heroes) == 1:
                updated[heroes]['damage_points'] += 1
                print(heroes + "'s damage points have been increased by 1 for this turn")
            else:
                print(heroes + "' damage points haven't been modified")

    else:
        for heroes in updated:
            if gap_calculator(positions, hero_name, heroes) <= level - 1:
                updated[heroes]['damage_points'] += level - 2
                print(heroes + "'s damage points have been increased by 1 for this turn")
            else:
                print(heroes + "%s ' damage points haven't been modified")

    return updated


def energise(positions, hero_name, player):
    """Raise the damage points of the allies in the hero's influence wage.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    player: Level, number of point, etc. of the heroes of the player (dict)

    Returns:
    --------
    updated_dict: Updated dictionary of the player which hero's using this attack (dict)

    Version:
    --------
    specification: Manon Michaux (v.4 27/03/19)
    implementation: Manon Michaux (v.3 26/03/19)
    """

    updated, bad_dict = good(hero_name)
    used = 0

    # Level of the hero from 1 to 5
    for level in range(1, 6):
        # Level from 2 to 5
        if level < 1:
            if updated[hero_name]['level'] == level:
                used, updates = energise_level(level, updated, used, positions, hero_name)

        # Level of the hero = 1
        else:
            print(" You can't use this special attack yet")

    # Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        updated[hero_name]['cooldown']['energise'] += 1
    else:
        print("You used energise but nothing happened")

    return updated


def stun_level(type, level, updated, hero_name, positions, used, creatures):
    """When a hero want's to use stun.

    Parameters:
    -----------
    type: Type of the hero (str)
    level: Level of the hero (int)
    updated: Updated dictionary of the player which hero's using this attack (dict)
    hero_name: Name of the hero using stun (str)
    positions: Contains all the coordinates of the board (dict)
    creatures: Has every information of each creature (list)

    Returns:
    --------
    positions: Contains all the coordinates of the board (dict)

    Version:
    --------
    specification: Aude Lekeux (v.1 03/04/19)
    implementation: Aude Lekeux (v.1 03/04/19)
    """

    if type == 'hero':
        for heroes in updated:
            if gap_calculator(positions, hero_name, heroes) == level - 2:
                if updated[heroes]['damage_points'] >= level - 1:
                    updated[heroes]['damage_points'] -= level - 2
                    used += 1
                    print(heroes + "'s damage points have been decreased by 1 for this turn")
                else:
                    print(heroes + "'s damage points haven't been modified")

            else:
                print(heroes + "'s damage points haven't been modified")

    elif type == 'creature':
        for enemies in creatures:
            if gap_calculator(positions, hero_name, enemies) == level - 2:
                if creatures[enemies]['damage_points'] >= level - 1:
                    creatures[enemies]['damage_points'] -= level - 2
                    used += 1
                    print(enemies + "'s damage points have been decreased by 1 for this turn")
                else:
                    print(enemies + "'s damage points haven't been modified")

            else:
                print(enemies + "'s damage points haven't been modified")

    return used, positions


def stun(positions, creatures, hero_name):
    """ Stun the ennemies ( both heroes and creatures) in the hero's wage.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    player: Level, number of point, etc. of the heroes of the player (dict)
    creatures: Has every information of each creature (list)
    hero_name: Name of the hero (str)

    Returns:
    --------
    updated: Dictionary of the enemy (dict)
    creatures: Has every information of each creature updated (list)
    good: Dictionary of the player which hero's using tha attack (dict)

    Version:
    --------
    specification: Manon Michaux (v.4 27/03/19)
    implementation: Manon Michaux (v.2 26/03/19)
    """

    good, updated = good(hero_name)
    used = 0

    # Level from 1 to 5
    for level in range(1, 6):
        # Level of the hero from 3 to 5
        if level > 2:
            if updated[hero_name]['level'] == level:
                stun_level('hero', level, updated, hero_name, positions, used, creatures)
        # Level of the hero from 1 to 2
        else:
            print(" You can't use this attack yet")

    # Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        good(hero_name)['cooldown']['stun'] += 1
    else:
        print("You used stun but nothing happened")

    return updated, creatures, good


# Rogue
def reach_level(level, updated, hero_name, positions, coordinates, used):
    """When a hero wants to use reach depending on his level.

    Parameters:
    -----------
    level: Level the hero is on (int)
    updated: Updated dictionary of the player which hero is using this attack (dict)
    hero_name: Name of the hero (str)
    positions: Contains all the coordinates of the board (dict)
    coordinates: Where the hero wants to use ovibus (tuple)

    Returns:
    --------
    updated: Updated dictionary of the player which hero is using this attack (dict)
    positions: Contains all the coordinates of the board updated (dict)

    Version:
    --------
    specification: Aude Lekeux (v.1 04/04/19)
    implementation: Aude Lekeux (v.1 04/04/19)
    """

    character_list = []
    unoccupied = 0

    if updated[hero_name]['level'] == level:
        if gap_calculator(positions[hero_name], coordinates) == level - 1:

            # For the all the characters in positions
            for characters in positions:
                if gap_calculator(positions[characters], coordinates) == 0:
                    print(characters + "is already on those coordinates right now")
                else:
                    unoccupied += 1
                character_list += characters
        else:
            print("The coordinates you tried to reach are too far away right now")

        # If none of the characters are on the target coordinates
        if unoccupied == len(character_list):
            positions[hero_name] = coordinates
            used += 1

    return updated, positions, used


def reach(positions, hero_name, coordinates):
    """Teleports the hero using the attack if he is the first using reach this turn and if the target coordinates aren't occupied.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    coordinates: Where the hero wants to use ovibus (tupl)

    Returns:
    --------
    positions: Contains all the coordinates of the board (dict)
    updated: Updated dictionary of the player which hero is using this attack (dict)

    Version:
    --------
    specification: Manon Michaux (v.2 03/04/19)
    implementation: Manon Michaux (v.3 04/04/19)
    """

    updated, bad_dict = good(hero_name)
    used = 0

    # Level of the hero from 1 to 5
    for level in range(2, 6):
        # Level from 3 to 5
        if level in range(3, 6):
            updated, positions, used = reach_level(level, updated, hero_name, positions, coordinates, used)
        # Level from 1 to 2
        else:
            print("You can't use this attack yet")

    # Adding the cooldown to the dictionary of the player if he attack has been used
    if used == 1:
        good[hero_name]['cooldown']['ovibus'] += 1
    else:
        print("You used stun but nothing happened ")

    return positions, updated


def burst_level(level, hero_name, positions, updated, creatures, used):
    """When a hero wants to use burst depending on his level.

    Parameters:
    -----------
    level: Level the hero is on (int)
    hero_name: Name of the hero (str)
    positions: Contains all the coordinates of the board (dict)
    updated: Updated dictionary of the player which hero's using this attack (dict)
    creatures: Has every information of each creature (list)

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    updated: Updated dictionary of the player which hero's using this attack (dict)
    creatures: Has every information of each creature updated (list)

    Version:
    --------
    specification: Aude Lekeux (v.1 04/04/19)
    implementation: Aude Lekeux (v.1 04/04/19)
    """

    if good[hero_name]['level'] == level:

        # For heroes of the other player
        for heroes in updated:
            # If level equals 3
            if level == 3:
                if gap_calculator(positions[hero_name], positions[heroes]) == 1:
                    updated[heroes]['life_points'] -= 1
                    used += 1
                    print(hero_name + "'s health points have been decreased by 1")
                else:
                    print(hero_name + "' health points haven't been modified")
            # Level from 4 to 5
            else:
                if gap_calculator(positions[hero_name], positions[heroes]) <= level - 2:
                    updated[heroes]['life_points'] -= level - 2
                    used += 1
                    print(hero_name + "'s health points have been decreased by 1")
                else:
                    print(hero_name + "' health points haven't been modified")

        # For the creatures
        for enemies in creatures:
            # If level equals 3
            if level == 3:
                if gap_calculator(positions[hero_name], positions[enemies]) == 1:
                    updated[enemies]['life_points'] -= 1
                    used += 1
                    print(enemies + "'s health points have been decreased by 1")
                else:
                    print(enemies + "' health points haven't been modified")
            # Level from 4 to 5
            else:
                if gap_calculator(positions[hero_name], positions[enemies]) <= level - 2:
                    updated[enemies]['life_points'] -= level - 2
                    used += 1
                    print(enemies + "'s health points have been decreased by 1")
                else:
                    print(enemies + "' health points haven't been modified")

    return positions, updated, creatures, used


def burst(positions, hero_name, creatures):
    """The creatures/ennemies in the hero's wage lose a given number of health points.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    creatures: Has every information of each creature list)

    Returns:
    --------
    updated: Updated dictionary of the player which hero's using this attack.
    good: Updated dictionary of the player which hero is using this attack.
    creatures: Has every information of each creature updated (list)

    Version:
    --------
    specification: Manon Michaux (v.2 03/04/19)
    implementation: Manon Michaux (v.2 04/04/19)
    """

    good, updated = good(hero_name)
    used = 0

    # Level of the hero from 1 to 5
    for level in range(1, 6):
        # Level from 3 to 5
        if level in range(3, 6):
            positions, updated, creatures, used = burst_level(level, hero_name, positions, updated, creatures, used)
        # Level of the hero from 1 to 2
        else:
            print(" You can't use this special attack yet")

    # Adding the cooldown to the dictionary of the player if the attack has been used
    if used >= 1:
        updated[hero_name]['cooldown'][burst] += 1
    else:
        print("You used burst but nothing happened")

    return updated, good, creatures


# launch('board.txt')
