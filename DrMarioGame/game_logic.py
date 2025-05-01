# This module handles the game logic of Dr Mario

def is_level_cleared(game_object):
    """
    if game_object returns False level is cleared
    """
    if game_object:  # is False
        print("LEVEL CLEARED")
    else:
        pass

# Supported commands


class CurrentState:
    # a method to get the number of rows/columns in your field
    # a method to create a faller
    # a methods to rotate a faller
    # a method to determine if the field contains any viruses
    def __init__(self):
        self.virus = None

    def is_virus(self):
        """
        determines if the field contains any viruses
        """
        return self.virus
