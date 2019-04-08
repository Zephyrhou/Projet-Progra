def invigorate_level(hero, type, level_hero, level_ally, updated, used):
    """If a hero want's to use invigorate.

    Parameters:
    -----------
    hero:
    type:
    level_hero:
    level_ally:
    updated:
    used:

    Returns:
    --------
    updated:
    used:

    Version:
    --------
    specification: Aude Lekeux (v.1 03/04/19)
    implementation: Aude Lekeux (v.1 03/04/19)
    """

    if level_hero == 2:
        if updated[hero]['level'] == level_ally:
            if updated[hero]['life_points'] < max_life_points[type][level]:
                updated[hero]['life_points'] += 1
                used += 1
                print(hero + "' health points have been increased by one for this turn")
            else:
                print(hero + "' health points haven't been modified")

    elif level_hero == 3:
        if updated[hero]['level'] == level_ally:
            max_health = max_life_points[type][level_ally] - 2
            if updated[hero]['life_points'] <= max_health:
                updated[hero]['life_points'] += 2
                used += 1
                print(hero + "' health points have been increased by one for this turn")
            else:
                print(hero + "' health points haven't been modified")

    elif level_hero == 4:
        if updated[hero]['level'] == level_ally:
            max_health = max_life_points[type][level_ally] - 3
            if updated[hero]['life_points'] <= max_health:
                updated[hero]['life_points'] += 3
                used += 1
                print(hero + "' health points have been increased by one for this turn")
            else:
                print(hero + "' health points haven't been modified")

    elif level_hero == 5:
        if updated[hero]['level'] == level_ally:
            max_health = max_life_points[type][level_ally] - 4
            if updated[hero]['life_points'] <= max_health:
                updated[hero]['life_points'] += 4
                modif[hero]['life_points_modifs'] += 4
                used += 1
                print(hero + "' health points have been increased by one for this turn")
            else:
                print(hero + "' health points haven't been modified")

    return updated, used


def invigorate(positions, hero_name, player):
    """Raise the health points of the allies in the hero's wage.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero_name: Name of the hero (str)
    player: Level, number of point, etc. of the heroes of player (dict)
    max_health_dict: Dictionary containing for each class and for each level their own maximum of health points (dict)

    Returns:
    --------
    updated: Updated dictionary of the player which hero's using this attack.

    Version:
    --------
    specification: Manon Michaux (v.2 27/03/19)
    implementation: Manon Michaux (v.4 03/04/19)
    """

    updated, bad_dict = good(hero_name)
    used = 0

    # Level of the hero from 2 to 5
    for level_hero in range(2, 6):
        if updated[hero_name]['level'] == level_hero:
            for heroes in updated:
                if gap_calculator(positions, hero_name, heroes) == level_hero - 1:

                    for type in dict_job:
                        if updated[heroes]['job'] == type:
                            # Level of the ally from 1 to 5
                            for level_ally in range(1, 6):
                                updated, used = invigorate_level(heroes, type, level_hero, level_ally, updated, used)
                        else:
                            print(" Class isn't correct")

    # Level of the hero = 1
    else:
        print(" You can't use this attack yet")

    # Adding the cooldown to the dictionary of the player if he attack has been used
    if used >= 1:
        good(hero_name)['cooldown']['stun'] += 1
    else:
        print("You used stun but nothing happened")

    return updated


def immunise(positions, player, creatures, hero_name, coordinates):
    """

    :return:
    """
