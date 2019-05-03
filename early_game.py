def early_game(nb_turn):
    """Check if we are in the 20 first turn.

    Parameters:
    -----------

    Returns:
    --------
    early: Is game in the 20 first turn or not(bool)

    Versions:
    ---------
    specification:
    implementation:
    """

    nb_turn += 1
    if nb_turn > 20:
        return nb_turn, 0
    else:
        return nb_turn, 1
