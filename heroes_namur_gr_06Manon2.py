
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
    implementation
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
def attack(name_attack, positions, player1, player2, creatures):
    """Checks whether the hero can do the attack, if yes, does it, if no, the attack is ignored.

    Parameters:
    -----------
    name_attack: Name of the attack (str)
    positions: Contains all the coordinates of the board (dict)    dico_player: All the data about heroes (dict)
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
def level(player):
    """Checks if a hero can level up and upgrade their characteristics.    Parameters:
    -----------
    player: All the data about the heroes (dict)

    Returns:
    --------
    dico_player: Updated data about the heroes (dict)

    Version:
    --------
    specification: Manon Michaux (v.3 04/03/19)
    implementation: 
    """

#Function 16
def summarize(player&, player2, modifs, creatures, nb_turns):
    """Summarize the state of the game.

    Parameters:
    -----------
    player1: All the data about the heroes of the first player(dict)
    player2: All the data about the heroes of the second player (dict)
    creatures: All the data about creatures (dict)
    nb_turns: Number of turns of the game (int)

    Version:
    --------
    specification: Manon Michaux (v.2 25/02/19)
    implementation:
    """
#Function 17
def is_on_spur(positions, player1, player2):
    """Checks which heroes are on spur at the end of a turn.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    player1: All the data about the heroes of the first player(dict)
    player2: All the data about the heroes of the second player (dict)

    Return:
    -------
    on_spur: List of the heroes on the spur (list)

    Version:
    --------
    specification: Manon Michaux (v.1 01/04/19)
    implementation: Manon Michaux (v.1 01/04/19)
    """
    on_spur = []
    for heroes in player1:
        for places in positions[spur]:
            if positions[heroes] == places:
                on_spur += heroes
    for heroes in player2:
        for places in positions[spur]:
            if positions[heroes] == places:
                on_spur += heroes

    return on_spur
    

    

    
#Function 18
def good(hero_name):
    """Check in which dictionary the hero is.

    Parameter:
    ----------
    hero_name: name of the hero (str)

    Returns:
    --------
    good: dictionary of the player which contains the hero (dict)
    bad: dictionary of the player which doesn't contain the hero (dict)
    Version:
    --------
    specification: Manon Michaux (v.4 03/04/19)
    implementation: Manon Michaux (v.5 03/04/19)

    """
    for heroes_names in dict_player1 :
        if heroes_names == hero_name:
            good = dict_player1
            bad = dict_player2
        else:
            for heroes in dict_player2:
                if heroes == hero_name:
                    good = dict_player2
                    bad = dict_player1
                else:
                    print("That hero doesn't exist")
    return good, bad
                
#Function 19 ( all the attacks)
#All the functions for the different attacks
#n°1 : Barbarian

def energise(positions, hero_name, player, modif):
    """Raise the damage points of the allies in the hero's influence wage.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    player: Level, number of point, etc. of the heroes of the player (dict)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)

    Returns:
    --------
    updated: Updated dictionary of the player which hero's using this attack.
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)

    Version:
    --------
    specification: Manon Michaux (v.4 27/03/19)
    implementation: Manon Michaux Aude Lekeux(v.3 03/04/19)
    """

    updated, bad = good(hero_name)
    used = 0

    # Level of the hero from 1 to 5
    for level in range(1, 6):
        # Level from 2 to 5
        if level > 1:
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

    return updated, modif


#Sub Function of energise
def energise_level(level, updated, used, positions, hero_name):
    """When a hero wants to use energise.

    Parameters:
    -----------
    level: Level of the hero using the attack (int)
    updated: Dictionary of the player which hero's using tha attack (dict)
    used: Number of times the attack has been successfully used (int)
    positions: Dictionary containing all the coordinates of each character (dict)
    hero_name: Name of the hero using the attack (str)

    Returns:
    --------
    used: Number of times the attack has been successfully used (int)
    updated: Dictionary of the player which hero's using tha attack (dict)

    Version:
    --------
    specification: Manon Michaux (v.1 03/04/19)
    implementation Aude Lekeux Manon Michaux (v.2 03/04/19)
    """
    #Level = 2
    if level == 2:
        for heroes in updated:
            if gap_calculator(positions, hero_name, heroes) == 1:
                updated[heroes]['d_points'] += 1
                modif[heroes]['d_points_modifs'] += 1
                used += 1
                print(heroes + "'s damage points have been increased by 1 for this turn")
            else:
                print(heroes + "' damage points haven't been modified")    #Level = 5
    elif level == 5:
        for heroes in updated:
            if gap_calculator(postions, hero_name, heroes) <= level - 1:
                updated[heroes]['damage_points'] += level - 3
                modif[heroes]['damage_points_modifs'] += level - 3
                used += 1
                print(heroes + "'s damage points have been increased by 2 for this turn")
            else:
                print(heroes + "%s ' damage points haven't been modified")
                
    else:
        for heroes in updated:
            if gap_calculator(positions, hero_name, heroes) <= level - 1:
                updated[heroes]['damage_points'] += level - 2
                modif[heroes]['damage_points_modifs'] += level - 2
                used += 1
                #Level = 3
                if level == 3:
                    print(heroes + "'s damage points have been increased by 1 for this turn")
                #Level = 4
                else:
                    print(heroes + "'s damage points have been increased by 1 for this turn")
            else:
                print(heroes + "%s ' damage points haven't been modified")

    return used, updated


def stun(positions, player_1, player_2, creatures, hero_name, modif):
    """ Stun the ennemies ( both heroes and creatures) in the hero's wage.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)
    creatures: All the data about creatures (dict)
    hero_name: Name of the hero (str)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature (dict)

    Returns:
    --------
    updated_dict: Dictionary of the ennemy (dict)
    creatures: updated Dictionary of the creatures (dict)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature (dict)
    good_dict: Dictionary of the player which hero's using tha attack (dict)
    
    Version:
    --------
    specification: Manon Michaux (v.4 27/03/19)
    implementation: Manon Michaux (v.2 26/03/19)

    """

    good_dict, updated_dict = good_dict(hero_name)

    #Level of the hero = 3
    if good_dict[hero_name][level] == 3:
        #For the heroes of the other player
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, heroes) == 1:
                if updated_dict[heroes][d_points] >= 2:
                    updated_dict[heroes][d_points] -= 1
                    modif[heroes][d_points_modif] -= 1
                    used += 1
                    print(" %s 's damage points have been decreased by 1 for this turn"%heroes)
                else:
                    print("%s 's damage points haven't been modified "%heroes)

            else:
                print("%s 's damage points haven't been modified "%heroes)

        #For the creatures
        for ennemies in creatures:
            if gap_calculator(positions,hero_name, ennemies) == 1:
                if creatures[ennemies][d_points] >= 2:
                    creatures[ennemies][d_points] -= 1
                    modif[ennemies][d_points_modif] -= 1
                    used += 1
                    print(" %s 's damage points have been decreased by 1 for this turn"%ennemies)
                else:
                    print("%s 's damage points haven't been modified "%ennemies)

            else:
                print("%s 's damage points haven't been modified "%ennemies)

    #Level of the hero = 4
    elif good_dict[hero_name][level] == 4:
        #For the heroes of the other player
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, heroes) <= 2:
                if updated_dict[heroes][d_points] >= 3:
                    updated_dict[heroes][d_points] -= 2
                    modif[heroes][d_points_modif] -= 2
                    used += 1
                    print(" %s 's damage points have been decreased by 2 for this turn"%heroes)
                else:
                    print("%s 's damage points haven't been modified "%heroes)
            else:
                print("%s 's damage points haven't been modified "%heroes)

        #For creatures
        for ennemies in creatures:
            if gap_calculator(positions,hero_name, ennemies) <= 2:
                if creatures[ennemies][d_points] >= 3:
                    creatures[ennemies][d_points] -= 2
                    modif[ennemies][d_points_modif] -= 2
                    used += 1
                    print(" %s 's damage points have been decreased by 2 for this turn"%ennemies)
                else:
                    print("%s 's damage points haven't been modified "%ennemies)
            else:
                print("%s 's damage points haven't been modified "%ennemies)

    #Level of the hero = 5
    elif good_dict[hero_name][level] == 5:
        #For the heroes of the other player
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, heroes) <= 3:
                if updated_dict[heroes][d_points] >= 4:
                    updated_dict[heroes][d_points] -= 3
                    modif[heroes][d_points_modif] -= 3
                    used += 1
                    print(" %s 's damage points have been decreased by 3 for this turn"%heroes)
                else:
                    print("%s 's damage points haven't been modified "%heroes)
            else:
                print("%s 's damage points haven't been modified "%heroes)

        #For creatures
        for ennemies in creatures:
            if gap_calculator(positions,hero_name, ennemies) <= 3:
                if creatures[ennemies][d_points] >= 4:
                    creatures[ennemies][d_points] -= 3
                    modif[ennemies][d_points_modif] -= 3
                    used += 1
                    print(" %s 's damage points have been decreased by 3 for this turn"%ennemies)
                else:
                    print("%s 's damage points haven't been modified "%ennemies)
            else:
                print("%s 's damage points haven't been modified "%ennemies)

    #Level of the hero = 1 or = 2
    else:
        print(" You can't use this attack yet")

    #Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        good_dict[hero_name][cooldown][stun] += 1
    else:
        print("You used stun but nothing happened ")

    return updated_dict, creatures, modif, good_dict
      

#Sub Function of stun
def stun_level(kind, level, updated, hero_name, positions, used, creatures):
    """When a hero want's to use stun.

    Parameters:
    -----------
    kind: Either 'hero' or 'creature' (str)
    level: Level of the hero using the attack (int)
    updated: Dictionary of the player which hero's using tha attack (dict)
    hero_name: Name of the hero using the attack (str)
    positions: Dictionary containing all the coordinates of each character (dict) 
    used: number of times the attack has been successfully used (int)
    creatures: dictionary containing all the data about the creatures (dict)

    Returns:
    --------
    used: number of times the attack has been successfully used (int)
    positions: Dictionary containing all the coordinates of each character (dict) 

    Version:
    --------
    specification: Aude Lekeux (v.1 03/04/19)
    implementation: Aude Lekeux (v.1 03/04/19)
    """
    decrease = 0
    if kind == 'hero':
        for heroes in updated:
            if gap_calculator(positions, hero_name, heroes) == level - 2:
                if updated[heroes]['d_points'] >= level - 1:
                    updated[heroes]['d_points'] -= level - 2
                    modif[heroes]['d_points_modifs'] -= level - 2                    decrease = modif[enemies]['d_points_modifs']
                    used += 1
                    print(heroes + "'s damage points have been decreased by %i for this turn"%decrease)
                else:
                    print(heroes + "'s damage points haven't been modified")

            else:
                print(heroes + "'s damage points haven't been modified")

    elif kind == 'creature':
        for enemies in creatures:
            if gap_calculator(positions, hero_name, enemies) == level - 2:
                if creatures[enemies]['d_points'] >= level - 1:
                    creatures[enemies]['d_points'] -= level - 2
                    modif[enemies]['d_points_modifs'] -= level - 2
                    decrease = modif[enemies]['d_points_modifs']
                    used += 1
                    print(enemies + "'s damage points have been decreased by %i for this turn"%decrease)
                else:
                    print(enemies + "'s damage points haven't been modified")

            else:
                print(enemies + "'s damage points haven't been modified")

    return used, positions



                
#n°2 : Healer

def invigorate(positions, hero_name, player, modif):
    """Raise the health points of the allies in the hero's wage.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)
    max_health_dict: Dictionary containing for each class and for each level their own maximum of health points (dict)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)

    Returns:
    --------
    updated: Updated dictionary of the player which hero's using this attack.
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)

    Version:
    --------
    specification: Manon Michaux (v.2 27/03/19)
    implementation: Manon Michaux Aude Lekeux(v.3 03/04/19)
    """

    updated, bad = good(hero_name)
    used = 0

    # Level of the hero from 2 to 5
    for level_hero in range(2, 6):
        if updated[hero_name]['level'] == level_hero:
            for heroes in updated:
                if gap_calculator(positions, hero_name, heroes) <= level_hero - 1:

                    for job in dict_job:
                        if updated[heroes]['job'] == job:
                            # Level of the ally from 1 to 5
                            for level_ally in range(1, 6):
                                updated, used = invigorate_level(heroes, job, level_hero, level_ally, updated, used)
                        else:
                            print(" Class isn't correct")

    # Level of the hero = 1
    else:
        print(" You can't use this attack yet")

    # Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        good(hero_name)['cooldown']['invigorate'] += 1
    else:
        print("You used invigoate but nothing happened")

    return updated, modif

#Sub function to use in invigorate
def invigorate_level(hero, job, level_hero, level_ally, updated, used, max_health_points):
    """ Sub function of invogorate following the level of the hero and the ally.
    Parameters:
    -----------
    hero: Name of the hero using the attack (str)
    job: job of the ally in the hero's wage (str)
    level_hero: Level of the hero (int)
    level_ally: Level of the ally (int)
    updated: Dictionary of the player which hero's using the attack (dict)
    used: number of time invigorate has been successfully used (int)
    max_health_points: Dictionary which for each job and for each level contains the maximum number of health points (dict)
    
    Returns:
    --------
    updated: Dictionary of the player which hero's using the attack (dict)
    used: number of time invigorate has been successfully used (int)

    Version:
    --------
    specification: Manon Michaux (v.1 03/04/19)
    implementation: Manon Michaux Aude Lekeux (v.1 03/04/19)
    """
    if level_hero == 2:
        if updated[hero]['level'] == level_ally:
            if updated[hero]['h_points'] < max_health_points[job][level]:
                updated[hero]['h_points'] += 1
                modif[hero]['h_points_modif'] += 1
                used += 1
                print(hero + "' health points have been increased by one")
            else:
                print(hero + "' health points haven't been modified")

    elif level_hero == 3:
        if updated[hero]['level'] == level_ally:
            max_health = max_health_points[job][level_ally] - 2
            if updated[hero]['h_points'] <= max_health:
                updated[hero]['h_points'] += 2
                modif[hero]['h_points_modif'] += 2
                used += 1
                print(hero + "' health points have been increased by two ")
            else:
                print(hero + "' health points haven't been modified")

    elif level_hero == 4:
        if updated[hero]['level'] == level_ally:
            max_health = max_health_points[job][level_ally] - 3
            if updated[hero]['h_points'] <= max_health:
                updated[hero]['h_points'] += 3
                modif[hero]['h_points_modif'] += 3
                used += 1
                print(hero + "' health points have been increased by three")
            else:
                print(hero + "' health points haven't been modified")

    elif level_hero == 5:
        if updated[hero]['level'] == level_ally:
            max_health = max_health_points[job][level_ally] - 4
            if updated[hero]['h_points'] <= max_health:
                updated[hero]['h_points'] += 4
                modif[hero]['h_points_modif'] += 4
                used += 1
                print(hero + "' health points have been increased by four")
            else:
                print(hero + "' health points haven't been modified")

    return updated, used

def immunise(positions, hero_name, player1, player2, modif, coordinates):
    """ Immunised the ally on the target coordinates.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature (dict)
    coordinates: Where the hero wants to use immunise(tupl)
    
    Returns:
    --------
    updated_dict: Updated dictionary of the player which hero's using this attack.
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)
 
    Version:
    --------
    specification: Manon Michaux (v.4 27/03/19)
    implementation: Manon Michaux (v.4 31/03/19)

    """
    updated_dict, bad_dict = good_dict(hero_name)

    #Level of the hero = 3
    if updated_dict[hero_name][level] == 3:
        #For the heroes of the player
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, coordinates) == 1:
                if gap_calculator(positions,coordinates, heroes) == 0:
                    modif[heroes][immunise] += 1
                    used += 1
                    print("%s has been immunized for this turn" %heroes)
                    
                else:
                    print("Those coordinates don't belong to %s"%heroes)
                print("The coordinates you tried to reach are too far away right now")

    #Level of the hero = 4
    elif updated_dict[hero_name][level] == 4:
        #For the heroes of the player
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, coordinates) <= 2:
                if gap_calculator(positions,coordinates, heroes) == 0:
                    modif[heroes][immunise] += 1
                    used += 1
                    print("%s has been immunized for this turn" %heroes)
                    
                else:
                    print("Those coordinates don't belong to %s"%heroes)
                print("The coordinates you tried to reach are too far away right now")
                

    #Level of the hero = 5
    elif updated_dict[hero_name][level] == 5:
        #For the heroes of the player
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, coordinates) <= 3:
                if gap_calculator(positions,coordinates, heroes) == 0:
                    modif[heroes][immunise] += 1
                    used += 1
                    print("%s has been immunized for this turn" %heroes)
                    
                else:
                    print("Those coordinates don't belong to %s"%heroes)
                print("The coordinates you tried to reach are too far away right now")


    #Level of the hero = 1 or = 2
    else:
        print("You can't use this attack yet")

    #Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        good_dict[hero_name][cooldown][immunise] += 3
    else:
        print("You used stun but nothing happened ")

    return updated_dict, modif

#n°3 : Mage

def fulgura(coordinates, player_1, player_2, creatures, hero_name, modif, positions):
    """ The creature / ennemy on the target coordinates loses a given number of health points.

    Parameters:
    -----------
    coordinates: Where the hero wants to use ovibus(tupl)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)
    creatures: All the data about creatures (dict)
    hero_name: Name of the hero (str)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature (dict)
    positions: Contains all the coordinates of the board (dict)


    Returns:
    --------
    updated_dict: Dictionary of the ennemy (dict)
    creatures: updated Dictionary of the creatures (dict)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature (dict)
    good_dict: Dictionary of the player which hero's using tha attack (dict)
    
    Version:
    --------
    specification: Manon Michaux (v.2 31/03/19)
    implementation: Manon Michaux (v.2 31/03/19)

    """

    good_dict, updated_dict = good_dict(hero_name)

    #Level of the hero = 2
    if good_dict[hero_name][level] == 2:
        if gap_calculator(positions,hero_name, coordinates) == 1:
            #For the heroes of the other player
            for heroes in updated_dict:
                if gap_calculator(positions,coordinates, heroes) == 0:
                    updated_dict[heroes][h_points] -= 3
                    used += 1
                    print(" %s 's health points have been decreased by 3 "%heroes)
                else:
                    print("%s 's damage points haven't been modified "%heroes)
            #For the creatures
            for ennemies in creatures:
                if gap_calculator(positions,hero_name, ennemies) == 0:
                    creatures[ennemies][h_points] -= 3
                    used += 1
                    print(" %s 's health points have been decreased by 3"%ennemies)
                else:
                    print("%s 's damage points haven't been modified "%ennemies)

            else:
                print("%s 's damage points haven't been modified "%ennemies)

    #Level of the hero = 3
    elif good_dict[hero_name][level] == 3:
        if gap_calculator(positions,hero_name, coordinates) <= 2:            #For the heroes of the other player
            for heroes in updated_dict:
                if gap_calculator(positions,coordinates, heroes) == 0:
                    updated_dict[heroes][h_points] -= 3
                    used += 1
                    print(" %s 's health points have been decreased by 3 "%heroes)
                else:
                    print("%s 's damage points haven't been modified "%heroes)
            #For the creatures
            for ennemies in creatures:
                if gap_calculator(positions,hero_name, ennemies) == 0:
                    creatures[ennemies][h_points] -= 3
                    used += 1
                    print(" %s 's health points have been decreased by 3"%ennemies)
                else:
                    print("%s 's damage points haven't been modified "%ennemies)

            else:
                print("%s 's damage points haven't been modified "%ennemies)


    #Level of the hero = 4
    elif good_dict[hero_name][level] == 4:
        if gap_calculator(positions,hero_name, coordinates) <= 3:            #For the heroes of the other player
            for heroes in updated_dict:
                if gap_calculator(positions,coordinates, heroes) == 0:
                    updated_dict[heroes][h_points] -= 4
                    used += 1
                    print(" %s 's health points have been decreased by 4 "%heroes)
                else:
                    print("%s 's damage points haven't been modified "%heroes)
            #For the creatures
            for ennemies in creatures:
                if gap_calculator(positions,hero_name, ennemies) == 0:
                    creatures[ennemies][h_points] -= 4
                    used += 1
                    print(" %s 's health points have been decreased by 4"%ennemies)
                else:
                    print("%s 's damage points haven't been modified "%ennemies)

            else:
                print("%s 's damage points haven't been modified "%ennemies)

    #Level of the hero = 5
    elif good_dict[hero_name][level] == 5:
        if gap_calculator(positions,hero_name, coordinates) <= 4:            #For the heroes of the other player
            for heroes in updated_dict:
                if gap_calculator(positions,coordinates, heroes) == 0:
                    updated_dict[heroes][h_points] -= 4
                    used += 1
                    print(" %s 's health points have been decreased by 4 "%heroes)
                else:
                    print("%s 's damage points haven't been modified "%heroes)
            #For the creatures
            for ennemies in creatures:
                if gap_calculator(positions,hero_name, ennemies) == 0:
                    creatures[ennemies][h_points] -= 4
                    used += 1
                    print(" %s 's health points have been decreased by 4"%ennemies)
                else:
                    print("%s 's damage points haven't been modified "%ennemies)

            else:
                print("%s 's damage points haven't been modified "%ennemies)


 
    #Level of the hero = 1 or = 2
    else:
        print(" You can't use this attack yet")

    #Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        good_dict[hero_name][cooldown][fulgura] += 1
    else:
        print("You used stun but nothing happened ")

    return updated_dict, creatures, modif, good_dict
      
        


def ovibus(positions, hero_name, coordinates, player1, player2, creatures, modif):
    """The creature/ennemy on the target coordinates is unable to act during a given number of turn.
    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    coordinates: Where the hero wants to use ovibus(tupl)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)
    creatures: All the data about creatures (dict)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)

    Returns:
    --------
    updated_dict: Updated dictionary of the player which hero isn't using this attack.
    good_dict:  Updated dictionary of the player which hero is using this attack.
    creatures: All the data about creatures (dict)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)

    Version:
    --------
    specification: Manon Michaux (v.1 29/03/19)
    implementation: Manon Michaux (v.1 29/03/19)

    """
   good_dict, updated_dict= good_dict(hero_name)

    #Level of the hero = 3
    if good_dict[hero_name][level] == 3:
        if gap_calculator(positions,hero_name, coordinates) == 1:
            #For the heroes of the player
            for heroes in updated_dict:
                if gap_calculator(positions,coordinates, heroes) == 0:
                    modif[heroes][confused] += 1
                    used += 1
                    print("%s is confused for one turn" %heroes)
                    
                else:
                    print("Those coordinates don't belong to %s"%heroes)
                    
            #For the creatures
            for ennemy in creatures:
                if gap_calculator(positions,coordinates, ennemy) == 0:
                    modif[ennemy][confused] += 1
                    used += 1
                    print("%s is confused for one turn" %heroes)
                else:
                    print("Those coordinates don't belong to %s"%heroes)

                
            print("The coordinates you tried to reach are too far away right now")

    #Level of the hero = 4
    elif good_dict[hero_name][level] == 4:
        if gap_calculator(positions,hero_name, coordinates) <= 2:            #For the heroes of the player
            for heroes in updated_dict:
                if gap_calculator(positions,coordinates, heroes) == 0:
                    modif[heroes][confused] += 2
                    used += 1
                    print("%s is confused for one turn" %heroes)
                    
                else:
                    print("Those coordinates don't belong to %s"%heroes)
                    
            #For the creatures
            for ennemy in creatures:
                if gap_calculator(positions,coordinates, ennemy) == 0:
                    modif[ennemy][confused] += 2
                    used += 1
                    print("%s is confused for one turn" %heroes)
                else:
                    print("Those coordinates don't belong to %s"%heroes)

                
            print("The coordinates you tried to reach are too far away right now")
                

    #Level of the hero = 5
    elif good_dict[hero_name][level] == 5:
        if gap_calculator(positions,hero_name, coordinates) <= 3:            #For the heroes of the player
            for heroes in updated_dict:
                if gap_calculator(positions,coordinates, heroes) == 0:
                    modif[heroes][confused] += 3
                    used += 1
                    print("%s is confused for one turn" %heroes)
                    
                else:
                    print("Those coordinates don't belong to %s"%heroes)
                    
            #For the creatures
            for ennemy in creatures:
                if gap_calculator(positions,coordinates, ennemy) == 0:
                    modif[ennemy][confused] += 3
                    used += 1
                    print("%s is confused for one turn" %heroes)
                else:
                    print("Those coordinates don't belong to %s"%heroes)

                
            print("The coordinates you tried to reach are too far away right now")


    #Level of the hero = 1 or = 2
    else:
        print("You can't use this attack yet")

    #Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        good_dict[hero_name][cooldown][ovibus] += 3
    else:
        print("You used stun but nothing happened ")

    return updated_dict, good_dict, creatures, modif


#n°4 : Rogue

def reach(positions, hero_name, coordinates, player1, player2, creatures, modif):
    """Teleports the hero using the attack if he is the first using reach this turn and if the target coordinates aren't occupied.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    coordinates: Where the hero wants to use ovibus(tupl)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)
    creatures: All the data about creatures (dict)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board (dict)
    updated_dict: Updated dictionary of the player which hero is using this attack.
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)

    Version:
    --------
    specification: Manon Michaux (v.2 03/04/19)
    implementation: Manon Michaux (v.2 03/04/19)

    """
   updated_dict, bad_dict= good_dict(hero_name)
   character_list = []

    #Level of the hero = 2
    if updated_dict[hero_name][level] == 2:
        if gap_calculator(positions,hero_name, coordinates) == 1:
            #For the all the characters in positions
            for characters in positions:
                if gap_calculator(positions,coordinates, characters) == 0:
                    print("%s is already on those coordinates right now" %characters)
                    
                else:
                    unoccupied += 1
                character_list += characters
        else:
            print("The coordinates you tried to reach are too far away right now")

        #if none of the characters are on the target coordinates
        if unoccupied == len(character_list):
            positions[hero_name] = coordinates
            used += 1

    #Level of the hero = 3
    if updated_dict[hero_name][level] == 3:
        if gap_calculator(positions,hero_name, coordinates) <= 2:            #For the all the characters in positions
            for characters in positions:
                if gap_calculator(positions,coordinates, characters) == 0:
                    print("%s is already on those coordinates right now" %characters)
                    
                else:
                    unoccupied += 1
                character_list += characters
        else:
            print("The coordinates you tried to reach are too far away right now")

        #if none of the characters are on the target coordinates
        if unoccupied == len(character_list):
            positions[hero_name] = coordinates
            used += 1

    #Level of the hero = 4
    if updated_dict[hero_name][level] == 4:
        if gap_calculator(positions,hero_name, coordinates) <= 3:            #For the all the characters in positions
            for characters in positions:
                if gap_calculator(positions,coordinates, characters) == 0:
                    print("%s is already on those coordinates right now" %characters)
                    
                else:
                    unoccupied += 1
                character_list += characters
        else:
            print("The coordinates you tried to reach are too far away right now")

        #if none of the characters are on the target coordinates
        if unoccupied == len(character_list):
            positions[hero_name] = coordinates
            used += 1

    #Level of the hero = 5
    if updated_dict[hero_name][level] == 5:
        if gap_calculator(positions,hero_name, coordinates) <= 4:            #For the all the characters in positions
            for characters in positions:
                if gap_calculator(positions,coordinates, characters) == 0:
                    print("%s is already on those coordinates right now" %characters)
                    
                else:
                    unoccupied += 1
                character_list += characters
        else:
            print("The coordinates you tried to reach are too far away right now")

        #if none of the characters are on the target coordinates
        if unoccupied == len(character_list):
            positions[hero_name] = coordinates
            used += 1
                  

    #Level of the hero = 1 or = 2
    else:
        print("You can't use this attack yet")

    #Adding the cooldown to the dictionary of the player if he attack has been used
    if used == 1:
        good_dict[hero_name][cooldown][ovibus] += 1
    else:
        print("You used stun but nothing happened ")

    return updated_dict, positions, modif

   
   
   
def burst(positions, hero_name,player1, player2, creatures, modif):
    """The creatures/ennemies in the hero's wage lose a given number of health points.
    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)
    creatures: All the data about creatures (dict)    
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)

    Returns:
    --------
    updated_dict: Updated dictionary of the player which hero's using this attack.
    good_dict:  Updated dictionary of the player which hero is using this attack.
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)
    creatures: All the data about creatures (dict)
    
    Version:
    --------
    specification: Manon Michaux (v.2 03/04/19)
    implementation: Manon Michaux (v.1 03/04/19)

    """
    good_dict, updated_dict = good_dict(hero_name)
    
    #Level of the hero = 3
    if good_dict[hero_name][level] == 3:
        #For heroes of the other player
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, heroes) == 1:
                updated_dict[heroes][h_points]-=1
                used += 1
                print("%s 's health points have been decreased by 1 "%heroes)
            else:
                print("%s ' health points haven't been modified"%heroes)
        #For the creatures
        for ennemies in creatures:
            if gap_calculator(positions,hero_name, enemies) == 1:
                updated_dict[ennemies][h_points]-=1
                used += 1
                print("%s 's health points have been decreased by 1 "%ennemies)
            else:
                print("%s ' health points haven't been modified"%ennemies)

    #Level of the hero = 4
    elif good_dict[hero_name][level] == 4:
        #For heroes of the other player
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, heroes) <= 2:
                updated_dict[heroes][h_points]-= 2
                used += 1
                print("%s 's health points have been decreased by 2 "%heroes)
            else:
                print("%s ' health points haven't been modified"%heroes)

        #For the creatures
        for ennemies in creatures:
            if gap_calculator(positions,hero_name, enemies) <= 2:                updated_dict[ennemies][h_points]-= 2
                used += 1
                print("%s 's health points have been decreased by 2 "%ennemies)
            else:
                print("%s ' health points haven't been modified"%ennemies)


    #Level of the hero = 5
    elif good_dict[hero_name][level] == 5:
        #For heroes of the other player
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, heroes) <= 3:
                updated_dict[heroes][h_points]-= 3
                used += 1
                print("%s 's health points have been decreased by 3 "%heroes)
            else:
                print("%s ' health points haven't been modified"%heroes)

        #For the creatures
        for ennemies in creatures:
            if gap_calculator(positions,hero_name, enemies) <= 3:                updated_dict[ennemies][h_points]-= 3
                used += 1
                print("%s 's health points have been decreased by 3 "%ennemies)
            else:
                print("%s ' health points haven't been modified"%ennemies)


    #Level of the hero = 1 or = 2
    else:
        print(" You can't use this special attack yet")
    
    #Adding the cooldown to the dictionary of the player if the attack has been used
    if used >= 1:
        updated_dict[heroes][cooldown][burst] += 1
    else:
        print("You used burst but nothing happened")

    
    return updated_dict, good_dict, modif, creatures  




