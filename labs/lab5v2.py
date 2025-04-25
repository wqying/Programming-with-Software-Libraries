#lab5.py

# Starter code for lab 5 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# NAME
# EMAIL
# STUDENT ID

# ---------------------

# Write your Note class here
class Note:
    def __init__(self, path):
        self.path = path

    def read_notes(self):
        notes_list = []
        with open(self.path, "r") as pynote_file:
        # read each line of the file
            for line in pynote_file:
                notes_list.append(line)
        return notes_list

    def save_note(self, user_input_note_to_save:str):
        new_note = user_input_note_to_save
        with open("pynote.txt", "a") as write_note:
            write_note.write(new_note + "\n")

    def remove_note(self, user_input_remove_id: int):
        with open("pynote.txt", "r") as fp:
            lines = fp.readlines()  # always read first
        with open("pynote.txt", "w") as fp:
            for num, line in enumerate(lines):
                if num == user_input_remove_id:
                    content_to_remove = line
                if num != user_input_remove_id:
                    fp.write(line)  # write all lines except the id one
        return content_to_remove

# ---------------------
from pathlib import Path

NOTES_PATH = ".."
NOTES_FILE = "pynote.txt"

def print_notes(notes:list[str]):
    id = 0
    for n in notes:
        print(f"{id}: {n}")
        id+=1

def delete_note(note:Note):
    try:
        remove_id = input("Enter the number of the note you would like to remove: ")
        remove_note = note.remove_note(int(remove_id))
        print(f"The following note has been removed: \n\n {remove_note}")
    except FileNotFoundError:
        print("The PyNote.txt file no longer exists")
    except ValueError:
        print("The value you have entered is not a valid integer")

def run():
    p = Path(NOTES_PATH) / NOTES_FILE
    if not p.exists():
        p.touch()
    note = Note(p)
    
    print("Here are your notes: \n")
    print_notes(note.read_notes())

    user_input = input("Please enter a note (enter :d to delete a note or :q to exit):  ")

    if user_input == ":d":
        delete_note(note)
    elif user_input == ":q":
        return
    else:    
        note.save_note(user_input)
    run()


if __name__ == "__main__":
    print("Welcome to PyNote! \n")

    run()
