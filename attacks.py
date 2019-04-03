#All the functions for the different attacks
#n°1 : Barbarian
def energise(positions, hero_name, player1, player2, modif):
    """Raise the damage points of the allies in the hero's influence wage.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    player1: Level, number of point, etc. of the heroes of player1 (dict)
    player2: Level, number of point, etc. of the heroes of player2 (dict)
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

    updated_dict, bad_dict = good_dict(hero_name)
    #Level of the hero = 2
    if updated_dict[hero_name]['level'] == 2:
        for heroes in updated_dict :
            if gap_calculator(positions,hero_name, heroes) == 1:
                updated_dict[heroes]['damage_points'] +=1
                modif[heroes]['damage_points_modifs'] += 1
                used += 1
                print("%s 's damage points have been increased by 1 for this turn"%heroes)
            else:
                print("%s ' damage points haven't been modified"%heroes)

    #Level of the hero = 3
     elif updated_dict[hero_name]['level'] == 3:
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, heroes) <= 2:
                updated_dict[heroes]['damage_points'] +=1
                modif[heroes]['damage_points_modifs'] += 1
                used += 1
                print("%s 's damage points have been increased by 1 for this turn"%heroes)
            else:
                print("%s ' damage points haven't been modified"%heroes)

    #Level of the hero = 4  
    elif updated_dict[hero_name]['level'] == 4:
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, heroes) <= 3:
                updated_dict[heroes]['damage_points']+= 2
                modif[heroes]['damage_points_modifs'] += 2
                used += 1
                print("%s 's damage points have been increased by 2 for this turn"%heroes)
            else:
                print("%s ' damage points haven't been modified"%heroes)
    
    #Level of the hero = 5    
    elif updated_dict[hero_name]['level'] == 5:
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, heroes) <= 4:
                updated_dict[heroes]['damage_points'] += 2
                modif[heroes]['damage_points_modifs'] += 2
                used += 1
                print("%s 's damage points have been increased by 2 for this turn"%heroes)
            else:
                print("%s ' damage points haven't been modified"%heroes)

    #Level of the hero = 1 
    else:
        print(" You can't use this special attack yet")
    
    #Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        updated_dict[heroes]['cooldown']['energise'] += 1
    else:
        print("You used energise but nothing happened")

    
    return updated_dict, modif        

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
    if updated_dict[hero_name]['level'] == 3:
        #For the heroes of the other player
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, heroes) == 1:
                if updated_dict[heroes]['damage_points'] >= 2:
                    updated_dict[heroes]['damage_points'] -= 1
                    modif[heroes]['damage_points_modifs'] -= 1
                    used += 1
                    print(" %s 's damage points have been decreased by 1 for this turn"%heroes)
                else:
                    print("%s 's damage points haven't been modified "%heroes)

            else:
                print("%s 's damage points haven't been modified "%heroes)

        #For the creatures
        for ennemies in creatures:
            if gap_calculator(positions,hero_name, ennemies) == 1:
                if creatures[ennemies]['damage_points'] >= 2:
                    creatures[ennemies]['damage_points'] -= 1
                    modif[ennemies]['damage_points_modifs'] -= 1
                    used += 1
                    print(" %s 's damage points have been decreased by 1 for this turn"%ennemies)
                else:
                    print("%s 's damage points haven't been modified "%ennemies)

            else:
                print("%s 's damage points haven't been modified "%ennemies)

    #Level of the hero = 4
    elif updated_dict[hero_name]['level'] == 4:
        #For the heroes of the other player
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, heroes) <= 2:
                if updated_dict[heroes]['damage_points'] >= 3:
                    updated_dict[heroes]['damage_points'] -= 2
                    modif[heroes]['damage_points_modifs'] -= 2
                    used += 1
                    print(" %s 's damage points have been decreased by 2 for this turn"%heroes)
                else:
                    print("%s 's damage points haven't been modified "%heroes)
            else:
                print("%s 's damage points haven't been modified "%heroes)

        #For creatures
        for ennemies in creatures:
            if gap_calculator(positions,hero_name, ennemies) <= 2:
                if creatures[ennemies]['damage_points'] >= 3:
                    creatures[ennemies]['damage_points'] -= 2
                    modif[ennemies]['damage_points_modifs'] -= 2
                    used += 1
                    print(" %s 's damage points have been decreased by 2 for this turn"%ennemies)
                else:
                    print("%s 's damage points haven't been modified "%ennemies)
            else:
                print("%s 's damage points haven't been modified "%ennemies)

    #Level of the hero = 5
    elif updated_dict[hero_name][level] == 5:
        #For the heroes of the other player
        for heroes in updated_dict:
            if gap_calculator(positions,hero_name, heroes) <= 3:
                if updated_dict[heroes]['damage_points'] >= 4:
                    updated_dict[heroes]['damage_points'] -= 3
                    modif[heroes]['damage_points_modifs'] -= 3
                    used += 1
                    print(" %s 's damage points have been decreased by 3 for this turn"%heroes)
                else:
                    print("%s 's damage points haven't been modified "%heroes)
            else:
                print("%s 's damage points haven't been modified "%heroes)

        #For creatures
        for ennemies in creatures:
            if gap_calculator(positions,hero_name, ennemies) <= 3:
                if creatures[ennemies]['damage_points'] >= 4:
                    creatures[ennemies]['damage_points'] -= 3
                    modif[ennemies]['damage_points_modifs'] -= 3
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
        good_dict[hero_name]['cooldown']['stun'] += 1
    else:
        print("You used stun but nothing happened ")

    return updated_dict, creatures, modif, good_dict
      
        


                
#n°2 : Healer

def invigorate(positions, hero_name, player1, player2, max_life_points, modif):
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
    updated_dict: Updated dictionary of the player which hero's using this attack.
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)

    Version:
    --------
    specification: Manon Michaux (v.2 27/03/19)
    implementation: Manon Michaux (v.2 27/03/19)

    """

    updated_dict, bad_dict = good_dict(hero_name)
    
    #Level of the hero = 2
    if updated_dict[hero_name]['level'] == 2:
            for heroes in updated_dict:
                if gap_calculator(positions,hero_name, heroes) == 1:
                    #Ally = barbarian
                    if updated_dict[heroes]['job'] == 'barbarian':
                        #Barbarian level == 1
                        if updated_dict[heroes]['level'] == 1:
                            if updated_dict[heroes]['life_points'] < max_life_points['barbarian'][1]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 2
                        if updated_dict[heroes]['level'] == 2:
                            if updated_dict[heroes]['life_points'] < max_life_points['barbarian'][2]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 3
                        if updated_dict[heroes]['level'] == 3:
                            if updated_dict[heroes]['life_points'] < max_life_points['barbarian'][3]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 4
                        if updated_dict[heroes]['level'] == 4:
                            if updated_dict[heroes]['life_points'] < max_life_points['barbarian'][4]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 5
                        else:
                            if updated_dict[heroes]['life_points'] < max_life_points['barbarian'][5]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                    #Ally = healer
                    if updated_dict[heroes]['job'] == 'healer':

                        #Healer level == 1
                        if updated_dict[heroes]['level'] == 1:
                            if updated_dict[heroes]['life_points'] < max_life_points['healer'][1]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 2
                        if updated_dict[heroes]['level'] == 2:
                            if updated_dict[heroes]['life_points'] < max_life_points['healer'][2]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 3
                        if updated_dict[heroes]['level'] == 3:
                            if updated_dict[heroes]['life_points'] < max_life_points['healer'][3]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 4
                        if updated_dict[heroes]['level'] == 4:
                            if updated_dict[heroes]['life_points'] < max_life_points['healer'][4]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 5
                        else:
                            if updated_dict[heroes]['life_points'] < max_life_points['barbarian'][5]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                    #Ally = mage
                    if updated_dict[heroes]['job'] == 'mage':

                        #Mage level == 1
                        if updated_dict[heroes]['level'] == 1:
                            if updated_dict[heroes]['life_points'] < max_life_points['mage'][1]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 2
                        if updated_dict[heroes]['level'] == 2:
                            if updated_dict[heroes]['life_points'] < max_life_points['mage'][2]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 3
                        if updated_dict[heroes]['level'] == 3:
                            if updated_dict[heroes]['life_points'] < max_life_points['mage'][3]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 4
                        if updated_dict[heroes]['level'] == 4:
                            if updated_dict[heroes]['life_points'] < max_life_points['mage'][4]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 5
                        else:
                            if updated_dict[heroes]['life_points'] < max_life_points['mage'][5]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        
                    #Ally = rogue
                    if updated_dict[heroes]['job'] == 'rogue':

                        #Rogue level == 1
                        if updated_dict[heroes]['level'] == 1:
                            if updated_dict[heroes]['life_points'] < max_life_points['rogue'][1]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 2
                        if updated_dict[heroes]['level'] == 2:
                            if updated_dict[heroes]['life_points'] < max_life_points['rogue'][2]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 3
                        if updated_dict[heroes]['level'] == 3:
                            if updated_dict[heroes]['life_points'] < max_life_points['rogue'][3]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 4
                        if updated_dict[heroes]['level'] == 4:
                            if updated_dict[heroes]['life_points'] < max_life_points['rogue'][4]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 5
                        else:
                            if updated_dict[heroes]['life_points'] < max_life_points['rogue'][5]:
                                updated_dict[heroes]['life_points'] += 1
                                modif[heroes]['life_points_modifs'] += 1
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                    else:
                        print(" Class isn't correct")

    #Level of the hero = 3
    elif updated_dict[hero_name]['level'] == 3:
            for heroes in updated_dict:
                if gap_calculator(positions,hero_name, heroes) == 2:
                    #Ally = barbarian
                    if updated_dict[heroes]['job'] == 'barbarian':
                        #Barbarian level == 1
                        if updated_dict[heroes][level] == 1:
                            max_health = max_life_points[barbarian][level_1] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 2
                        if updated_dict[heroes][level] == 2:
                            max_health = max_life_points[barbarian][level_2] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 3
                        if updated_dict[heroes][level] == 3:
                            max_health = max_life_points[barbarian][level_3] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 4
                        if updated_dict[heroes][level] == 4:
                            max_health = max_life_points[barbarian][level_4] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 5
                        else:
                            max_health = max_life_points[barbarian][level_5] - 2
                            if updated_dict[heroes][h_points] < max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                    #Ally = healer
                    if updated_dict[heroes][job] == healer:

                        #Healer level == 1
                        if updated_dict[heroes][level] == 1:
                            max_health = max_life_points[healer][level_1] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 2
                        if updated_dict[heroes][level] == 2:
                            max_health = max_life_points[healer][level_2] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 3
                        if updated_dict[heroes][level] == 3:
                            max_health = max_life_points[healer][level_3] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 4
                        if updated_dict[heroes][level] == 4:
                            max_health = max_life_points[healer][level_4] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 5
                        else:
                            max_health = max_life_points[healer][level_5] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                    #Ally = mage
                    if updated_dict[heroes][job] == mage:

                        #Mage level == 1
                        if updated_dict[heroes][level] == 1:
                            max_health = max_life_points[mage][level_1] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 2
                        if updated_dict[heroes][level] == 2:
                            max_health = max_life_points[mage][level_2] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 3
                        if updated_dict[heroes][level] == 3:
                            max_health = max_life_points[mage][level_3] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 4
                        if updated_dict[heroes][level] == 4:
                            max_health = max_life_points[mage][level_4] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 5
                        else:
                            max_health = max_life_points[mage][level_5] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        
                    #Ally = rogue
                    if updated_dict[heroes][job] == rogue:
                        
                        #Rogue level == 1
                        if updated_dict[heroes][level] == 1:
                            max_health = max_life_points[rogue][level_1] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 2
                        if updated_dict[heroes][level] == 2:
                            max_health = max_life_points[rogue][level_2] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 3
                        if updated_dict[heroes][level] == 3:
                            max_health = max_life_points[rogue][level_3] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 4
                        if updated_dict[heroes][level] == 4:
                            max_health = max_life_points[rogue][level_4] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 5
                        else:
                            max_health = max_life_points[rogue][level_5] - 2
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 2
                                modif[heroes][h_points_modifs] += 2
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                    else:
                        print(" Class isn't correct")


    #Level of the hero = 4
    elif updated_dict[hero_name][level] == 4:
            for heroes in updated_dict:
                if gap_calculator(positions,hero_name, heroes) == 3:
                    #Ally = barbarian
                    if updated_dict[heroes][job] == barbarian:
                        #Barbarian level == 1
                        if updated_dict[heroes][level] == 1:
                            max_health = max_life_points[barbarian][level_1] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 2
                        if updated_dict[heroes][level] == 2:
                            max_health = max_life_points[barbarian][level_2] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 3
                        if updated_dict[heroes][level] == 3:
                            max_health = max_life_points[barbarian][level_3] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modif] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 4
                        if updated_dict[heroes][level] == 4:
                            max_health = max_life_points[barbarian][level_4] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 5
                        else:
                            max_health = max_life_points[barbarian][level_5] - 3
                            if updated_dict[heroes][h_points] < max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                    #Ally = healer
                    if updated_dict[heroes][job] == healer:

                        #Healer level == 1
                        if updated_dict[heroes][level] == 1:
                            max_health = max_life_points[healer][level_1] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 2
                        if updated_dict[heroes][level] == 2:
                            max_health = max_life_points[healer][level_2] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 3
                        if updated_dict[heroes][level] == 3:
                            max_health = max_life_points[healer][level_3] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 4
                        if updated_dict[heroes][level] == 4:
                            max_health = max_life_points[healer][level_4] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 5
                        else:
                            max_health = max_life_points[healer][level_5] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                    #Ally = mage
                    if updated_dict[heroes][job] == mage:

                        #Mage level == 1
                        if updated_dict[heroes][level] == 1:
                            max_health = max_life_points[mage][level_1] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 2
                        if updated_dict[heroes][level] == 2:
                            max_health = max_life_points[mage][level_2] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 3
                        if updated_dict[heroes][level] == 3:
                            max_health = max_life_points[mage][level_3] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 4
                        if updated_dict[heroes][level] == 4:
                            max_health = max_life_points[mage][level_4] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 5
                        else:
                            max_health = max_life_points[mage][level_5] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        
                    #Ally = rogue
                    if updated_dict[heroes][job] == rogue:
                        
                        #Rogue level == 1
                        if updated_dict[heroes][level] == 1:
                            max_health = max_life_points[rogue][level_1] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 2
                        if updated_dict[heroes][level] == 2:
                            max_health = max_life_points[rogue][level_2] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 3
                        if updated_dict[heroes][level] == 3:
                            max_health = max_life_points[rogue][level_3] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 4
                        if updated_dict[heroes][level] == 4:
                            max_health = max_life_points[rogue][level_4] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 5
                        else:
                            max_health = max_life_points[rogue][level_5] - 3
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 3
                                modif[heroes][h_points_modifs] += 3
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                    else:
                        print(" Class isn't correct")

    #Level of the hero = 5
    elif updated_dict[hero_name][level] == 5:
            for heroes in updated_dict:
                if gap_calculator(positions,hero_name, heroes) == 4:
                    #Ally = barbarian
                    if updated_dict[heroes][job] == barbarian:
                        #Barbarian level == 1
                        if updated_dict[heroes][level] == 1:
                            max_health = max_life_points[barbarian][level_1] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 2
                        if updated_dict[heroes][level] == 2:
                            max_health = max_life_points[barbarian][level_2] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 3
                        if updated_dict[heroes][level] == 3:
                            max_health = max_life_points[barbarian][level_3] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 4
                        if updated_dict[heroes][level] == 4:
                            max_health = max_life_points[barbarian][level_4] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Barbarian level == 5
                        else:
                            max_health = max_life_points[barbarian][level_5] - 4
                            if updated_dict[heroes][h_points] < max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                    #Ally = healer
                    if updated_dict[heroes][job] == healer:

                        #Healer level == 1
                        if updated_dict[heroes][level] == 1:
                            max_health = max_life_points[healer][level_1] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 2
                        if updated_dict[heroes][level] == 2:
                            max_health = max_life_points[healer][level_2] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 3
                        if updated_dict[heroes][level] == 3:
                            max_health = max_life_points[healer][level_3] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 4
                        if updated_dict[heroes][level] == 4:
                            max_health = max_life_points[healer][level_4] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Healer level == 5
                        else:
                            max_health = max_life_points[healer][level_5] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                    #Ally = mage
                    if updated_dict[heroes][job] == mage:

                        #Mage level == 1
                        if updated_dict[heroes][level] == 1:
                            max_health = max_life_points[mage][level_1] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 2
                        if updated_dict[heroes][level] == 2:
                            max_health = max_life_points[mage][level_2] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 3
                        if updated_dict[heroes][level] == 3:
                            max_health = max_life_points[mage][level_3] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 4
                        if updated_dict[heroes][level] == 4:
                            max_health = max_life_points[mage][level_4] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Mage level == 5
                        else:
                            max_health = max_life_points[mage][level_5] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        
                    #Ally = rogue
                    if updated_dict[heroes][job] == rogue:
                        
                        #Rogue level == 1
                        if updated_dict[heroes][level] == 1:
                            max_health = max_life_points[rogue][level_1] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 2
                        if updated_dict[heroes][level] == 2:
                            max_health = max_life_points[rogue][level_2] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 3
                        if updated_dict[heroes][level] == 3:
                            max_health = max_life_points[rogue][level_3] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 4
                        if updated_dict[heroes][level] == 4:
                            max_health = max_life_points[rogue][level_4] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                        #Rogue level == 5
                        else:
                            max_health = max_life_points[rogue][level_5] - 4
                            if updated_dict[heroes][h_points] <= max_health:
                                updated_dict[heroes][h_points] += 4
                                modif[heroes][h_points_modifs] += 4
                                used += 1
                                print("%s ' health points have been increased by one for this turn"%heroes)
                            else:
                                print("%s ' health points haven't been modified "%heroes)

                    else:
                        print(" Class isn't correct")

    #Level of the hero = 1 
    else:
        print(" You can't use this attack yet")


    #Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        good_dict[hero_name][cooldown][stun] += 1
    else:
        print("You used stun but nothing happened ")

    return updated_dict, modif               

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
    implementation: Manon Michaux (v.3 26/03/19)

    """
 





                        

                                
                                
                                
    
    

