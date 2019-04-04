def is_game_over(nb_turns_wanted, nb_turns1, nb_turns2, inactivity_time):
    """Checks whether the game is over or not.

    Parameters:
    -----------
    nb_turns_wanted: Number of turns the heroes need to be on spur to win (int)
    nb_turns1: Number of turns a hero of player1 stands on the spur (int)
    nb_turns2: Number of turns a hero of player2 stands on the spur (int)
    inactivity_time: Number of turns no activity has been observed (int)

    Returns:
    -------
    game_over: Is the game over or not (bool)

    Notes:
    ------
    A hero must stay for a given number of consecutive turns on the spur in order to win, this number is in board_file.

    Version:
    --------
    specification: Aude Lekeux (v.4 04/03/2019)
    implementation: Zéphyr Houyoux (v.1 03/04/2019)
    """

    if nb_turns_wanted == nb_turns1 or nb_turns2:
        return True
    elif inactivity_time == 40:
        return True
    else:
        return False
