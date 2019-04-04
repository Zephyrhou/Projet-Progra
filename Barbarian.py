def energise_level(level, updated, used, positions, hero_name):
    """When a hero want's to use energise.
    
    Parameters:
    -----------
    level:
    updated:
    used:
    positions:
    hero_name:
    
    Returns:
    --------
    used:
    updated:
    
    Version:
    --------
    specification: Aude Lekeux (v.1 03/04/19)
    implementation Aude Lekeux (v.1 03/04/19)
    """
    
    if level == 2:
        for heroes in updated:
            if gap_calculator(positions, hero_name, heroes) == 1:
                updated[heroes]['damage_points'] += 1
                modif[heroes]['damage_points_modifs'] += 1
                used += 1
                print(heroes + "'s damage points have been increased by 1 for this turn")
            else:
                print(heroes + "' damage points haven't been modified")
                
    else:
        for heroes in updated:
            if gap_calculator(positions, hero_name, heroes) <= level - 1:
                updated[heroes]['damage_points'] += level - 2
                modif[heroes]['damage_points_modifs'] += level - 2
                used += 1
                print(heroes + "'s damage points have been increased by 1 for this turn")
            else:
                print(heroes + "%s ' damage points haven't been modified")
                
    return used, updated


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
    updated_dict: Updated dictionary of the player which hero's using this attack.
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)

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

    return updated, modif


def stun_level(type, level, updated, hero_name, positions, used, creatures):
    """When a hero want's to use stun.
    
    Parameters:
    -----------
    type:
    level:
    updated:
    hero_name:
    positions:
    used:
    creatures: 
    
    Returns:
    --------
    used:
    positions:
    
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
                    modif[heroes]['damage_points_modifs'] -= level - 2
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
                    modif[enemies]['damage_points_modifs'] -= level - 2
                    used += 1
                    print(enemies + "'s damage points have been decreased by 1 for this turn")
                else:
                    print(enemies + "'s damage points haven't been modified")
    
            else:
                print(enemies + "'s damage points haven't been modified")
                
    return used, positions
    

def stun(positions, player, creatures, hero_name, modif):
    """ Stun the ennemies ( both heroes and creatures) in the hero's wage.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    player: Level, number of point, etc. of the heroes of the player (dict)
    creatures: All the data about creatures (dict)
    hero_name: Name of the hero (str)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature (dict)

    Returns:
    --------
    updated_dict: Dictionary of the ennemy (dict)
    creatures: updated Dictionary of the creatures (dict)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature (dict)
    dict: Dictionary of the player which hero's using tha attack (dict)

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

    return updated, creatures, modif, good
