from heroes_namur_gr_06 import *


def is_game_over(nb_turns_wanted, nb_turns1, nb_turns2, inactivity_time, positions, initial_positions, creatures, initial_creatures):
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
    specification: Aude Lekeux (v.5 07/04/2019)
    implementation: Zéphyr Houyoux (v.3 07/04/2019)
    """

    if nb_turns1 == nb_turns_wanted or nb_turns2 == nb_turns_wanted:
        return True

    i_time = inactivity(positions, initial_positions, creatures, initial_creatures, inactivity_time)
    print(i_time[0])
    if i_time[0] >= 40:
        return True
    else:
        return False


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

nb_turns_wanted = 25
nb_turns1 = 0
nb_turns2 = 24
inactivity_time = 39
print(is_game_over(nb_turns_wanted, nb_turns1, nb_turns2, inactivity_time, positions, initial_positions, creatures, initial_creatures))
