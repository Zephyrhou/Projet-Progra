from heroes_namur_gr_06 import *


def game(player_1, player_2):
    """Starts a new turn if the game is not finished.

    Returns:
    --------
    nb_turns_wanted: Number of turns needed to be on the spur in order to win (int)
    nb_turns1: Number of turns a hero of player1 stands on the spur (int)
    nb_turns2: Number of turns a hero of player2 stands on the spur (int)
    inactivity: Number of turns no activity has been observed (int)

    Version:
    --------
    specification: Zephyr Houyoux (v.4 02/04/19)
    implementation:
    """

    while not is_game_over():
        is_game_over()

    return nb_turns_wanted, nb_turns1, nb_turns2, inactivity_time