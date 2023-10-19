# lib/helpers.py
from models.Animal import Animal
from models.AnimalFood import AnimalFood
from models.Food import Food




def exit_program():
    print("You have now exited the program")
    print("---------- Goodbye! ----------\n\n")
    exit()


# Create an animal instance and store it in 'animals' table when given a name
# def create_animal():
#     name = input("Enter animal name: ").lower()
#     # Input validation: Ensure the name is not empty.
#     if not name or not isinstance(name, str):
#         print("--------------------------------------------------\n <!> Animal name cannot be empty and must be a string. <!> \n--------------------------------------------------")
#         return
#     animal = Animal.create(name.lower().strip())
#     print(f"-----------------------------------------------------\nAnimal '{animal.name}' created and added to Database.\n-----------------------------------------------------")



# def create_animal():
#     name = input("Enter animal name: ").strip().lower()
#     # Input validation: make sure the name typed in is not empty.
#     if not name:
#         return  
#     # confirmation
#     confirmation = input(f"---------------------------------------------------------------------\nAre you sure you want to add '{name.capitalize()}' to the database? (yes/no):\n---------------------------------------------------------------------\nResponse: ").strip().lower()

#     if confirmation == "yes":
#         animal = Animal.create(name)
#         print(f"---------------------------------------------------\nAnimal '{animal.name.capitalize()}' created and added to the Database.\n---------------------------------------------------")
#     else:
#         print(f"-----------------------------\n <!> Add '{name.capitalize()}' was canceled. <!> \n-----------------------------")


def create_animal():
    name = input("Enter animal name: ").strip().lower()
    # Input validation: make damn sure the name is not empty.
    if not name:
        return
    
    if name == "cooper":
        print(f"------------------------------------------------------------\n <!> CATUION <!> \n------------------------------------------------------------ \n We do not allow 'Coopers' \n------------------------------------------------------------ \n'Cooper' cannot be added to the database. Creation canceled.\n------------------------------------------------------------")
        return
    # Fetch the list of existing animals
    existing_animals = [animal.name.lower() for animal in Animal.get_all_animal()]
    if name in existing_animals:
        print(f"------------------------------------------------------------\nAnimal '{name.capitalize()}' already exists in the database. Creation canceled.\n------------------------------------------------------------")
        return

    # confirmation
    confirmation = input(f"---------------------------------------------------------------------\nAre you sure you want to add '{name.capitalize()}' to the database? (yes/no):\n---------------------------------------------------------------------\nResponse: ").strip().lower()
    if confirmation == "yes":
        animal = Animal.create(name)
        print(f"---------------------------------------------------\nAnimal '{animal.name.capitalize()}' created and added to the Database.\n---------------------------------------------------")
    else:
        print(f"-----------------------------\n <!> Add '{name.capitalize()}' was canceled. <!> \n-----------------------------")




# --------old code--------- vvvv

# Delete row of Animal table by name attribute
# def delete_animal():
#     name = input("Enter the name of the animal to delete: ")
#     animal = Animal.find_by_name(name)
#     id = animal.id

#     ids = animal.animal_foods_ids()
#     print(AnimalFood.all)
#     for id in ids:
#         del AnimalFood.all[id]
#         animal.delete_animal_foods(id)

#     animal.delete(id)
#     print(f"{name} deleted from the database")
#     print(AnimalFood.all)





# vvvvvvvvv delete animal code block vvvvvv

