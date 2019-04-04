from heroes_namur_gr_06 import *


def reach_level(level, updated, hero_name, positions, coordinates, used):
    """When a hero wants to use reach depending on his level.

    Parameters:
    -----------
    level: Level the hero is on (int)
    updated: Updated dictionary of the player which hero is using this attack (dict)
    hero_name: Name of the hero (str)
    positions: Contains all the coordinates of the board (dict)
    coordinates: Where the hero wants to use ovibus (tupl)
    used:

    Returns:
    --------
    updated: Updated dictionary of the player which hero is using this attack (dict)
    positions: Contains all the coordinates of the board updated (dict)
    used:

    Version:
    --------
    specification: Aude Lekeux (v.1 04/04/19)
    implementation: Aude Lekeux (v.1 04/04/19)
    """

    character_list = []
    unoccupied = 0

    if updated[hero_name]['level'] == level:
        if gap_calculator(positions[hero_name], coordinates) == level - 1:

            # For the all the characters in positions
            for characters in positions:
                if gap_calculator(positions[characters], coordinates) == 0:
                    print(characters + "is already on those coordinates right now")
                else:
                    unoccupied += 1
                character_list += characters
        else:
            print("The coordinates you tried to reach are too far away right now")

        # If none of the characters are on the target coordinates
        if unoccupied == len(character_list):
            positions[hero_name] = coordinates
            used += 1

    return updated, positions, used


def reach(positions, hero_name, coordinates, modif):
    """Teleports the hero using the attack if he is the first using reach this turn and if the target coordinates aren't occupied.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    coordinates: Where the hero wants to use ovibus (tupl)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)

    Returns:
    --------
    positions: Contains all the coordinates of the board (dict)
    updated: Updated dictionary of the player which hero is using this attack (dict)
    modif: Dictionary which contains each modification of the damage point / health points of each hero / creature and if they are immunised(dict)

    Version:
    --------
    specification: Manon Michaux (v.2 03/04/19)
    implementation: Manon Michaux (v.2 03/04/19)
    """

    updated, bad_dict = good(hero_name)
    used = 0

    # Level of the hero from 1 to 5
    for level in range(2, 6):
        # Level from 3 to 5
        if level in range(3, 6):
            updated, positions, used = reach_level(level, updated, hero_name, positions, coordinates, used)
        # Level from 1 to 2
        else:
            print("You can't use this attack yet")

    # Adding the cooldown to the dictionary of the player if he attack has been used
    if used == 1:
        good[hero_name]['cooldown']['ovibus'] += 1
    else:
        print("You used stun but nothing happened ")

    return positions, updated, modif


def burst_level(level, hero_name, positions, updated, creatures, used):
    """When a hero wants to use burst depending on his level.

    Parameters:
    -----------
    level: Level the hero is on (int)
    hero_name: Name of the hero (str)
    positions: Contains all the coordinates of the board (dict)
    updated: Updated dictionary of the player which hero's using this attack (dict)
    creatures: All the data about creatures (dict)
    used:

    Returns:
    --------
    positions: Contains all the coordinates of the board updated (dict)
    updated: Updated dictionary of the player which hero's using this attack (dict)
    creatures: All the data about creatures updated (dict)
    used:

    Version:
    --------
    specification: Aude Lekeux (v.1 04/04/19)
    implementation: Aude Lekeux (v.1 04/04/19)
    """

    if good[hero_name]['level'] == level:

        # For heroes of the other player
        for heroes in updated:
            # If level equals 3
            if level == 3:
                if gap_calculator(positions[hero_name], positions[heroes]) == 1:
                    updated[heroes]['life_points'] -= 1
                    used += 1
                    print(hero_name + "'s health points have been decreased by 1")
                else:
                    print(hero_name + "' health points haven't been modified")
            # Level from 4 to 5
            else:
                if gap_calculator(positions[hero_name], positions[heroes]) <= level - 2:
                    updated[heroes]['life_points'] -= level - 2
                    used += 1
                    print(hero_name + "'s health points have been decreased by 1")
                else:
                    print(hero_name + "' health points haven't been modified")

        # For the creatures
        for enemies in creatures:
            # If level equals 3
            if level == 3:
                if gap_calculator(positions[hero_name], positions[enemies]) == 1:
                    updated[enemies]['life_points'] -= 1
                    used += 1
                    print(enemies + "'s health points have been decreased by 1")
                else:
                    print(enemies + "' health points haven't been modified")
            # Level from 4 to 5
            else:
                if gap_calculator(positions[hero_name], positions[enemies]) <= level - 2:
                    updated[enemies]['life_points'] -= level - 2
                    used += 1
                    print(enemies + "'s health points have been decreased by 1")
                else:
                    print(enemies + "' health points haven't been modified")

    return positions, updated, creatures, used


def burst(positions, hero_name, creatures):
    """The creatures/ennemies in the hero's wage lose a given number of health points.
    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    creatures: All the data about creatures (dict)

    Returns:
    --------
    updated: Updated dictionary of the player which hero's using this attack.
    good:  Updated dictionary of the player which hero is using this attack.
    creatures: All the data about creatures (dict)

    Version:
    --------
    specification: Manon Michaux (v.2 03/04/19)
    implementation: Manon Michaux (v.1 03/04/19)
    """

    good, updated = good(hero_name)
    used = 0

    # Level of the hero from 1 to 5
    for level in range(1, 6):
        # Level from 3 to 5
        if level in range(3, 6):
            positions, updated, creatures, used = burst_level(level, hero_name, positions, updated, creatures, used)
        # Level of the hero from 1 to 2
        else:
            print(" You can't use this special attack yet")

    # Adding the cooldown to the dictionary of the player if the attack has been used
    if used >= 1:
        updated[hero_name]['cooldown'][burst] += 1
    else:
        print("You used burst but nothing happened")

    return updated, good, creatures
