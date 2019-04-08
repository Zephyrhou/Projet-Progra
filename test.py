classes = {'barbarian': {'energise': [[1, 1, 1], [2, 1, 1], [3, 2, 1], [4, 2, 1]],
                         'stun': [[1, 1, 1], [2, 2, 2], [3, 3, 1]]},
           'healer': {'invigorate': [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]],
                      'immunise': [[1, 0, 1], [2, 0, 3], [3, 0, 3]]},
           'mage': {'fulgura': [[1, 3, 1], [2, 3, 1], [3, 4, 1], [4, 4, 1]],
                    'ovibus': [[1, 1, 3], [2, 2, 3], [3, 2, 3]]},
           'rogue': {'reach': [[1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1]],
                     'brust': [[1, 1, 1], [2, 2, 1], [3, 3, 1]]}}

player = {'Baz': 'barbarian', 'Lee': 'healer', 'May': 'mage', 'Rob': 'rogue'}

players_positions = {'spawn_player_1': ('20', '3'), 'spawn_player_2': ('20', '38'), 'Baz': ('20', '3'),
                     'Lee': ('20', '3'), 'May': ('20', '3'), 'Rob': ('20', '3'), 'Buf': ('20', '38'),
                     'Lia': ('20', '38'), 'Mey': ('20', '38'), 'Tob': ('20', '38')}

# positions = {('20', '3'): 'spawn_player_1', ('20', '37'): 'spawn_player_2', 'Baz': ('10', '3'), 'Lee': ('24', '3'),
#              'May': ('14', '6'), 'Rob': ('20', '17'), 'Buf': ('20', '17'), 'Lia': ('19', '7'), 'Mey': ('3', '3'),
#              'Tob': ('2', '37'), ('20', '38'): 'spur', ('20', '39'): 'spur', ('21', '38'): 'spur',
#              ('21', '39'): 'spur', ('10', '10'): ['bear', '20', '5', '3', '100'],
#              ('10', '20'): ['bear', '20', '5', '3', '100'], ('15', '10'): ['wolf', '10', '3', '2', '50']}

creatures = ['bear', 'bear', 'wolf']

lecture = ['map', '39', '40', '25', 'spawn', '20', '3', '20', '38', 'spur', '20', '38', '20', '39', '21', '38', '21',
           '39', 'creatures', 'bear', '10', '10', '20', '5', '3', '100', 'bear', '10', '20', '20', '5', '3', '100',
           'wolf', '15', '10', '10', '3', '2', '50']

level = {'barbarian': [[2, 100, 13, 3], [3, 200, 16, 4], [4, 400, 19, 5], [5, 800, 22, 6]],
         'healer': [[2, 100, 11, 2], [3, 200, 12, 3], [4, 400, 13, 3], [5, 800, 14, 4]],
         'mage': [[2, 100, 12, 3], [3, 200, 14, 4], [4, 400, 16, 5], [5, 800, 18, 6]],
         'rogue': [[2, 100, 12, 3], [3, 200, 14, 4], [4, 400, 16, 5], [5, 800, 18, 6]]}

player1 = {'Baz': {'class': 'barbarian', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Lee': {'class': 'healer', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'May': {'class': 'mage', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2},
           'Rob': {'class': 'rogue', 'level': 1, 'life_points': 10, 'victory_points': 0, 'damage_points': 2}}

# Baz:barbarian Lee:healer May:mage Rob:rogue
# Buf:barbarian Lia:rogue Mey:mage Tob:rogue