def delete_animal():
    name = input("-----------------------------------------\nEnter the name of the animal to delete: ").lower()
    animal = Animal.find_by_name(name)
    if not animal:
        print(f" <!> Animal '{name}' not found <!> ")
        return

    if name.lower() == "dog":
        # Ask for double confirmation
        confirmation = input(f"----------------------------------------------------------------------------------------------------\nAre you sure you want to delete '{name}' and be known as the 'Dog Deleter'??? Type 'yes' to confirm: \n----------------------------------------------------------------------------------------------------\nResponse: ").strip().lower()
        if confirmation == "yes":
            second_confirmation = input(f"----------------------------------------------------------------------------------------------------\nWooooooooow, I see what kind of person you are... so you really want to delete '{name}'? Type 'yes' to confirm your savagery: \n----------------------------------------------------------------------------------------------------\nResponse: ").strip().lower()
            if second_confirmation == "yes":
                
                # Proceed with dog deletion
                id = animal.id
                ids = animal.animal_foods_ids()

                for id in ids:
                    del AnimalFood.all[id]
                    animal.delete_animal_foods(id)

                animal.delete(id)
                print(f"----------------------------------------\nThe sweet sweet'{name}' was deleted from the database, I hope you're happy you sick twisted monster\n----------------------------------------")
                # print(AnimalFood.all)
            else:
                print(f"-----------------------------------------------------------------------\nI freakin thought so you sick son of a sideways salamander.... Deletion of the adorable '{name}' was canceled.\n-----------------------------------------------------------------------")
        else:
            print("-------------------------\n <!> Deletion canceled. <!> \n-------------------------")
    else:
        # Ask for regular confirmation
        confirmation = input(f"----------------------------------------\nAre you sure you want to delete '{name}'? (yes/no): \n----------------------------------------\nResponse: ").strip().lower()

        if confirmation == "yes":
            id = animal.id
            ids = animal.animal_foods_ids()

            # Regular delete
            for id in ids:
                del AnimalFood.all[id]
                animal.delete_animal_foods(id)
            animal.delete(id)
            print(f"------------------------------------\n <!> '{name}' deleted from the database <!> \n------------------------------------")
            # print(AnimalFood.all)
        elif confirmation == "no":
            print(f"------------------------------------\n<!> Deletion of '{name}' canceled. <!>\n------------------------------------")
        else:
            print("--------------------------------------------\n<!> Invalid input. Please enter 'yes' or 'no' for confirmation. <!>\n--------------------------------------------")




# Get all names from 'foods' table
def list_foods():
    print("--------------\nFood List:\n--------------")
    foods = Food.get_all_food()

    
    food_name = [food.name for food in foods]
    sorted_food_names = sorted(food_name)

    for food in sorted_food_names:
        print(f"- {food}")
    print(" ")



# Get all names from 'animals' table
# def list_animals():
#     print("Species List:\n")
#     animals = Animal.get_all_animal()
#     for animal in animals:
#         print(f'{animal.name}')
#     print(" ")

def list_animals():
    print("--------------\nSpecies List:\n--------------")
    animals = Animal.get_all_animal()

    # Extracted animal names and sorted them within the list_animals function
    animal_names = [animal.name for animal in animals]
    sorted_animal_names = sorted(animal_names)

    for name in sorted_animal_names:
        print(f"- {name}")
    print(" ")





# def update_animal_name():
#     current_name = input("Type the animal whose name you wish to change: ")
#     animal = Animal.find_by_name(current_name)
#     if not animal:
#         print(f"Animal '{current_name}' not found")
#         return
#     new_name = input("Type the new name you wish to save: ")
#     animal.update(new_name)
#     print(f"The name of animal '{current_name} has been updated to '{new_name}")

def update_animal_name():
    current_name = input("----------------------------------------------------\nType the animal whose name you wish to change: ")
    animal = Animal.find_by_name(current_name)
    if not animal:
        print(f"----------------------------\n <!> Animal '{current_name}' not found <!> \n----------------------------")
        return
    new_name = input(f"-------------------------------------------\nWhat would you like to switch '{current_name}' to: ")
    
    while True:
        confirmation = input(f"-----------------------------------------\nDo you want to update '{current_name}' to '{new_name}'? (yes/no)\n-----------------------------------------\nResponse: ").strip().lower()
        if confirmation == "yes":
            animal.update(new_name)
            print(f"--------------------------------------------------\nThe name of animal '{current_name}' has been updated to '{new_name}'\n--------------------------------------------------")
            break
        elif confirmation == "no":
            print(f"------------------------------------\n <!> Update '{current_name}' name canceled. <!> \n------------------------------------\n\n")
            break
        else:
            print("------------------------------------\n!!!>>>>  Please Confirm (yes/no).  <<<<!!!")