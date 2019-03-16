import os


def boardfilecreation():
    """ create the file for the game.
    Version:
    --------
    specification : Manon Michaux (v.1 08/03/19 )
    implementation : Manon Michaux (v.1 08/03/19)
    """
    b_file = open('board_file','a')
    line = "map: \n 30 30 25 \n spawn: \n 25 6 \n 12 8 \n spur: \n 1 25 \n 1 26 \n 2 25 \n 2 26 \n"
    line += "creatures: \n lion 2 27 20 7 7 150 \n bear 2 28 17 9 4 200 \n"
    b_file.write(line)
    b_file.close()


#Function 3

def create_board(board_file):
    """Creates the map and displays it.

    Parameter:
    ----------
    board_file : Path of the file used to create the board (str)

    Returns:
    --------
    dico_positions: Contains all the coordinates of the board (dict)    nb_turns_wanted: Number of turns the heroes need to be on spur to win (int)

    Version:
    --------
    specification : Zephyr Houyoux (v.4 04/03/19)
    implementation: Manon Michaux (v.1 08/03/19)
    """
    board_file = str(board_file)
    os.getcwd()
    b_file = open(board_file,'r')
    informations = b_file.readlines()
    print(informations)
    
    
boardfilecreation()
create_board('board_file')
