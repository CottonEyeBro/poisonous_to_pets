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

def unsafe_foods_for_animal():
    #ask for a species
    animal_name = input("Which animal would you like to check: ")
    # print(animal_name)

    #get the id of the species from animal table
    animal = Animal.find_by_name(animal_name)
    print(animal)
    if not animal:
        print(f"Animal '{current_name}' not found")
        return
    
    #get all animal_foods ids for that animal
    all_ids = animal.animal_foods_ids() #returns a list of ids
    # print(all_ids)

    #get all fk_foods ids where isSafe == false
    unsafe = []
    for id in all_ids:
        animal_food = AnimalFood.find_unsafe_by_id(id)
        if animal_food != None:
            unsafe.append(animal_food)
    # print(unsafe)

    #iterate through AnimalFood objects and return a list of their fk_food values
    fk_food_values = []
    for af_object in unsafe:
        fk = af_object.fk_food
        fk_food_values.append(fk)
    # print(fk_food_values)

    #iterate over list to return foods table names for each id
    food_names = []
    for id in fk_food_values:
        food_obj = Food.find_by_id(id)
        name = food_obj.name
        food_names.append(name)
    # print(food_names)

    #alphabetize the names
    sorted_names = sorted(food_names)

    #print the names
    print(f"Unsafe Foods for '{animal_name}:")
    for name in sorted_names:
        print(name)