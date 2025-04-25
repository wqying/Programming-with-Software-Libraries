# Main entry point of the program


from ui import print_grid


# def run_game():
#     rows = input("")
#     cols = input("")
#     return rows, cols






if __name__ == "__main__":
    rows = input("")
    cols = input("")
    game_type = input("")  # EMPTY or CONTENTS
    print_grid(rows, cols)
