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


def available_attack(name_attack, player1, player2, job):
    """ Checks whether an attack is accessible or not.

    Parameters:
    -----------
    name_attack: Name of the attack the hero wants to use (str)
    player1: Dictionary of the first player (dict)
    player2: Dictionary of the second player (dict)
    job: Dictionary of special attacks following their job (dict)

    Return:
    -------
    availability: whether the hero can use the attack or not (bool)

    Notes:
    ------
    availability is true if the hero can use the attack and false otherwise.

    Version:
    --------
    specification: Manon Michaux (v.1 24/04/19)
    implementation: Manon Michaux (v.1 24/04/19)

    """
    good, bad = good(hero_name)
    used = 0
    
    #correct class ?
    for vocations in job:
        if good[hero_name][job] == vocations:
            for actions in job[vocations]:
                if actions == name_attack:
                    used += 1
    #correct level ?
    if used == 1:
        if name_attack == job[vocations][0]:
            if good[hero_name][level] < 2:
                used -= 1
        else:
            if name_attack == job[vocations][1]:
                if good[hero_name][level] < 3:
                    used -= 1

    #Cooldown ok ?
    if used == 1:
        if good[hero_name][cooldown][name_attack] == 0:
            return True
        else:
            return False
    else:
        return False 
                
        
        
         





    
    









    
