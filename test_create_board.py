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

    b_file.close()

    positions = {}
    creatures = {}

    nb_rows = board[1]
    nb_columns = board[2]
    nb_turns_wanted = board[3]

    positions[(board[5], board[6])] = 'spawn_player_1'
    positions[(board[7], board[8])] = 'spawn_player_2'

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

    # del board

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

    return nb_rows, nb_columns, nb_turns_wanted, positions, creatures