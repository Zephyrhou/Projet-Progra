
#Function 0
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



#Function 1
def launch(board_file):
    """Starts the game.

    Parameter:
    ----------
    board_file: Path of the file used to create the board (str)

    Version:
    --------
    specification: Zephyr Houyoux (v.2 04/03/19)
    implementation:
    """

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
    implementation:
    """

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

    Version:
    --------
    specification : Zephyr Houyoux (v.4 04/03/19)
    implementation:
    """ 

#Function 4
def create_heroes(player_input, dico_positions):
    """Takes the player's input, splits the information and stores it into a dictionary.

    Parameters:
    -----------
    player_input: Name of the different heroes and the classes the player chooses (str)
    positions: Contains all the coordinates of the board (dict)
    
    Returns: 
    --------
    positions: Contains all the coordinates of the board and the heroes(dict)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)

    Notes: 
    ------
    The names of the different heroes must all be unique and can't contain special characters.

    Version:
    --------
    specification: Zephyr Houyoux (v.2 04/03/19)
    implementation:
    """

#Function 5
def display_board(dico_positions):
    """Displays the board.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    
    Version:
    --------
    specification: Manon Michaux (v.2 25/02/19)
    implementation:
    """

#Function 6
def is_game_over(nb_turns_wanted, nb_turns1, nb_turns2, inactivity):
    """Checks whether the game is over or not.

    Parameters:
    -----------
    nb_turns_wanted: Number of turns the heroes need to be on spur to win (int)
    nb_turns1: Number of turns a hero of player1 stands on the spur (int)
    nb_turns2: Number of turns a hero of player2 stands on the spur (int)
    inactivity: Number of turns no activity has been observed (int)

    Returns:
    -------
    game_over: Is the game over or not (bool)

    Notes:
    ------
    A hero must stay for a given number of consecutive turns on the spur in order to win, this number is in board_file.

    Version:
    --------
    specification: Aude Lekeux (v.4 04/03/2019)
    implementation:
    """
    if nb_turns_wanted == nb_turns1 or nb_turns2:
        return True
    elif inactivity == 40:
        return True
    else:
        return False
    
#Function 7
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
#Function 8 
def gap_calculator(positions, name_character1, name_character2):
    """ Compute the gap between two things.
    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    name_character1: name of the first character ( can be an hero or a creature) (str)
    name_character2: name of the second character ( can be an hero or a creature) (str)

    Return:
    -------
    gap : gap between two things (int)
    
    Version:
    --------
    specification : Manon Michaux (v.2 18/03/19)
    implementaion : Manon Michaux (v.2 18/03/19)
    """
    position_1 = positions[name_character1]
    position_2 = positions[name_character2]
    pos1r = int(position_1[0])
    pos1c = int(position_1[1])
    pos2r = int(position_2[0])
    pos2c = int(position_2[1])
    gap = (((pos2r-pos1r)**2) + (pos2c-pos1c)**2)**0.5
    return gap

#Function 9
def inactivity(dico_positions, dico_inactivity, incativity_time):    """Count the inactivity of the players.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board and the heroes(dict)
    dict_inactivity: Coutains all the coordinates of the board and the heroes of the previous turn(dict)

    Returns:
    --------
    dict_inactivity: Coutains all the coordinates of the board and the heroes of the previous turn(dict)
    inactivity_time: Number of inactivity turn(int)


    Versions:
    ---------
    specification: Zephyr Houyoux(17/03/19)
    implementation: Zephyr Houyoux(17/03/19)
    """
    if dico_positions == dico_inactivity:
        inactivity_time =+ 1
    dico_inactivity = dico_positions
    return dico_inactivity, inactivity_time

#Function 10
def creature_turn(dico_positions, dico_creatures, dico_player1, dico_player2):
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

#Function 11
def defeated(dico_player, dico_creature):
    """Whenever a hero or a creature is defeated.

    Parameters:
    -----------
    dico_player: Information on the player's defeated hero who will respawn (dict)
    dico_creature: Information on the creature that dies (dict)

    Returns:
    --------
    dico_player: Information on the player's defeated hero who will respawn (dict)
    dico_position: Contains all the coordinates of the board (dict)

    Notes:
    ------
    A hero or a creature is defeated whenever their health points are at O or less.
    When a hero is defeated he respawns.
    When a creature is defeated it dies and it's victory points are distributed to the heroes around.

    Version:
    --------
    specification: Aude Lekeux (v.5 04/03/2019)
    implementation:
    """

#Function 12
def players_choice(choice, dico_positions):
    """Translates the player's order into actions.

    Parameters:
    -----------
    choice: Order of the player (str)
    dico_positions: Contains all the coordinates of the board (dict)
    Returns:
    --------
    dico_positions: Contains all the coordinates of the board (dict)
    Notes:
    ------
    The order of the player must be with the expected format = "hero_name : @r-c(movement) or *r-c(attack) "

    Version:
    --------
    specification: Manon Michaux (v.3 04/03/19)
    implementation:
    """

#Function 13
def attack(name_attack, dico_positions, dico_player, dico_creatures):
    """Checks whether the hero can do the attack, if yes, does it, if no, the attack is ignored.

    Parameters:
    -----------
    name_attack: Name of the attack (str)
    dico_positions: Contains all the coordinates of the board (dict)    dico_player: All the data about heroes (dict)
    dico_creatures: All the data about creatures (dict)

    Returns:
    --------
    dico_player: All the data about heroes (dict)
    creatures: All the data about creatures (dict)

    Version:
    --------
    specification: Zephyr Houyoux (v.3 04/03/19)
    implementation: 
    """

#Function 14
def move(dico_positions, movement):
    """Checks if the position he will end on is allowed.

    Parameters:
    -----------
    dico_positions: Contains all the coordinates of the board (dict)    movement: Coordinates the hero will go (str)

    Returns:
    --------
    dico_positions: Contains the updated coordinates of the board (dict)

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

#Function 15
def level(dico_player):
    """Checks if a hero can level up and upgrade their characteristics.    Parameters:
    -----------
    dico_player: All the data about the heroes (dict)

    Returns:
    --------
    dico_player: Updated data about the heroes (dict)

    Version:
    --------
    specification: Manon Michaux (v.3 04/03/19)
    implementation: 
    """

#Function 16
def summarize(dico_player, dico_creatures, nb_turns):
    """Summarize the state of the game.

    Parameters:
    -----------
    dico_player: All the data about the heroes (dict) 
    dico_creatures: All the data about creatures (dict)
    nb_turns: Number of turns of the game (int)

    Version:
    --------
    specification: Manon Michaux (v.2 25/02/19)
    implementation:
    """
#Function 17
def good_dict(hero_name):
    """Check in which dictionary the hero is.

    Parameter:
    ----------
    hero_name: name of the hero (str)

    Returns:
    --------
    good_dict: dictionary of the player which contains the hero (dict)
    bad_dict: dictionary of the player which doesn't contain the hero (dict)

    Version:
    --------
    specification: Manon Michaux (v.3 24/03/19)
    implementation: Manon Michaux (v.3 24/03/19)

    """
    for heroes_names in dict_player1 :
        if heroes_names == hero_name:
            good_dict == dict_player1
        else:
            for heroes in dict_player2:
                if heroes == hero_name:
                    good_dict = dict_player2
                    bad_dict = dict_player1
                else:
                    print("That hero doesn't exist")
    return good_dict, bad_dict
                


