# lib/cli.py
from seed import Animal, AnimalFood, Food

from helpers import (
    exit_program,
    delete_animal,
    create_animal,
    list_foods,
    list_animals,
    web_md
)

def main():
    while True:
        # from models.AnimalFood import AnimalFood
        # print(AnimalFood.all)
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_animal()
        elif choice == "2":
            delete_animal()
        elif choice == "3":
            list_foods()
        elif choice == "4":
            list_animals()
        elif choice == "9":
            web_md()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a new animal")
    print("2. Delete animal")
    print("3. List all currently supported foods from database")
    print("4. List all currently supported animals from database")
    print("9. Check WebMD")

if __name__ == "__main__":
    main()