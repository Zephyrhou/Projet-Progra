def inactivity(dico_positions, dico_inactivity, incativity_time):    """Count the inactivity of the players.

    Parameters:
    -----------
    dico_positions: Contains all the coordinates of the board and the heroes(dict)
    dico_inactivity: Coutains all the coordinates of the board and the heroes of the previous turn(dict)

    Returns:
    --------
    dico_inactivity: Coutains all the coordinates of the board and the heroes of the previous turn(dict)
    inactivity_time: Number of inactivity turn(int)


    Versions:
    ---------
    specification: Zéphyr Houyoux(17/03/19)
    implementation: Zéphyr Houyoux(17/03/19)
    """
    if dico_positions == dico_inactivity:
        inactivity_time =+ 1
    dico_inactivity = dico_positions
    return dico_inactivity, inactivity_time

