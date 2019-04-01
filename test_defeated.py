def defeated(player, nb_player, creature, positions):
    """Whenever a hero or a creature is defeated.

    Parameters:
    -----------
    player: Information on the player's defeated hero who will respawn (dict)
    creature: Information on the creature that dies (dict)
    positions: Contains all the coordinates of the board (dict)

    Returns:
    --------
    player: Information on the player's defeated hero who will respawn (dict)
    position: Contains all the coordinates of the board (dict)

    Notes:
    ------
    A hero or a creature is defeated whenever their health points are at O or less.
    When a hero is defeated he respawns.
    When a creature is defeated it dies and it's victory points are distributed to the heroes around.

    Version:
    --------
    specification: Aude Lekeux (v.5 04/03/2019)
    implementation: Aude Lekeux (v.3 19/03/19)
    """

    if player['life_points'] <= 0:
        if nb_player == 1:
            positions[player] = 'spawn_player_1'
        if nb_player == 2:
            positions[player] = 'spawn_player_2'
        print('The player', player, 'is respawn')
    if positions[creature] <= 0:
        del positions[creature]
        print('The creature', creature, 'is dead')

    return player, positions
