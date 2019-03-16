import os


def boardfilecreation():
    """ create the file for the game.
    """

    b_file = open('board_file','a')
    line = 'map: \n 30 30 25 \n spawn: \n 25 6 \n 12 8 \n spur: \n 1 25 \n 1 26 \n 2 25 \n 2 26 \n'
    line += 'creatures: \n lion 2 27 20 7 7 150 \n bear 2 28 17 9 4 200 \n'
    b_file.write(line)
    b_file.close()
