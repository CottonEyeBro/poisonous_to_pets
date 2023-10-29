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
    name = input("Enter New animal name: ").strip().lower()
    # Here I make darn sure the name is not empty
    if not name:
        return
    
    if name == "cooper":
        print(f"------------------------------------------------------------\n <!> CATUION <!> \n------------------------------------------------------------ \n We do not allow 'Coopers' \n------------------------------------------------------------ \n'Cooper' cannot be added to the database. Creation canceled.\n------------------------------------------------------------")
        return

    # here I Fetch the list of existing animals
    existing_animals = [animal.name.lower() for animal in Animal.get_all_animal()]
    if name in existing_animals:
        print(f"Animal '{name.capitalize()}' already exists in the database. Creation canceled.")
        return

    # this Creates a new animal instance
    animal = Animal.create(name)
    print(f"--------------------------------------------------\nAnimal '{animal.name.capitalize()}' created and added to the Database.\n--------------------------------------------------")

    # this Creates a set to keep track of the selected foods for this animal ---- this is where I have to figure out how to add  ---> selected_foods = {food.id: "not supported" for food in Food.get_all_food()}
    selected_foods = set()

    # this sweet sweet baby allows you to add foods to the animal
    while True:
        print(f"\nSelect a food from the list to add to '{name}' (type 'done' or press 'enter' to finish):\n")
        list_foods()

        food_name = input("\nFood name: ").strip().lower()

        # here is the break that ends the process if done
        if food_name == 'done' or not food_name:
            
            done_setup = input(f"\n------------------------------------------------------------\nAre you sure you're done setting up '{name}'? (yes/no): \n------------------------------------------------------------\n\nResponse: ").strip().lower()
            if done_setup == 'yes':
                print(f"\n---------------------------------------\nAnimal '{animal.name.capitalize()}' setup is complete.\n---------------------------------------")
                break
            elif food_name == 'no':
                print(f"Setup for '{name}' continues. Add more foods.")
                continue



        # having a slight issue where if you press enter and then follow up with no I am getting below error message regardless of working ---
        # this is where I Check if the food exists in the database
        food = Food.find_by_name(food_name)
        if not food:
            print(f"\nFood '{food_name}' not found in the database.\n Please add the food to the database first.")
        else:
            # Checks if the food is already added to this animal because why not
            if food.id in selected_foods:
                print(f"-------------------------------------------------\n <!> '{food.name}' is already added to '{animal.name}'. <!> \n-------------------------------------------------")
            else:

                # Creates an AnimalFood instance to associate the food with the animal and voila!!!!!
                is_safe = input(f"Is '{food.name}' safe for '{animal.name}'? (true/false): ").strip().lower()
                if is_safe not in ['true', 'false']:
                    print("-------------------------------------------------\n <!><!> Invalid input. Please enter 'true' or 'false. <!><!> \n-------------------------------------------------")
                else:
                    AnimalFood.create(animal.id, food.id, is_safe) # here is the creation
                    selected_foods.add(food.id) # heres where we add it
                    print(f"\n------------------------------------------------------------------------------\n'{food.name}' added to '{animal.name}' as {'safe' if is_safe == 'true' else 'unsafe'} food.\n------------------------------------------------------------------------------") # my happy confirmed message
















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
    print("\n--------------\nSpecies List:\n--------------")
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
    from cli import main # ---> here Im importing main from CLI so I can kill my function and send it back to menu upon cooper code
    list_animals()
    current_name = input("----------------------------------------------------\nType the animal whose name you wish to change: ")
    animal = Animal.find_by_name(current_name)
    if not animal:
        print(f"----------------------------\n <!> Animal '{current_name}' not found <!> \n----------------------------")
        return
    while True:
        new_name = input(f"-------------------------------------------\nWhat would you like to switch '{current_name}' to: ")
        # Checks if new_name is an empty string
        if not new_name.strip(): 
            print("----------------------------------------------------\n!!!>>>>  Please provide a usable name.  <<<<!!!")
            break
        if new_name.strip().lower() == "cooper":
            print(f"------------------------------------------------------------\n <!> CATUION <!> \n------------------------------------------------------------ \n We do not allow 'Coopers' \n------------------------------------------------------------ \n'Cooper' cannot be added to the database. Creation canceled.\n------------------------------------------------------------")
            main()
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



# def update_animal_name():
#     from cli import main # ---> here Im importing main from CLI so I can kill my function and send it back to menu upon cooper code
#     list_animals()
#     current_name = input("----------------------------------------------------\nType the animal whose name you wish to change: ")
#     animal = Animal.find_by_name(current_name)
#     if not animal:
#         print(f"----------------------------\n <!> Animal '{current_name}' not found <!> \n----------------------------")
#         return
    
