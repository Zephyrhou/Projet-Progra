from heroes_namur_gr_06 import *


def infighting():
    """

    :return:
    """


def stun_available():
    """

    :return:
    """


def ally_nearby():
    """

    :return:
    """


def enemy_nearby():
    """

    :return:
    """


def spur_available():
    """

    :return:
    """


def ovibus_available():
    """

    :return:
    """


def fulgura_available():
    """

    :return:
    """


def reach_available():
    """

    :return:
    """


def burst_available():
    """

    :return:
    """


def get_IA_orders(positions, player1, player2):
    """Decides what each hero will do.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    player1: Level, number of point, etc. of the heroes of player 1 (dict)
    player2: Level, number of point, etc. of the heroes of player 2 (dict)

    Returns:
    --------
    choice: Orders for each hero (str)

    Version:
    --------
    specification: Aude Lekeux (v.1 25/04/2019)
    implementation: Aude Lekeux (v.1 25/04/2019)
    """

    # Choice of the IA built as you go
    choice = ''

    # Check what class is every item
    for hero in positions:
        if hero in player1:
            hero_class = player1[hero]['class']
            choice += str(hero)
        elif hero in player2:
            hero_class = player2[hero]['class']
            choice += str(hero)

        # Depending on the class of the hero
        # If hero is a barbarian
        if hero_class == 'barbarian':
            if infighting():
                if stun_available():
                    choice += ':stun '
                elif ally_nearby():
                    choice += ':enerigse '
                else:
                    choice += ':*'
            else:
                if spur_available():
                    if is_on_spur():
                        # Do nothing
                        choice += ':@'
                    else:
                        # Move towards spur
                        choice += ':@'
                else:
                    # Move towards enemy
                    choice += ':@'

        # If hero is a healer
        elif hero_class == 'healer':
            if ally_nearby():
                if enemy_nearby():
                    choice += ':immunise '
                else:
                    choice += ':invigorate '
            elif enemy_nearby():
                choice += ':*'
            else:
                if spur_available():
                    if is_on_spur():
                        # Do nothing
                        choice += ':@'
                    else:
                        # Move towards spur
                        choice += ':@'
                else:
                    # Move towards enemy
                    choice += ':@'

        # If hero is a mage
        elif hero_class == 'mage':
            if ovibus_available():
                if enemy_nearby():
                    choice += ':ovibus '
            elif fulgura_available():
                if enemy_nearby():
                    choice += ':fulgura '
                elif infighting():
                    choice += ':*'
                elif spur_available():
                    if is_on_spur():
                        # Do nothing
                        choice += ':@'
                    else:
                        # Move towards spur
                        choice += ':@'
                else:
                    # Move towards enemy
                    choice += ':@'

        # If hero is a rogue
        elif hero_class == 'rogue':
            if burst_available():
                if enemy_nearby():
                    choice += ':burst '
            elif infighting():
                choice += ':*'
            else:
                if spur_available():
                    if is_on_spur():
                        # Do nothing
                        choice += ':@'
                    else:
                        # Move towards spur
                        choice += ':@'
                else:
                    if reach_available():
                        choice += ':reach '
