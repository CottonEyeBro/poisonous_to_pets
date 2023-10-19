# lib/helpers.py
from models.Animal import Animal
from models.AnimalFood import AnimalFood
from models.Food import Food
from figures import web_m_dumper

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

# WebMD results
def web_md():
    response = input("Are you sure that you would like to check WebMD? [yes/no]")
    if response == "yes":
        print("BeeYoop BeeDeepBoom Weeop DEEpaEEya... It's probably cancer.\n")
        return web_m_dumper()
    else:
        return

def exit_program():
    print("Goodbye!")
    exit()