#     new_name = input(f"-------------------------------------------\nWhat would you like to switch '{current_name}' to: ")
#     # Checks if new_name is an empty string
#     if not new_name.strip(): 
#         print("----------------------------------------------------\n!!!>>>>  Please provide a usable name.  <<<<!!!")
#         return
#     if new_name.strip().lower() == "cooper":
#         print(f"------------------------------------------------------------\n <!> CATUION <!> \n------------------------------------------------------------ \n We do not allow 'Coopers' \n------------------------------------------------------------ \n'Cooper' cannot be added to the database. Creation canceled.\n------------------------------------------------------------")
#         main()
#         return

#     while True:
#         confirmation = input(f"-----------------------------------------\nDo you want to update '{current_name}' to '{new_name}'? (yes/no)\n-----------------------------------------\nResponse: ").strip().lower()
#         if confirmation == "yes":
#             animal.update(new_name)
#             print(f"--------------------------------------------------\nThe name of animal '{current_name}' has been updated to '{new_name}'\n--------------------------------------------------")
#             break
#         elif confirmation == "no":
#             print(f"------------------------------------\n <!> Update '{current_name}' name canceled. <!> \n------------------------------------\n\n")
#             break
#         else:
#             print("------------------------------------\n!!!>>>>  Please Confirm (yes/no).  <<<<!!!")






# ------------------------------------------------------------------
# Below is the helper to LIST ALL UNSAFE FOODS FOR A SPECIFIC ANIMAL
# ------------------------------------------------------------------




def unsafe_foods_for_animal():
    
    while True:
        list_animals() # This shows list of animals for user to choose from
        animal_name = input("\n----------------------------------------------\nWhich animal would you like to check \n----------------------------------------------\n(enter '1' to return to menu):\n\n> ")
        
        if animal_name == "1": # <---- this will return to main menu
            return
        
        animal = Animal.find_by_name(animal_name)
        
        if not animal:
            print(f"Animal '{animal_name}' not found")
            continue

        unsafe_foods = []
        for animal_food_id in animal.animal_foods_ids():
            animal_food = AnimalFood.find_unsafe_by_id(animal_food_id)
            if animal_food:
                food = Food.find_by_id(animal_food.fk_food)
                if food:
                    unsafe_foods.append(food.name)

        unsafe_foods.sort()

        if unsafe_foods:
            print(f"\n------------------------\nUnsafe Foods for '{animal_name}':\n------------------------")
            for name in unsafe_foods:
                print(f"- {name}")
        else:
            print(f"No unsafe foods found for '{animal_name}'")

        another_animal = input("\nDo you want to check another animal? (y/n): ")
        if another_animal.lower() != "y":
            return


#----------------------------------------
# My first rewrite attempt below
#----------------------------------------

# def unsafe_foods_for_animal():
#     list_animals()
#     animal_name = input("\n----------------------------------------------\nWhich animal would you like to check \n----------------------------------------------\n(enter '1' to return to menu):\n\n> ")
    
#     if animal_name == "1":
#         return
    
#     animal = Animal.find_by_name(animal_name)
    
#     if not animal:
#         print(f"Animal '{animal_name}' not found")
#         return

#     unsafe_foods = []
#     for animal_food in [AnimalFood.find_unsafe_by_id(id) for id in animal.animal_foods_ids()]:
#         if animal_food:
#             food = Food.find_by_id(animal_food.fk_food)
#             if food:
#                 unsafe_foods.append(food.name)

#     unsafe_foods.sort()

#     if unsafe_foods:
#         print(f"\n------------------------\nUnsafe Foods for '{animal_name}':\n------------------------")
#         for name in unsafe_foods:
#             print(f"- {name}")
#     else:
#         print(f"No unsafe foods found for '{animal_name}'")

# ------------------------------------
# Jessica's code below
# ------------------------------------

# def unsafe_foods_for_animal():
#     from cli import menu
#     #ask for a species
#     list_animals() #  ----->  hey jess I added this here for functionality -CO
#     animal_name = input("\n----------------------------------------------\nWhich animal would you like to check \n----------------------------------------------\n(enter '1' to return to menu):\n\n> ")
#     # print(animal_name)

#     #get the id of the species from animal table
#     animal = Animal.find_by_name(animal_name)
#     # print(animal)
#     if animal_name == "1":
#         return
#     elif not animal:
#         print(f"Animal '{animal_name}' not found")
#         unsafe_foods_for_animal()
    
#     #get all animal_foods ids for that animal
#     all_ids = animal.animal_foods_ids() #returns a list of ids
#     # print(all_ids)

#     #get all fk_foods ids where isSafe == false
#     unsafe = []
#     for id in all_ids:
#         animal_food = AnimalFood.find_unsafe_by_id(id)
#         if animal_food != None:
#             unsafe.append(animal_food)
#     # print(unsafe)

#     #iterate through AnimalFood objects and return a list of their fk_food values
#     fk_food_values = []
#     for af_object in unsafe:
#         fk = af_object.fk_food
#         fk_food_values.append(fk)
#     # print(fk_food_values)

#     #iterate over list to return foods table names for each id
#     food_names = []
#     for id in fk_food_values:
#         food_obj = Food.find_by_id(id)
#         name = food_obj.name
#         food_names.append(name)
#     # print(food_names)

