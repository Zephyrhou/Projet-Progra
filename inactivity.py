def inactivity(positions, initial_positions, creatures, initial_creatures, inactivity_time):
    """Count the inactivity of the players.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board and the heroes (dict)
    initial_positions: Contains all the coordinates of the board and the heroes before changes (dict)
    creatures: Has every information of each creature (dict)
    initial_creatures: Has every information of each creature before changes (dict)
    inactivity_time: Number of turns no changes has been made (int)

    Returns:
    --------
    inactivity_time: Number of turns where the game is inactive (int)
    game_over: If the game is over or not depending on inactivity_time (bool)

    Notes:
    ------
    If no changes has been made in the game (no moves, no attacks, etc.) for 40 turns then the game is over.

    Versions:
    ---------
    specification: Zéphyr Houyoux(v.2 05/04/19)
    implementation: Zéphyr Houyoux(v.4 06/04/19)
    """

    is_game_over = False

    # If no changes has been made to positions
    if positions == initial_positions:
        # If no changes has been made in creatures
        if len(creatures) == len(initial_creatures):

            # Then inactivity increased by one
            inactivity_time += 1
            if inactivity_time >= 40:
                is_game_over = True
            else:
                is_game_over = False

    return inactivity_time, is_game_over


initial_positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'),
                     'Lee': ('24', '3'), 'May': ('14', '6'), 'Rob': ('20', '17'), 'Buf': ('20', '17'),
                     'Lia': ('19', '7'), 'Mey': ('3', '3'), 'Tob': ('2', '37'), ('20', '38'): 'spur',
                     ('20', '39'): 'spur', ('21', '38'): 'spur', ('21', '39'): 'spur',
                     ('10', '10'): ['bear', '20', '5', '3', '100'], ('10', '20'): ['bear', '20', '5', '3', '100'],
                     ('15', '10'): ['wolf', '10', '3', '2', '50']}

positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'),
             'Lee': ('24', '3'), 'May': ('14', '6'), 'Rob': ('20', '17'), 'Buf': ('20', '17'), 'Lia': ('19', '7'),
             'Mey': ('3', '3'), 'Tob': ('2', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ['bear', '20', '5', '3', '100'],
             ('10', '20'): ['bear', '20', '5', '3', '100'], ('15', '10'): ['wolf', '10', '3', '2', '50']}

initial_creatures = ['bear', 'bear', 'wolf']
creatures = ['bear', 'bear', 'wolf']

inactivity_time = 36

print(inactivity(positions, initial_positions, creatures, initial_creatures, inactivity_time))
