list_attack = {"energise", "stun", "invigorate", "immunise", "fulgura", "ovibus", "reach", "burst"}

# The class of the heroes in the dictionary is called "job" because class is already a part of the words in python !
# Dict of special attacks following their "job"

dict_job = {"barbarian": ['energise', 'stun'], "healer": ['invigorate', 'immunise'],
            "mage": ['fulgura', 'ovibus'], "rogue": ['reach', 'burst']}

# Dict of the first player (our future I.A.)
# At the start of the game (first turn after their creation with create_heroes())
# Basically the second player one is the same except for the heroes' names (which must be unique)
# And also their job that may vary following the strategy of player 2.

IA_hero_names = ['Bernard', 'Heidy', 'Marguerite', 'Raymond']

player1 = {"Bernard": {"job": 'barbarian', "level": 1, "life_points": 10, "victory_points": 0, "damage_points": 2,
                       "cooldown": {"energise": 0, "stun": 0}},
           "Heidy": {"job": 'healer', "level": 1, "life_points": 10, "victory_points": 0, "damage_points": 2,
                     "cooldown": {"invigorate": 0, "immunise": 0}},
           "Marguerite": {"job": 'mage', "level": 1, "life_points": 10, "victory_points": 0, "damage_points": 2,
                          "cooldown": {"fulgura": 0, "ovibus": 0}},
           "Raymond": {"job": 'rogue', "level": 1, "life_points": 10, "victory_points": 0, "damage_points": 2,
                       "cooldown": {"reach": 0, "burst": 0}}}

# Dictionary used by invigorate
max_life_points = {"barbarian": {1: 10, 2: 13, 3: 16, 4: 19, 5: 22},
                   "healer": {1: 10, 2: 11, 3: 12, 4: 13, 5: 14},
                   "mage": {1: 10, 2: 12, 3: 14, 4: 16, 5: 18},
                   "rogue": {1: 10, 2: 12, 3: 14, 4: 16, 5: 18}}

# Must  be created in initialization because the number of creatures may vary !
# Dictionary of modifications of the players' heroes' d_points/h_points .
# Please note that the dictionary also represents the start of the game with the heroes of the future IA.

modif = {"Bernard": {"damage_points_modifs": 0, "life_points_modifs": 0, "immunised": 0},
         "Heidy": {"damage_points_modifs": 0, "life_points_modifs": 0, "immunised": 0},
         "Marguerite": {"damage_points_modifs": 0, "life_points_modifs": 0, "immunised": 0},
         "Raymond": {"damage_points_modifs": 0, "life_points_modifs": 0, "immunised": 0},
         "hero_1_player2": {"damage_points_modifs": 0, "life_points_modifs": 0, "immunised": 0},
         "hero_2_player2": {"damage_points_modifs": 0, "life_points_modifs": 0, "immunised": 0},
         "hero_3_player2": {"damage_points_modifs": 0, "life_points_modifs": 0, "immunised": 0},
         "hero_4_player2": {"damage_points_modifs": 0, "life_points_modifs": 0, "immunised": 0},
         "creature_name_1": {"damage_points_modif": 0, "life_points_modif": 0},
         "creature_name_2": {"damage_points_modif": 0, "life_points_modif": 0}}

# Dictionaryb used by player's choice, move, attack, ...

order = {"Hero_name1": {"order": "",  # move or attack (str)
                        "name_attack": "",  # "" = basic if basic attack (str)
                        "where": (0, 0)},
         "Hero_name2": {"order": "", "name_attack": "", "where": (0, 0)},
         "Hero_name3": {"order": "", "name_attack": "", "where": (0, 0)},
         "Hero_name4": {"order": "", "name_attack": "", "where": (0, 0)},
         "Hero_name5": {"order": "", "name_attack": "", "where": (0, 0)},
         "Hero_name6": {"order": "", "name_attack": "", "where": (0, 0)},
         "Hero_name7": {"order": "", "name_attack": "", "where": (0, 0)},
         "Hero_name8": {"order": "", "name_attack": "", "where": (0, 0)},
         "creature_name1": {"order": "", "name_attack": "", "where": (0, 0)},
         "creature_name2": {"order": "", "name_attack": "", "where" : (0, 0)}}

classes = {'barbarian': {'energise': [[1, 1, 1], [2, 1, 1], [3, 2, 1], [4, 2, 1]],
                         'stun': [[1, 1, 1], [2, 2, 2], [3, 3, 1]]},
           'healer': {'invigorate': [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]],
                      'immunise': [[1, 0, 1], [2, 0, 3], [3, 0, 3]]},
           'mage': {'fulgura': [[1, 3, 1], [2, 3, 1], [3, 4, 1], [4, 4, 1]],
                    'ovibus': [[1, 1, 3], [2, 2, 3], [3, 2, 3]]},
           'rogue': {'reach': [[1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1]],
                     'brust': [[1, 1, 1], [2, 2, 1], [3, 3, 1]]}}



