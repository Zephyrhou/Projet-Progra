from gap import *


def move(positions, hero, movement):
    """Checks if the position he will end on is allowed. Do it if it is allowed.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    hero: Name of the hero who wants to move (str)
    movement: Coordinates the hero wants to go to (tuple)

    Returns:
    --------
    positions: Contains the updated coordinates of the board (dict)

    Notes:
    ------
    It isn't allowed to move if there is already a hero or a creatures where you want to move.
    If the movement can't be done an error message is displayed and the movement is ignored.
    Movement can only be of one step in one of the eight directions.

    Version:
    --------
    specification: Zephyr Houyoux (v.5 04/04/19)
    implementation: Zephyr Houyoux (v.3 4/04/19)
    """

    position_hero = positions[hero]
    # Computes the gap between the position of the hero and where he wants to go
    gap = gap_calculator(movement, position_hero)
    error_message = 'You can\'t move there'

    # If the position the hero wants to go to is the same as where he is
    if movement[0] == positions[hero][0] and movement[1] == positions[hero][1]:
        return error_message
    else:
        # If the gap is less than 1.5 he can move
        if gap < 1.5:
            positions[hero] = movement
            return positions
        else:
            return error_message


positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'), 'Lee': ('24', '3'),
             'May': ('14', '6'), 'Rob': ('20', '17'), 'Buf': ('20', '17'), 'Lia': ('19', '7'), 'Mey': ('3', '3'),
             'Tob': ('2', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
             ('21', '39'): 'spur', ('10', '10'): ['bear', '20', '5', '3', '100'],
             ('10', '20'): ['bear', '20', '5', '3', '100'], ('15', '10'): ['wolf', '10', '3', '2', '50']}

print(move(positions, 'Buf', ('20', '18')))
