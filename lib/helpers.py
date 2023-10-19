# lib/helpers.py
from models.Animal import Animal
from models.AnimalFood import AnimalFood
from models.Food import Food
from figures import web_m_dumper







# --------------------------------------------------------------
# Below is the helper to EXIT THE PROGRAM ENTIRELY
# --------------------------------------------------------------


def exit_program():
    print("\n\nYou have now exited the program")
    print("---------- Goodbye! ----------\n\n")
    exit()










# --------------------------------------------------------------
# Below is the helper to CREAT A NEW ANIMAL
# --------------------------------------------------------------






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














# --------------------------------------------------------------
# Below is the helper to DELETE AN EXISTING ANIMAL
# --------------------------------------------------------------





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











# --------------------------------------------------------------
# Below is the helper to LIST ALL FOODS
# --------------------------------------------------------------



def list_foods():
    print("--------------\nFood List:\n--------------")
    foods = Food.get_all_food()

    
    food_name = [food.name for food in foods]
    sorted_food_names = sorted(food_name)

    for food in sorted_food_names:
        print(f"- {food}")
    print(" ")













# --------------------------------------------------------------
# Below is the helper to LIST ALL ANIMALS
# --------------------------------------------------------------

def list_animals():
    print("--------------\nSpecies List:\n--------------")
    animals = Animal.get_all_animal()

    # Extracted animal names and sorted them within the list_animals function
    animal_names = [animal.name for animal in animals]
    sorted_animal_names = sorted(animal_names)

    for name in sorted_animal_names:
        print(f"- {name}")
    print(" ")












# --------------------------------------------------------------
# Below is the helper to UPDATE EXISTING ANIMAL NAME
# --------------------------------------------------------------

def update_animal_name():
    current_name = input("----------------------------------------------------\nType the animal whose name you wish to change: ")
    animal = Animal.find_by_name(current_name)
    if not animal:
        print(f"----------------------------\n <!> Animal '{current_name}' not found <!> \n----------------------------")
        return
    while True:
        new_name = input(f"-------------------------------------------\nWhat would you like to switch '{current_name}' to: ")
        # Checks if new_name is an empty string
        if not new_name.strip():  
            print("----------------------------------------------------\n!!!>>>>  Please provide a non-empty name.  <<<<!!!")
        else:
            break
    
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










# ------------------------------------------------------------------
# Below is the helper to LIST ALL UNSAFE FOODS FOR A SPECIFIC ANIMAL
# ------------------------------------------------------------------







def unsafe_foods_for_animal():
    #ask for a species
    animal_name = input("\n\nWhich animal would you like to check: ")
    # print(animal_name)

    #get the id of the species from animal table
    animal = Animal.find_by_name(animal_name)
    # print(animal)
    if not animal:
        print(f"Animal '{animal_name}' not found")
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
    print(f"\n------------------------\nUnsafe Foods for '{animal_name}':\n------------------------")
    for name in sorted_names:
        print(f"- {name}")









# --------------------------------------------------------------
# Below is the helper to SHOW WEBMD RESULTS
# --------------------------------------------------------------


# WebMD results
def web_md():
    response = input("Are you sure that you would like to check WebMD? [yes/no]")
    if response == "yes":
        print("BeeYoop BeeDeepBoom Weeop DEEpaEEya... It's probably cancer.\n")
        return web_m_dumper()
    else:
        return
