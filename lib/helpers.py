# lib/helpers.py
from models.Animal import Animal

def helper_1():
    print("Performing useful function#1.")

# Delete function for Animal table by name attribute
def delete_animal():
    db_file = 'safety.db'
    animal_name = int(input("Enter the name of the animal to delete: "))

    Animal.delete_animal(animal_name, db_file)


def exit_program():
    print("Goodbye!")
    exit()