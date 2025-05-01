# Main entry point of the program


from ui import print_grid
from game_logic import CurrentState, is_level_cleared


# def run_game():
#     rows = input("")
#     cols = input("")
#     return rows, cols






if __name__ == "__main__":
    # shell program start
    rows = int(input(""))
    cols = int(input(""))
    game_type = str(input(""))  # EMPTY or CONTENTS
    print_grid(rows, cols, game_type)
    game_start = CurrentState()
    is_level_cleared(game_start)

