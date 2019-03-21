

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
    lecture = []
    lines = []
    lines += b_file.readlines()

    for line in lines:
        line = line.replace('\n', '')
        line = line.split(' ')
        lecture += line
    print(lecture)

    b_file.close()
    positions = {}
    creatures = {}
    nb_ranges = lecture[1]
    nb_columns = lecture[2]
    nb_turns_wanted = lecture[3]
    positions[spawn][player1] = (lecture[5], lecture[6])
    positions[spawn][player_2] = (lecture[7], lecture[8])
    #optimisation ? Boucle while pour spur & creatures ( nombre peut fluctuer en fonction du fichier)
    positions[spur] = [(lecture[10],lecture[11]),(lecture[12],lecture[13]),(lecture[14],lecture[15]),(lecture[16],lecture[17])]
    positions[lecture[19]]=(lecture[20],lecture[21])
    positions[lecture[26]]=(lecture[27],lecture[28])
    print(positions)
    creatures[lecture[19]][h_points]= lecture[22]
    creatures[lecture[19]][d_points]= lecture[23]
    creatures[lecture[19]][creature_wage]= lecture[24]
    creatures[lecture[19]][v_points]= lecture[25]
    creatures[lecture[26]][h_points]= lecture[29]
    creatures[lecture[26]][d_points]= lecture[30]
    creatures[lecture[26]][creature_wage]= lecture[31]
    creatures[lecture[26]][v_points]= lecture[32]
    print(creatures)
    return nb_ranges, nb_columns, nb_turns_wanted, positions, creatures

create_board("Users/Imperatrice/Desktop/board_file.hon.txt")
    


