def gap_calculator(positions, character_1, character_2):
    """Computes the gap between two characters.

    Parameter:
    -----------
    positions: Contains all the coordinates of the board (dict)
    character_1: Name of the first character (str)
    character_2: Name of the second character (str)

    Returns:
    -------
    gap: Gap between two characters (int)

    Version:
    --------
    specification: Manon Michaux (v.2 04/04/19)
    implementation: Zéphyr Houyoux (v.2 04/04/19)
    """

    pos1h = int(positions[character_1][0])
    pos1l = int(positions[character_1][1])
    pos2h = int(positions[character_2][0])
    pos2l = int(positions[character_2][1])

    gap = ((pos1l - pos2l) ** 2 + (pos1h - pos2h) ** 2) ** 0.5

    return gap


positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'), 'Lee': ('24', '3'),
             'May': ('14', '6'), 'Rob': ('20', '17'), 'Buf': ('20', '16'), 'Lia': ('19', '7'), 'Mey': ('3', '3'),
             'Tob': ('2', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ['bear', '20', '5', '3', '100'],
             ('10', '20'): ['bear', '20', '5', '3', '100'], ('15', '10'): ['wolf', '10', '3', '2', '50']}

print(gap_calculator(positions, 'Buf', 'Rob'))
