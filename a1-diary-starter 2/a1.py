# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME: Luna Snow
# EMAIL: lsdagoat@uci.edu
# STUDENT ID: 123456789
# test


from command_parser import command_handler

# if command E is issued before any C or O is issued, program should print ERROR


if __name__ == "__main__":
    while True:
        user_command = input("")
        if user_command == "Q":
            break
        command_handler(user_command)

