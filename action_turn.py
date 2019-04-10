from heroes_namur_gr_06 import *


# Sub-function of players_choice determining the order of attacks /movements of the creatures / heroes
def actions_turn(positions, player1, player2, creatures):
    """Determines the order of attacks / moves following the choices of both player and the creatures' ones.

    Parameters:
    -----------
    positions: Contains all the coordinates of the board (dict)
    player1: All the data about the heroes of the first player (dict)
    player2: All the data about the heroes of the second player (dict)
    creatures: Contains all the data about creatures (dict)

    Returns:
    --------
    player1: All the data about the heroes of the first player (dict)
    player2: All the data about the heroes of the second player (dict)
    creatures: Contains all the data about creatures (dict)
    positions: Contains all the coordinates of the board (dict)
    """

    attacking = []
    moving = []

    # Split the orders within attacks and movements
    for character in positions:
        if character in creatures:
            if positions[character]['order'] == 'attack':
                attacking += character
            else:
                moving += character
        elif character in player1:
            if positions[character]['order'] == 'attack':
                attacking += character
            else:
                moving += character

        else:
            if positions[character]['order'] == 'attack':
                attacking += character
            else:
                moving += character

    # Execute the attacks
    for character in attacking:
        # First attacking : the creatures
        if character in creatures:
            hero_name = character
            name_attack = positions[character]['name_attack']
            attack_coord = positions[character]['where']
            attack(positions, hero_name, name_attack, (0, 0), attack_coord, player1, player2, creatures)
        # Then the heroes of the first player
        elif character in player1:
            hero_name = character
            name_attack = positions[character]['name_attack']
            attack_coord = positions[character]['where']
            attack(positions, hero_name, name_attack, (0, 0), attack_coord, player1, player2, creatures)
        # Finally the ones of the second player
        else:
            hero_name = character
            name_attack = positions[character]['name_attack']
            attack_coord = positions[character]['where']
            attack(positions, hero_name, name_attack, (0, 0), attack_coord, player1, player2, creatures)

    for character in moving:
        print(character, moving)
        # First moving : the creatures
        if character in creatures:
            hero_name = character
            movement_coord = positions[character]['where']
            move(hero_name, positions, movement_coord)

        # Then the heroes of the first player
        elif character in player1:
            hero_name = character
            movement_coord = positions[character]['where']
            move(hero_name, positions, movement_coord)

        # Finally the ones of the second player
        else:
            hero_name = character
            movement_coord = positions[character]['where']
            move(hero_name, positions, movement_coord)

    return player1, player2, positions, creatures


choice1 = 'Baz:@21-3 Lee:@20-4 May:@10-10 Rob:@21-3'
choice2 = 'Buf:@20-36 Lia:@21-37 Mey:@20-38 Tob:@21-36'
choice_creature = 'arrack:@30-31 wolf:@30-21 fox:*10-15'

print(actions_turn(positions, player1, player2, creatures))
