from heroes_namur_gr_06 import *


def fulgura(coordinates, creatures, hero_name, modif, positions):
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

    good, updated = good(hero_name)
    used = 0

    # Level of the hero = 2
    if good[hero_name]['level'] == 2:
        if gap_calculator(positions, hero_name, coordinates) == 1:
            # For the heroes of the other player
            for heroes in updated:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    updated[heroes]['life_points'] -= 3
                    used += 1
                    print(" %s 's health points have been decreased by 3 " % heroes)
                else:
                    print("%s 's damage points haven't been modified " % heroes)
            # For the creatures
            for enemies in creatures:
                if gap_calculator(positions, hero_name, enemies) == 0:
                    creatures[enemies]['life_points'] -= 3
                    used += 1
                    print(" %s 's health points have been decreased by 3" % enemies)
                else:
                    print("%s 's damage points haven't been modified " % enemies)

            else:
                print("%s 's damage points haven't been modified " % enemies)

    # Level of the hero = 3
    elif good[hero_name][level] == 3:
        if gap_calculator(positions, hero_name, coordinates) <= 2:  # For the heroes of the other player
            for heroes in updated:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    updated[heroes][h_points] -= 3
                    used += 1
                    print(" %s 's health points have been decreased by 3 " % heroes)
                else:
                    print("%s 's damage points haven't been modified " % heroes)
            # For the creatures
            for enemies in creatures:
                if gap_calculator(positions, hero_name, enemies) == 0:
                    creatures[enemies][h_points] -= 3
                    used += 1
                    print(" %s 's health points have been decreased by 3" % enemies)
                else:
                    print("%s 's damage points haven't been modified " % enemies)

            else:
                print("%s 's damage points haven't been modified " % enemies)

    # Level of the hero = 4
    elif good[hero_name][level] == 4:
        if gap_calculator(positions, hero_name, coordinates) <= 3:  # For the heroes of the other player
            for heroes in updated:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    updated[heroes][h_points] -= 4
                    used += 1
                    print(" %s 's health points have been decreased by 4 " % heroes)
                else:
                    print("%s 's damage points haven't been modified " % heroes)
            # For the creatures
            for enemies in creatures:
                if gap_calculator(positions, hero_name, enemies) == 0:
                    creatures[enemies][h_points] -= 4
                    used += 1
                    print(" %s 's health points have been decreased by 4" % enemies)
                else:
                    print("%s 's damage points haven't been modified " % enemies)

            else:
                print("%s 's damage points haven't been modified " % enemies)

    # Level of the hero = 5
    elif good[hero_name][level] == 5:
        if gap_calculator(positions, hero_name, coordinates) <= 4:  # For the heroes of the other player
            for heroes in updated:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    updated[heroes][h_points] -= 4
                    used += 1
                    print(" %s 's health points have been decreased by 4 " % heroes)
                else:
                    print("%s 's damage points haven't been modified " % heroes)
            # For the creatures
            for enemies in creatures:
                if gap_calculator(positions, hero_name, enemies) == 0:
                    creatures[enemies][h_points] -= 4
                    used += 1
                    print(" %s 's health points have been decreased by 4" % enemies)
                else:
                    print("%s 's damage points haven't been modified " % enemies)

            else:
                print("%s 's damage points haven't been modified " % enemies)

    # Level of the hero = 1 or = 2
    else:
        print(" You can't use this attack yet")

    # Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        good[hero_name][cooldown][fulgura] += 1
    else:
        print("You used stun but nothing happened ")

    return updated, creatures, modif, good


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

    good_dict, updated_dict = good_dict(hero_name)

    # Level of the hero = 3
    if good_dict[hero_name][level] == 3:
        if gap_calculator(positions, hero_name, coordinates) == 1:
            # For the heroes of the player
            for heroes in updated_dict:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    modif[heroes][confused] += 1
                    used += 1
                    print("%s is confused for one turn" % heroes)

                else:
                    print("Those coordinates don't belong to %s" % heroes)

            # For the creatures
            for ennemy in creatures:
                if gap_calculator(positions, coordinates, ennemy) == 0:
                    modif[ennemy][confused] += 1
                    used += 1
                    print("%s is confused for one turn" % heroes)
                else:
                    print("Those coordinates don't belong to %s" % heroes)

            print("The coordinates you tried to reach are too far away right now")

    # Level of the hero = 4
    elif good_dict[hero_name][level] == 4:
        if gap_calculator(positions, hero_name, coordinates) <= 2:  # For the heroes of the player
            for heroes in updated_dict:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    modif[heroes][confused] += 2
                    used += 1
                    print("%s is confused for one turn" % heroes)

                else:
                    print("Those coordinates don't belong to %s" % heroes)

            # For the creatures
            for ennemy in creatures:
                if gap_calculator(positions, coordinates, ennemy) == 0:
                    modif[ennemy][confused] += 2
                    used += 1
                    print("%s is confused for one turn" % heroes)
                else:
                    print("Those coordinates don't belong to %s" % heroes)

            print("The coordinates you tried to reach are too far away right now")

    # Level of the hero = 5
    elif good_dict[hero_name][level] == 5:
        if gap_calculator(positions, hero_name, coordinates) <= 3:  # For the heroes of the player
            for heroes in updated_dict:
                if gap_calculator(positions, coordinates, heroes) == 0:
                    modif[heroes][confused] += 3
                    used += 1
                    print("%s is confused for one turn" % heroes)

                else:
                    print("Those coordinates don't belong to %s" % heroes)

            # For the creatures
            for ennemy in creatures:
                if gap_calculator(positions, coordinates, ennemy) == 0:
                    modif[ennemy][confused] += 3
                    used += 1
                    print("%s is confused for one turn" % heroes)
                else:
                    print("Those coordinates don't belong to %s" % heroes)

            print("The coordinates you tried to reach are too far away right now")

    # Level of the hero = 1 or = 2
    else:
        print("You can't use this attack yet")

    # Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        good_dict[hero_name][cooldown][ovibus] += 3
    else:
        print("You used stun but nothing happened ")

    return updated_dict, good_dict, creatures, modif
