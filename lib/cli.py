# lib/cli.py
from seed import Animal, AnimalFood, Food



from helpers import (
    exit_program,
    delete_animal,
    create_animal,
    list_foods,
    list_animals, 
    unsafe_foods_for_animal,
    update_animal_name
)

def main():
    while True:
        # from models.AnimalFood import AnimalFood
        # print(AnimalFood.all)
        menu()
        choice = input("\n> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_animal()
        elif choice == "2":
            delete_animal()
        elif choice == "3":
            update_animal_name()
        elif choice == "4":
            list_foods()
        elif choice == "5":
            list_animals()
        elif choice == "6":
            unsafe_foods_for_animal()
        else:
            print("----------------\n <!> Invalid choice <!> \n----------------")

def menu():
    print("\n\n----- Please select an option -----\n")
    print("0. Exit le program")
    print("1. Add a new animal")
    print("2. Delete an animal")
    print("3. Update an animal's name")
    print("4. List all currently supported foods from database")
    print("5. List all currently supported animals from database")
    print("6. List all unsafe foods for an animal")

if __name__ == "__main__":
    main()