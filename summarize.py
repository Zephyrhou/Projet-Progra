def summarize(initial_creatures, creatures, nb_turns, nb_turns_left, initial_positions, positions, ROWS, COLUMNS):
    """Summarizes the state of the game.

    Parameters:
    -----------
    creatures: All the data about creatures (dict)
    nb_turns: Number of turns of the game (int)
    nb_turns_left: Number of turns left for a player to win the game (int)
    positions: positions: Contains all the coordinates of the board (dict)
    ROWS: Number of rows of the board (int)
    COLUMNS: Number of columns of the board (int)

    Version:
    --------
    specification: Manon Michaux (v.3 04/04/19)
    implementation: Aude Lekeux (v.2 04/04/19)
    """

    # Whenever a hero has moved
    for hero in positions:
        if positions[hero] != initial_positions[hero]:

            # Whenever a hero has been respawning
            for key, value in positions.copy().items():
                if positions[hero] == key:
                    print(hero + ' has been respawning to ' + str(key))

            print(hero + ' moved from ' + str(initial_positions[hero]) + ' to ' + str(positions[hero]))

    # Whenever a creature has been defeated
    for creature in range(1, len(creatures)):
        if creatures[creature] != initial_creatures[creature]:
            print(initial_creatures[creature] + ' has been defeated')

    # print('Creatures = ' + creatures)
    # print('Positions = ' + positions) 
    # print('Number of turns played = ' + nb_turns)
    # display_board(ROWS, COLUMNS, positions)

    # Resets initial positions to positions
    initial_positions = positions
    # Resets initial creatures to creatures
    initial_creatures = creatures

    return initial_positions, positions, initial_creatures, creatures


initial_positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'),
                     'Lee': ('24', '3'), 'May': ('14', '6'), 'Rob': ('20', '17'), 'Buf': ('20', '17'),
                     'Lia': ('19', '7'), 'Mey': ('3', '3'), 'Tob': ('2', '37'), ('20', '38'): 'spur',
                     ('20', '39'): 'spur', ('21', '38'): 'spur', ('21', '39'): 'spur',
                     ('10', '10'): ['bear', '20', '5', '3', '100'], ('10', '20'): ['bear', '20', '5', '3', '100'],
                     ('15', '10'): ['wolf', '10', '3', '2', '50']}

positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'), 'Lee': ('24', '3'),
             'May': ('14', '6'), 'Rob': ('20', '24'), 'Buf': ('20', '17'), 'Lia': ('20', '37'), 'Mey': ('3', '3'),
             'Tob': ('6', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ['bear', '20', '5', '3', '100'],
             ('10', '20'): ['bear', '20', '5', '3', '100'], ('15', '10'): ['wolf', '10', '3', '2', '50']}

initial_creatures = ['bear', 'bear', 'wolf']

creatures = ['bear', 'wolf']

nb_turns = 0
nb_turns_left = 0
ROWS = 0
COLUMNS = 0

initial_positions, positions, initial_creatures, creatures = \
    summarize(initial_creatures, creatures, nb_turns, nb_turns_left, initial_positions, positions, ROWS, COLUMNS)
