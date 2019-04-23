from heroes_namur_gr_06 import *


def launch(board_file):

    player1, player2, positions, ROWS, COLUMNS, NB_TURNS, creatures = initialization(board_file)

    nb_turn = 0
    nb_spur_p1 = 0
    nb_spur_p2 = 0

    # While the game is not over the next turn begins
    while not is_game_over(NB_TURNS, nb_spur_p1, nb_spur_p2):
        nb_spur_p1, nb_spur_p2, positions = game(nb_spur_p1, nb_spur_p2, player1, player2, positions, creatures)
        display_board(ROWS, COLUMNS, positions)
        nb_turn += 1


def initialization(board_file):

    player_1 = create_heroes()
    player_2 = create_heroes()

    ROWS, COLUMNS, NB_TURNS, positions, creatures = create_board(board_file, player_1, player_2)

    display_board(ROWS, COLUMNS, positions)

    return player_1, player_2, positions, ROWS, COLUMNS, NB_TURNS, creatures


def game(nb_spur_p1, nb_spur_p2, player_1, player_2, positions, creatures):

    choice1 = input('Player 1: Enter your orders for your heroes: ')
    choice2 = input('Player 2: Enter your orders for your heroes: ')

    positions, player_1, player_2, creatures = players_choice(choice1, positions, player_1, player_2, creatures)
    positions, player_1, player_2, creatures = players_choice(choice2, positions, player_1, player_2, creatures)

    player_1, player_2, positions, creatures = defeated(player_1, player_2, positions, creatures)

    nb_spur_p1, nb_spur_p2 = is_on_spur(nb_spur_p1, nb_spur_p2, player_1, player_2, positions)

    return nb_spur_p1, nb_spur_p2, positions


def create_heroes():
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
                player[key] = {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}
            elif value == 'rogue':
                player[key] = {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}
            elif value == 'healer':
                player[key] = {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}
            elif value == 'mage':
                player[key] = {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}

    return player


def create_board(board_file, player_1, player_2):

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
        positions[(board[index + 1], board[index + 2])] = [board[index], board[index + 3], board[index + 4],
                                                           board[index + 5], board[index + 6]]
        creatures += [board[index]]

    del board
    
    return ROWS, COLUMNS, NB_TURNS, positions, creatures


def get_content(row, column, positions):

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


# Baz:barbarian Lee:healer May:mage Rob:rogue
# Buf:barbarian Lia:rogue Mey:mage Tob:rogue
# Baz:@21-3 Lee:@20-4 May:@10-10 Rob:@21-3
# Buf:@20-36 Lia:@21-37 Mey:@20-38 Tob:@21-36
# Baz:@21-4 Lee:@19-4 May:@21-3 Rob:*21-36
# Buf:@21-36 Lia:*21-37 Mey:@20-38 Tob:*21-3

# Bernard:barbarian Heidi:healer Marguerite:mage Robert:rogue
# Billy:barbarian Hans:healer Maya:mage Ruben:rogue
# Bernard:@21-3 Heidi:@20-4 Marguerite:@10-10 Robert:@21-3
# Billy:@20-36 Hans:@21-37 Maya:@20-38 Ruben:@21-36
# Bernard:@21-4 Heidi:@19-4 Marguerite:@21-3 Robert:*21-36
# Billy:@21-36 Hans:*21-37 Maya:@20-38 Ruben:*21-3
launch("board2")
