# This module handles the user interface of the game





def print_grid(rows, cols, config):
    if config == "EMPTY":
        for _ in range(rows):
            cell = 3 * cols  # a cell is 3 blanks
            blanks = " " * cell
            print("|" + blanks + "|")
        floor = "_" * (3 * cols)
        print(" " + floor + " ")
    elif config == "CONTENTS":
        pass

#EMPTY: start game with empty field
#CONTENTS: start game with specific field config

