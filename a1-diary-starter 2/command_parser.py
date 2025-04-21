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
    Checks if the path exists, and prints ERROR message according to the command
    """
    handled_path_name = Path(path_name)
    parsed_handled_path_name = shlex.split(path_name)
    if command == "C":
        if not os.path.exists(handled_path_name):
            print("ERROR")
            return False
    elif command == "D":
        if not parsed_handled_path_name[-1].endswith(".json"):
            print("ERROR")
            return False
        elif not os.path.exists(handled_path_name):
            print("ERROR")
            return False
    elif command == "O":
        if not parsed_handled_path_name[-1].endswith(".json"):
            print("ERROR")
            return False
        elif not os.path.exists(handled_path_name):
            print("ERROR")
            return False
    return True

# C "/home/john/ics 32/my notebooks" -n my_diary
def command_handler(user_command_input):
    parsed_input = (shlex.split(user_command_input))
    command = parsed_input[0]
    specified_path = parsed_input[1]
    flag_c_o = False

    while True:
        if command == "E" or command == "P":  # illegal if E or P is used before anything else
            if not flag_c_o:
                print("ERROR")
                break
            else:
                command_e_and_p(command)

        elif command == "C" and parsed_input[2] == "-n":
            flag_c_o = True
            diary_name = parsed_input[3]
            new_diary_path = specified_path + "/" + diary_name + ".json"
            p = Path(new_diary_path)
            if p.exists():  # if the file name already exists in the directory
                print("ERROR")  # prints error message
                break
            if not path_validity_checker("C", specified_path):
                break
            else:
                username = input("")
                password = input("")
                bio = input("")
                # Create a new Notebook object with user input info
                new_notebook_obj = Notebook(username, password, bio)
                new_notebook_obj.save(p)
                print(f"{p} CREATED")
                break
        elif command == "D":
            if not path_validity_checker("D", specified_path):
                break
            else:
                if os.path.exists(specified_path):
                    os.remove(specified_path)
                    print(f"{specified_path} DELETED")
                break
        elif command == "O":
            if not path_validity_checker("O", specified_path):
                break
            else:
                # don't need Path() bc the .load() does it for us
                username = input("")
                password = input("")
                bio = ""  # empty string placeholder
                new_notebook = Notebook(username, password, bio)
                new_notebook.load(specified_path)
                if username != new_notebook.username or password != new_notebook.password:
                    print("ERROR")
                else:
                    print("Notebook loaded.")
                    print(new_notebook.username)
                    print(new_notebook.bio)
                break
    return False

def command_e_and_p(command_e_or_p):  # use this in the C and O commands
    options_list = ["-usr", "-pwd", "-bio", "-add", "-del", "-diaries", "-diary [ID]", "-all"]
    e_options = options_list[:5]
    p_options = options_list[5:8]
    user_input_e_or_p = input("")
    split_input_e_and_p = user_input_e_or_p.split()
    # E command:
    if command_e_or_p == "E":
        user_input_e_option_list = []
        for inputs in split_input_e_and_p:
            if inputs in e_options:
                user_input_e_option_list.append(inputs)














