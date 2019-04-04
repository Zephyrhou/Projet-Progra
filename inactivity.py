def inactivity(positions, inactivity, incativity_time):
    """Count the inactivity of the players.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board and the heroes(dict)
    inactivity: Contains all the coordinates of the board and the heroes of the previous turn(dict)

    Returns:
    --------
    inactivity: Contains all the coordinates of the board and the heroes of the previous turn(dict)
    inactivity_time: Number of inactivity turn(int)

    Versions:
    ---------
    specification: Zéphyr Houyoux(v.1 17/03/19)
    implementation: Zéphyr Houyoux(v.2 17/03/19)
    """

    if positions == inactivity:
        inactivity_time =+ 1
    inactivity = positions

    return inactivity, inactivity_time

