# lib/helpers.py
from models.Animal import Animal
from models.AnimalFood import AnimalFood
from models.Food import Food

# Delete row of Animal table by name attribute
def delete_animal():
    name = input("Enter the name of the animal to delete: ")
    animal = Animal.find_by_name(name)
    id = animal.id

    ids = animal.animal_foods_ids()
    print(AnimalFood.all)
    for id in ids:
        del AnimalFood.all[id]
        animal.delete_animal_foods(id)

    animal.delete(id)
    print(f"{name} deleted from the database")
    print(AnimalFood.all)

# Create an animal instance and store it in 'animals' table when given a name
def create_animal():
    """ """
    name = input("Enter animal name: ")
    # Input validation: Ensure the name is not empty.
    if not name and not isinstance(name, str):
        print("Animal name cannot be empty and must be a string.")
        return
    animal = Animal.create(name.lower().strip())
    print(f"Animal '{animal.name}' created.")

def exit_program():
    print("Goodbye!")
    exit()

# Get all names from 'foods' table
def list_foods():
    foods = Food.get_all_food()
    for food in foods:
        print(food.name)
    
# Get all names from 'animals' table
def list_animals():
    animals = Animal.get_all_animal()
    for animal in animals:
        print(animal.name)

def update_animal_name():
    current_name = input("Type the animal whose name you wish to change: ")
    animal = Animal.find_by_name(current_name)
    if not animal:
        print(f"Animal '{current_name}' not found")
        return
    new_name = input("Type the new name you wish to save: ")
    animal.update(new_name)
    print(f"The name of animal '{current_name} has been updated to '{new_name}")