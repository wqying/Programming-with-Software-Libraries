# lab8v2.py

# Starter code for lab 8 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME
# EMAIL
# STUDENT ID


from abc import ABC, abstractmethod
import random

class Appetite:
    LOW = 3
    MEDIUM = 4
    HIGH = 5

class Dog(ABC):
    def __init__(self, name, age, appetite):
        self._name = name
        self._age = age
        self.appetite = appetite
        self.hunger_clock = 0  # initialize to 0

    @abstractmethod
    # means that all child classes must override this method
    # in their own definition
    def breed(self):
        pass

    def name(self):
        return self._name

    def age(self):
        return self._age

    def hungry(self):
        """
        The hungry method will check the hungry clock to see if some time has
        passed since the last feeding. If clock is greater than breed typical
        appetite, hunger assessment is randomly selected,
        otherwise hunger clock increases
        """
        if self.hunger_clock > self.appetite:
            return bool(random.getrandbits(1))
        else:
            self.hunger_clock += 1
            return False

    def feed(self):
        """
        Feeds the dog. Hunger clock is reset
        """
        self.hunger_clock = 0

class GermanShepherd(Dog):
    def __init__(self, name, age):
        super().__init__(name, age, Appetite.HIGH)

    def breed(self):
        return "German Shepherd"

class Husky(Dog):
    def __init__(self, name, age):
        super().__init__(name, age, Appetite.MEDIUM)

    def breed(self):
        return "Husky"

class Poodle(Dog):
    def __init__(self, name, age):
        super().__init__(name, age, Appetite.LOW)

    def breed(self):
        return "Poodle"


if __name__ == "__main__":
    while True:
        try:
            user_dog_breed = int(input("Choose a dog breed (enter integers): \n"
                                       "1. German Shepherd\n"
                                       "2. Husky\n"
                                       "3. Poodle\n"))
            user_dog_name = input("Name your dog: ")
            user_dog_age = int(input("How old is your dog: "))
            if user_dog_breed == 1:
                dog = GermanShepherd(user_dog_name, user_dog_age)
                break
            elif user_dog_breed == 2:
                dog = Husky(user_dog_name, user_dog_age)
                break
            elif user_dog_breed == 3:
                dog = Poodle(user_dog_name, user_dog_age)
                break
            else:
                print("Please enter a valid dog breed integer.")
        except ValueError:
            print("Enter only integers.")


    q_flag = False
    h_text = ""
    while not q_flag:
        h_text = "" if dog.hungry() else "not "
        print(f"Your {dog.breed()}, {dog.name()} is {h_text}hungry.")
        feed = input(f"Would you like to feed {dog.name()}? (y/n/q): ")

        if feed == "y":
            dog.feed()
        elif feed == "q":
            q_flag = True
