# This module handles the game logic of Dr Mario

def is_level_cleared(game_object):
    """
    if game_object returns False level is cleared
    """
    if game_object:  # is False
        print("LEVEL CLEARED")
    else:
        pass


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


# Supported commands
def blank_line_command():
    """
    this command represents passage of time in the game.
    if there is a faller currently on the field, it falls down one cell
    if there is a faller that has landed, it freezes
    if there are capsule cells with empty cells below, gravity is applied one cell at a time
    """
    pass

def F_command():
    """
    example: F R Y (creates a faller with a red left segment and a yellow right segment.
    """
    pass