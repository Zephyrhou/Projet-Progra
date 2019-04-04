from heroes_namur_gr_06 import *


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

    updated_dict, bad_dict = good(hero_name)
    character_list = []

    # Level of the hero = 2
    if updated_dict[hero_name][level] == 2:
        if gap_calculator(positions, hero_name, coordinates) == 1:
            # For the all the characters in positions
            for characters in positions:
                if gap_calculator(positions, coordinates, characters) == 0:
                    print("%s is already on those coordinates right now" % characters)
                else:
                    unoccupied += 1
                character_list += characters
        else:
            print("The coordinates you tried to reach are too far away right now")

        # if none of the characters are on the target coordinates
        if unoccupied == len(character_list):
            positions[hero_name] = coordinates
            used += 1

    # Level of the hero = 3
    if updated_dict[hero_name][level] == 3:
        if gap_calculator(positions, hero_name, coordinates) <= 2:  # For the all the characters in positions
            for characters in positions:
                if gap_calculator(positions, coordinates, characters) == 0:
                    print("%s is already on those coordinates right now" % characters)

                else:
                    unoccupied += 1
                character_list += characters
        else:
            print("The coordinates you tried to reach are too far away right now")

        # if none of the characters are on the target coordinates
        if unoccupied == len(character_list):
            positions[hero_name] = coordinates
            used += 1

    # Level of the hero = 4
    if updated_dict[hero_name][level] == 4:
        if gap_calculator(positions, hero_name, coordinates) <= 3:  # For the all the characters in positions
            for characters in positions:
                if gap_calculator(positions, coordinates, characters) == 0:
                    print("%s is already on those coordinates right now" % characters)

                else:
                    unoccupied += 1
                character_list += characters
        else:
            print("The coordinates you tried to reach are too far away right now")

        # if none of the characters are on the target coordinates
        if unoccupied == len(character_list):
            positions[hero_name] = coordinates
            used += 1

    # Level of the hero = 5
    if updated_dict[hero_name][level] == 5:
        if gap_calculator(positions, hero_name, coordinates) <= 4:  # For the all the characters in positions
            for characters in positions:
                if gap_calculator(positions, coordinates, characters) == 0:
                    print("%s is already on those coordinates right now" % characters)

                else:
                    unoccupied += 1
                character_list += characters
        else:
            print("The coordinates you tried to reach are too far away right now")

        # if none of the characters are on the target coordinates
        if unoccupied == len(character_list):
            positions[hero_name] = coordinates
            used += 1


    # Level of the hero = 1 or = 2
    else:
        print("You can't use this attack yet")

    # Adding the cooldown to the dictionary of the player if he attack has been used
    if used == 1:
        good_dict[hero_name][cooldown][ovibus] += 1
    else:
        print("You used stun but nothing happened ")

    return updated_dict, positions, modif


def burst(positions, hero_name, player1, player2, creatures, modif):
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

    good, updated = good(hero_name)

    # Level of the hero = 3
    if good[hero_name][level] == 3:
        # For heroes of the other player
        for heroes in updated:
            if gap_calculator(positions, hero_name, heroes) == 1:
                updated[heroes][h_points] -= 1
                used += 1
                print("%s 's health points have been decreased by 1 " % heroes)
            else:
                print("%s ' health points haven't been modified" % heroes)
        # For the creatures
        for enemies in creatures:
            if gap_calculator(positions, hero_name, enemies) == 1:
                updated[enemies][h_points] -= 1
                used += 1
                print("%s 's health points have been decreased by 1 " % enemies)
            else:
                print("%s ' health points haven't been modified" % enemies)

    # Level of the hero = 4
    elif good[hero_name][level] == 4:
        # For heroes of the other player
        for heroes in updated:
            if gap_calculator(positions, hero_name, heroes) <= 2:
                updated[heroes][h_points] -= 2
                used += 1
                print("%s 's health points have been decreased by 2 " % heroes)
            else:
                print("%s ' health points haven't been modified" % heroes)

        # For the creatures
        for enemies in creatures:
            if gap_calculator(positions, hero_name, enemies) <= 2:
                updated[enemies][h_points] -= 2
                used += 1
                print("%s 's health points have been decreased by 2 " % enemies)
            else:
                print("%s ' health points haven't been modified" % enemies)

    # Level of the hero = 5
    elif good_dict[hero_name][level] == 5:
        # For heroes of the other player
        for heroes in updated_dict:
            if gap_calculator(positions, hero_name, heroes) <= 3:
                updated_dict[heroes][h_points] -= 3
                used += 1
                print("%s 's health points have been decreased by 3 " % heroes)
            else:
                print("%s ' health points haven't been modified" % heroes)

    # For the creatures
    for ennemies in creatures:
        if gap_calculator(positions, hero_name, enemies) <= 3:
            updated_dict[ennemies][h_points] -= 3
            used += 1
            print("%s 's health points have been decreased by 3 " % ennemies)
        else:
            print("%s ' health points haven't been modified" % ennemies)

    # Level of the hero = 1 or = 2
    else:
        print(" You can't use this special attack yet")

    # Adding the cooldown to the dictionary of the player if the attack has been used
    if used >= 1:
        updated_dict[heroes][cooldown][burst] += 1
    else:
        print("You used burst but nothing happened")

    return updated_dict, good_dict, modif, creatures
