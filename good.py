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

    for heroes_names in dict_player1:
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