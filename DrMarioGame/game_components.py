# This module handles the game components

# Field: grid of cells, each cell is occupied by one half of a vitamin capsule
# or a virus, or an empty space

class Capsule:
    def vitamin(self):
        pass

    def virus(self):
        pass



# Vitamin Capsule:
# two connected halve (cells) possessing red yellow or blue
# can be one or two color
# can be horizontal or vertical
# [ R ]

# Virus:
# can be red yellow or blue
# single cell

# Faller:
# the vitamin capsule that is currently descending downward
# can rotate clockwise or counterclockwise