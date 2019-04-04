def gap_calculator(position_1, position_2):
    """Computes the gap between two characters.

    Parameter:
    -----------
    position_1: Position of the first character (tuple)
    position_2: Position of the second character (tuple)

    Returns:
    -------
    gap: Gap between two characters (int)

    Version:
    --------
    specification: Manon Michaux (v.3 04/04/19)
    implementation: Zéphyr Houyoux (v.3 04/04/19)
    """

    pos1c = int(position_1[0])
    pos1r = int(position_1[1])
    pos2c = int(position_2[0])
    pos2r = int(position_2[1])

    gap = ((pos1r - pos2r) ** 2 + (pos1c - pos2c) ** 2) ** 0.5

    return gap


positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'), 'Lee': ('24', '3'),
             'May': ('14', '6'), 'Rob': ('20', '17'), 'Buf': ('20', '16'), 'Lia': ('19', '7'), 'Mey': ('3', '3'),
             'Tob': ('2', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ['bear', '20', '5', '3', '100'],
             ('10', '20'): ['bear', '20', '5', '3', '100'], ('15', '10'): ['wolf', '10', '3', '2', '50']}

# print(gap_calculator(('20', '16'), ('20', '17')))
