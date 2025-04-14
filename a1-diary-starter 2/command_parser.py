# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME: Luna Snow
# EMAIL: lsdagoat@uci.edu
# STUDENT ID: 123456789

import shlex
from pathlib import Path
from notebook import Notebook, NotebookFileError, IncorrectNotebookError
import os


def path_validity_checker(command, path_name):
    """
    Checks if the path exists, and prints messages according to the command
    """
    handled_path_name = Path(path_name)
    if command == "C":
        if not os.path.exists(handled_path_name):
            print("ERROR")
    return False

# C "/home/john/ics 32/my notebooks" -n my_diary
def command_handler(user_command_input):
    parsed_input = (shlex.split(user_command_input))
    command = parsed_input[0]
    specified_path = parsed_input[1]
    # if len(parsed_input) > 2:
    #     option = parsed_input[2]
    #     diary_name = parsed_input[3]
    #     new_diary_path = specified_path + "/" + diary_name + ".json"
    #     p = Path(new_diary_path)

    while True:
        if command == "C" and parsed_input[2] == "-n":
            diary_name = parsed_input[3]
            new_diary_path = specified_path + "/" + diary_name + ".json"
            p = Path(new_diary_path)
            if p.exists():  # if the file name already exists in the directory
                print("ERROR")
                break
            path_validity_checker("C", specified_path)
            username = input("")
            password = input("")
            bio = input("")
            # Create a new Notebook object with user input info
            new_notebook_obj = Notebook(username, password, bio)
            new_notebook_obj.save(p)
            print(f"{p} CREATED")
            break
        elif command == "D":
            if os.path.exists(specified_path):
                os.remove(specified_path)
                print(f"{specified_path} DELETED")
            else:
                print("ERROR")
            break
        # elif command == "O":


    return False











