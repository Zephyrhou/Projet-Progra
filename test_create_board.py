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


create_board("C:/Users/Aude/Desktop/board.txt")
    