#     #alphabetize the names
#     sorted_names = sorted(food_names)

#     #print the names
#     print(f"\n------------------------\nUnsafe Foods for '{animal_name}':\n------------------------")
#     for name in sorted_names:
#         print(f"- {name}")










# --------------------------------------------------------------
# Below is the helper to SHOW WEBMD RESULTS
# --------------------------------------------------------------


# WebMD results
def web_md():
    response = input("\nAre you sure that you would like to check WebMD? [yes/no]\n\nResponse:")
    if response == "yes":
        print("BeeYoop BeeDeepBoom Weeop DEEpaEEya... It's probably cancer.\n")
        web_m_dumper()
        confirmation = input("\n---> press any key to exit....")
        if not confirmation:
            return
    elif response == "no":
        print("\n---------------------\nSmart Choice\n---------------------")
    else:
        print("\n------------------------------------------\n <!> Please Type yes' or 'no' <!> \n------------------------------------------")
        web_md()









# ----------------------------------------------------------------
# TEST CODE ---- this is the code to add change or modify foods
# need to figure out how to call Jessica's code here to print out list of foods so you know what you're editing
# ----------------------------------------------------


def update_animal():
    list_animals() # this shows whole list of animals
    animal_name = input("Enter the name of the animal you want to update: ").strip().lower()
  #---> this compares against database
    animal = Animal.find_by_name(animal_name)
    if not animal:
        print(f"Animal '{animal_name.capitalize()}' not found in the database.")
        return
  
    print(f"Current food associations for '{animal_name}':") # Displays current associations
    show_animal_foods(animal_name)

    while True:
        action = input("Add, remove, or alter_safe Foods (done to finish): ").strip().lower()

        if action == 'done':
            break
        elif action == 'add':
            # Add a new food association
            food_name = input("Food name: ").strip().lower()
            is_safe = input("Is it safe (true/false): ").strip().lower()
            # Add to the database
        elif action == 'remove':
            # Remove a food 
            food_name = input("Food name to remove: ").strip().lower()
            # Remove from the animal 
        elif action == 'alter_safe':
       #---> Change whether a food is safe or not
            food_name = input("Food name to modify: ").strip().lower()
            is_safe = input("Updated safety status (true/false): ").strip().lower()
            # Update in the database

    print(f"Food associations for '{animal_name}' have been updated.")



# ---------------------------------------------------------------------------------------------------
# TEST CODE ---- This is code to show all foods for an animal and then present the as not supported, safe or not safe
# ----------------------------------------------------------------------------------------------------

def show_animal_foods(animal_name):
    animal = Animal.find_by_name(animal_name)
    if animal:
        animal_foods = AnimalFood.find_by_animal(animal)
        print(f"Foods associated with '{animal_name}':")
        for animal_food in animal_foods:
            food = Food.find_by_id(animal_food.food_id)
            safety_status = "safe" if animal_food.is_safe == "true" else "not safe"
            print(f"{food.name}: {safety_status}")
    else:
        print(f"Animal '{animal_name.capitalize()}' not found in the database.")














# def show_animal_foods(animal_name):
#     animal = Animal.find_by_name(animal_name)
#     if not animal:
#         print(f"Animal '{animal_name}' not found.")
#         return


#     animal_foods = AnimalFood.find_by_animal(animal.id)
#     if animal_foods is None:
#         print(f"No food associations found for '{animal_name}'.")
#         return
#     print(f"Foods associated with '{animal_name}':")

#     for animal_food in animal_foods:
#         food = Food.find_by_id(animal_food.fk_food)
#         if food:
#             food_name = food.name
#             is_safe = animal_food.is_safe
#             if is_safe is None:
#                 print(f"Food: {food_name}, Safety: Not Supported")
#             else:
#                 print(f"Food: {food_name}, Safety: {is_safe}")
#         else:
#             print("Food not found for this association.")



# def show_foods_for_animal():
#     list_animals()
#     animal_name = input("\n----------------------------------------------\nWhich animal's foods would you like to check? \n----------------------------------------------\n(enter '1' to return to the menu):\n\n> ")

#     if animal_name == "1":
#         return

#     animal = Animal.find_by_name(animal_name)

#     if not animal:
#         print(f"Animal '{animal_name}' not found")
#         return

#     animal_foods = []
#     for animal_food_id in animal.animal_foods_ids():
#         animal_food = AnimalFood.find_by_id(animal_food_id)
#         if animal_food:
#             food = Food.find_by_id(animal_food.fk_food)
#             if food:
#                 is_safe = "Safe" if animal_food.is_safe == "true" else "Unsafe"
#                 animal_foods.append((food.name, is_safe))

#     if animal_foods:
#         print(f"\n------------------------\nFoods for '{animal_name}':\n------------------------")
#         for food, is_safe in animal_foods:
#             print(f"- {food} ({is_safe})")
#     else:
#         print(f"No foods found for '{animal_name}'")

#     another_animal = input("Do you want to check another animal? (y/n): ")
#     if another_animal.lower() != "y":
#         return