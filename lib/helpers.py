# lib/helpers.py
from models.Animal import Animal

def helper_1():
    print("Performing useful function#1.")

# Delete function for Animal table by name attribute
def delete_animal():
    name = input("Enter the name of the animal to delete: ")
    animal = Animal.find_by_name(name)
    id = animal.id

    animal.delete(id)
    print(f"{name} deleted from the animal database")
    #need to delete dog related items from the animals_food database 

def exit_program():
    print("Goodbye!")
    exit()