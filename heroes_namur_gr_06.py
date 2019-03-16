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
    implementation: Manon Michaux (v.2 15/02/19)
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


#Function 4
def create_heroes(positions):
    """Takes the player's input, splits the information and stores it into a dictionary.

    Parameter:
    ----------
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
    specification: Zephyr Houyoux (v.3 09/03/19)
    implementation: Aude Lekeux (v.1 08/03/19)
    """

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

#Function 7
def game(positions, nb_turns_wanted, player1, player2):
    """Starts a new turn if the game is not finished.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    nb_turns_wanted: Number of turns the heroes need to be on spur to win (int)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)

    Returns:
    --------
    nb_turns1: Number of turns a hero of player1 stands on the spur (int)
    nb_turns2: Number of turns a hero of player2 stands on the spur (int)
    inactivity: Number of turns no activity has been observed (int)

    Version:
    --------
    specification: Zephyr Houyoux (v.4 15/03/19)
    implementation:
    """

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

#Function 9
def defeated(player, creature):
    """Whenever a hero or a creature is defeated.

    Parameters:
    -----------
    player: Information on the player's defeated hero who will respawn (dict)
    creature: Information on the creature that dies (dict)

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
    implementation: Aude Lekeux (v.2 15/03/19)
    """

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