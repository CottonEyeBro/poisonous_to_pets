# lib/helpers.py
from models.Animal import Animal
from models.AnimalFood import AnimalFood
print(AnimalFood.all)

def helper_1():
    print("Performing useful function#1.")

# Delete function for Animal table by name attribute
def delete_animal():
    name = input("Enter the name of the animal to delete: ")
    animal = Animal.find_by_name(name)
    id = animal.id

    ids = animal.animal_foods_ids()
    print(AnimalFood.all)
    for id in ids:
        # del AnimalFood.all[id]
        animal.delete_animal_foods(id)

    animal.delete(id)
    print(f"{name} deleted from the animal database")

def exit_program():
    print("Goodbye!")
    exit()